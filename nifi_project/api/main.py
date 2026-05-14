from fastapi import FastAPI
from faker import Faker
import random

app = FastAPI()
fake = Faker()

@app.get("/clean-customers")
def get_clean_data():
    return [{"customer_id": i, "name": fake.name(), "email": fake.email()} for i in range(50)]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)