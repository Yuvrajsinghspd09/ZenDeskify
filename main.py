import streamlit as st
import pandas as pd
from datetime import datetime
from database import get_db_connection, initialize_database
from model import analyze_sentiment
from preprocessing import preprocess_data, create_it_owner_mapping
from utils import adjust_weights, calculate_ticket_priority

initialize_database()
conn = get_db_connection()
cursor = conn.cursor()

st.title("IT Support Ticket System")

# User Ticket Submission
with st.form("ticket_form"):
    description = st.text_area("Describe your query", max_chars=500)
    requestor_seniority = st.number_input("Requestor Seniority (0-3)", min_value=0, max_value=3, step=1)
    filed_against = st.selectbox("Filed Against", ["Systems", "Software", "Access/Login", "Hardware"])
    ticket_type = st.selectbox("Ticket Type", ["Issue", "Request"])
    severity = st.selectbox("Severity", ["Unclassified-0", "Minor-1", "Normal-2", "Major-3", "Critical-4"])
    priority = st.selectbox("Priority", ["Unclassified-0", "Minor-1", "Normal-2", "Major-3", "Critical-4"])
    submitted = st.form_submit_button("Submit Ticket")

    if submitted:
        sentiment = analyze_sentiment(description)
        adjust_weights(sentiment)
        severity_val = int(severity.split('-')[1])
        priority_val = int(priority.split('-')[1])
        
        cursor.execute('''
        INSERT INTO tickets (requestor_seniority, filed_against, ticket_type, severity, priority, sentiment, description, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (requestor_seniority, filed_against, ticket_type, severity_val, priority_val, sentiment, description, datetime.now()))
        conn.commit()
        st.success("Ticket Submitted Successfully!")
