
import data
import clean_data
import pandas as pd
if __name__ == "__main__":
    print("--- Bắt đầu luồng xử lý dữ liệu ---")
    print("Đang đọc file Excel...")
    df = pd.read_excel('Credit Risk Dataset.xlsx')

    print("Đang làm sạch dữ liệu...")
    df_cleaned = clean_data.clean_credit_data(df)
    
    print("Đang đẩy dữ liệu vào PostgreSQL...")
    engine = data.connect_db()
    df_cleaned.to_sql('credit_table', engine, if_exists='replace', index=False)