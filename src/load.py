from sqlalchemy import create_engine
import pandas as pd
DB_URL = 'postgresql+psycopg2://postgres:14102005@localhost:5432/credit_db'

def get_engine():
    try:
        engine = create_engine(DB_URL)
        return engine
    except Exception as e:
        print(f"Lỗi khởi tạo engine: {e}")
        return None

    
def upload_to_db(df, table_name, engine):
    if df is not None and engine is not None:
        try:
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Đã đẩy dữ liệu vào bảng '{table_name}' thành công.")
        except Exception as e:
            print(f"Lỗi khi đẩy dữ liệu lên DB: {e}")
    else:
        print("Dữ liệu hoặc Engine không hợp lệ.")