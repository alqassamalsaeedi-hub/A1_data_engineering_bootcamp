from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="Qassam Financial CSV API")

@app.get("/")
def home():
    return {"message": "Welcome! Use /rates to see CSV data"}

@app.get("/rates")
def get_rates():
    file_path = 'finance_data.csv'
    if os.path.exists(file_path):
        # قراءة ملف CSV وتحويله إلى قائمة من القواميس (JSON) ليعرضه المتصفح
        df = pd.read_csv(file_path)
        data = df.to_dict(orient='records')
        return {
            "total_records": len(data),
            "data": data
        }
    return {"error": "CSV file not found. Run the scraper first."}