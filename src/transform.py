import pandas as pd
from src import extract

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['person_age'] <= 100]
    df = df.drop_duplicates()
    df['person_emp_length'] = df['person_emp_length'].fillna(0)
    df['loan_int_rate'] = df['loan_int_rate'].fillna(df.groupby('loan_grade')['loan_int_rate'].transform('mean'))
    return df
    
    