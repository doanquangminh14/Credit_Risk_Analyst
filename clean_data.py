def clean_credit_data(df):
    df['person_emp_length'] = df['person_emp_length'].fillna(0)
    df['loan_int_rate'] = df.groupby('loan_grade')['loan_int_rate'].transform('mean')
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    return df