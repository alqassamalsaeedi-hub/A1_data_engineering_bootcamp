# 🚀 Data Engineering & Real-Time ETL Pipeline Project
A comprehensive data engineering system designed to ingest, transform, and clean customer data in real-time using Apache NiFi, Python, and FastAPI.

## 📋 1. Project Overview
This project demonstrates a robust ETL (Extract, Transform, Load) pipeline. It handles two distinct data streams:

Unclean Stream: Synthetic data generated via Python with intentional duplicates and null values.

Clean Stream: Data fetched via a REST API (FastAPI) representing a "gold standard" source.

## 🏗️ 2. System Architecture
The system architecture is built on three main pillars:

🐍 Python Data Generator: Simulates a real-world scenario by streaming CSV files with errors.

⚡ FastAPI Service: Acts as a clean external data source for cross-validation.

🌊 Apache NiFi: The heart of the project, orchestrating the entire flow from ingestion to storage.

![NiFi DataFlow Pipeline](images\dataflow.png)

## ⚙️ 3. The Data Pipeline (ETL Stages)
📥 A. Data Ingestion
File Ingestion: Using ListFile and FetchFile to monitor directories for new CSV arrivals.

API Ingestion: Using InvokeHTTP to programmatically fetch JSON data from our FastAPI server.

✨ B. Data Transformation (The Cleaning Logic)
This is where the magic happens! We used SQL inside NiFi (via QueryRecord) to clean the data:

SQL
SELECT 
    customer_id, 
    MAX(customer_name) AS customer_name, 
    MAX(email) AS email, 
    MAX(address) AS address, 
    MAX(phone) AS phone
FROM FLOWFILE
WHERE email IS NOT NULL AND email <> ''
GROUP BY customer_id
🚫 Deduplication: Handled via GROUP BY customer_id to ensure unique records.

🧹 Null Filtering: Handled via the WHERE clause to remove records with missing emails.

<table>
  <tr>
    <td><b>Before Cleaning (Dirty Data)</b></td>
    <td><b>After Cleaning (Clean Data)</b></td>
  </tr>
  <tr>
    <td><img src="images\dirty_data.png" width="400"></td>
    <td><img src="images\cleaned_data.png" width="400"></td>
  </tr>
</table>

## 🛠️ 4. Tech Stack
Orchestration: Apache NiFi

Programming: Python 3.10

Web Framework: FastAPI & Uvicorn

Environment: Docker & WSL (Ubuntu)

Query Language: SQL (Apache Calcite)

## 🚀 5. How to Run
Start NiFi: Run your Docker container.

Start Generator: Run python data_gen.py.

Start API: Run uvicorn main:app --host 0.0.0.0 --port 8000.

📥 Importing the Flow: You can import the provided flow_definition.json into any NiFi instance by right-clicking the canvas and selecting "Upload Flow Definition".

Execute Flow: Start all processors in the NiFi UI.

## ✅ 6. Key Achievements
Real-time Processing: Files are processed as soon as they are created.

Data Integrity: 100% success in removing duplicates and null entries.

Hybrid Ingestion: Successfully combined file-based and API-based data sources.

Prepared by: Alqassam Alsaeedi 🎓
Field: Data Engineering & AI
Date: May 2026