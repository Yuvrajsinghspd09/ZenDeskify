import pandas as pd

def extract_numerical_value(column):
    return column.astype(str).str.extract(r'^(\d+)')[0].astype(float)

def preprocess_data(data):
    columns_to_process = ['Severity', 'Priority', 'Satisfaction', 'RequestorSeniority']
    for col in columns_to_process:
        data[col] = extract_numerical_value(data[col])
        data[col].fillna(data[col].mode()[0], inplace=True)
    return data

def create_it_owner_mapping(data):
    resolved_tickets = data.groupby(['FiledAgainst', 'TicketType', 'ITOwner']).size().reset_index(name='count')
    best_it_owner = resolved_tickets.loc[resolved_tickets.groupby(['FiledAgainst', 'TicketType'])['count'].idxmax()]
    return {(row['FiledAgainst'], row['TicketType']): row['ITOwner'] for _, row in best_it_owner.iterrows()}
