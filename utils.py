feature_weights = {
    'Severity': 0.4,
    'Priority': 0.3,
    'days_open': 0.2,
    'requestor_seniority': 0.1
}

def adjust_weights(sentiment):
    if sentiment == 'negative':
        feature_weights['Severity'] = 0.5
        feature_weights['Priority'] = 0.4
        feature_weights['requestor_seniority'] = 0.1
    elif sentiment == 'neutral':
        feature_weights['Severity'] = 0.35
        feature_weights['Priority'] = 0.3
        feature_weights['requestor_seniority'] = 0.15
    else:
        feature_weights['Severity'] = 0.2
        feature_weights['Priority'] = 0.2
        feature_weights['requestor_seniority'] = 0.6

def calculate_ticket_priority(data):
    days_open = data['days_open'] if pd.notna(data['days_open']) else 0
    return (
        feature_weights['Severity'] * data['severity'] +
        feature_weights['Priority'] * data['priority'] +
        feature_weights['days_open'] * days_open +
        feature_weights['requestor_seniority'] * data['requestor_seniority']
    )
