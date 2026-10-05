import pandas as pd

file_path = "../dataset/Credit Risk Dataset.xlsx"
def extract_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: ", e)
        return None   
    