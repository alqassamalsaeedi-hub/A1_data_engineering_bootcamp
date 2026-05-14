import csv
import random
import os
import time
from faker import Faker
from datetime import datetime

fake = Faker()

# Directory for NiFi to monitor
output_dir = "generated_files"
os.makedirs(output_dir, exist_ok=True)

def generate_single_file_stream():
    """Generates a unique CSV file for each execution to simulate streaming"""
    
    # Number of records per file (Keep it 1 for true streaming)
    records_per_file = 50 
    records = []

    for _ in range(records_per_file):
        c_id = random.randint(1000, 9000)
        name = fake.name()
        email = fake.email()
        address = fake.city()
        phone = fake.phone_number()

        # Inject 5% Null values into the email field
        if random.random() < 0.10:
            email = ""
        
        record = [c_id, name, email, address, phone]
        records.append(record)
        
        # Inject 5% Duplicates (Adding the same record twice in one file)
        if random.random() < 0.10:
            records.append(record)

    # Generate a unique filename using timestamp and micro-seconds
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = os.path.join(output_dir, f"customer_{timestamp}.csv")
    
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Write CSV Header
        writer.writerow(["customer_id", "customer_name", "email", "address", "phone"])
        writer.writerows(records)

    print(f"📂 New file created: {file_path}")

if __name__ == "__main__":
    print("🚀 Infinite Data Generator Started...")
    print(f"📢 Monitoring directory: {output_dir}")
    print("⌨️  Press Ctrl + C to stop the process.")
    
    try:
        while True:
            generate_single_file_stream()
            
            # Adjusted sleep time for smoother NiFi ingestion
            # You can change 0.2 to 0.1 for faster flow, or 1.0 for slower
            time.sleep(5.0) 
            
    except KeyboardInterrupt:
        print("\n🛑 Data generation stopped by user.")