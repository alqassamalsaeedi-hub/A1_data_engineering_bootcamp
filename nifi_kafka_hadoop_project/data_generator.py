import csv
import time
import random
import uuid
import os
from datetime import datetime
from faker import Faker

fake = Faker()
OUTPUT_DIR = r"D:\Data Engineering Bootcamp\spark-sql-and-pyspark-using-python3\spark-sql-and-pyspark-using-python3\streaming_input"
os.makedirs(OUTPUT_DIR, exist_ok=True)

recent_records = []

def generate_messy_record():
    global recent_records
    
    if recent_records and random.random() < 0.10:
        return random.choice(recent_records)

    record = {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": fake.numerify('CUST-####'),
        "timestamp": datetime.now().isoformat(),
        "product_category": random.choice(["Electronics", "Clothing", "Books", "Smart Home", "Sports"]),
        "ai_recommendation_score": round(random.uniform(0.1, 0.99), 2),
        "amount": round(random.uniform(15.0, 1500.0), 2),
        "status": random.choice(["completed", "failed", "processing"])
    }

    ts_chance = random.random()
    if ts_chance < 0.3:
        record["timestamp"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    elif ts_chance < 0.6:
        record["timestamp"] = str(int(time.time()))

    if random.random() < 0.15:
        keys = list(record.keys())
        record[random.choice(keys)] = ""

    if random.random() < 0.10:
        record["amount"] = random.choice([-150.50, "INVALID_AMOUNT", 9999999.99])

    recent_records.append(record)
    if len(recent_records) > 50:
        recent_records.pop(0)

    if random.random() < 0.05:
        return {"transaction_id": "CORRUPTED_ROW_MISSING_COLUMNS"} 

    return record

def stream_data():
    print(f"🚀 Starting data generation... Files are saved in directory: {OUTPUT_DIR}/")
    print("Press Ctrl+C to stop.")
    
    file_index = 1
    fieldnames = ["transaction_id", "customer_id", "timestamp", "product_category", "ai_recommendation_score", "amount", "status"]

    try:
        while True:
            filename = os.path.join(OUTPUT_DIR, f"ecommerce_stream_{int(time.time())}_{file_index}.csv")
            
            num_records = random.randint(5, 20)
            
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for _ in range(num_records):
                    record = generate_messy_record()
                    if "customer_id" not in record: 
                        file.write("CORRUPTED_DATA,MISSING,EVERYTHING\n")
                    else:
                        writer.writerow(record)
            
            print(f"✅ File created: {filename} ({num_records} records)")
            file_index += 1
            
            time.sleep(5.0)
            
    except KeyboardInterrupt:
        print("\n🛑 Data generation stopped successfully.")

if __name__ == "__main__":
    stream_data()