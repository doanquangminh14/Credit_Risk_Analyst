from sqlalchemy import create_engine

def connect_db():
    url = 'postgresql+psycopg2://postgres:14102005@localhost:5432/credit_db'
    return create_engine(url)