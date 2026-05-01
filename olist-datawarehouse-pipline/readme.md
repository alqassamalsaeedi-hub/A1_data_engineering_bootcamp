📊 Olist E-Commerce End-to-End Data Warehouse Project
Welcome to the Olist Data Warehouse project! This repository demonstrates a robust ETL pipeline and a modern data architecture designed to transform raw e-commerce data into actionable business insights. 🚀

🏗️ 1. Hybrid Architecture: Kimball meets Medallion
In this project, I implemented a Hybrid Architecture that combines the organizational clarity of the Medallion Architecture with the analytical power of the Kimball Dimensional Model.

🥉 Bronze Layer (Raw)
Source: Data is ingested directly from the original SQLite database.

State: Raw, unprocessed data representing the "Single Source of Truth."

🥈 Silver Layer (Transformed)
Processing: Data cleaning, handling missing values, and English translations.

SCD Type 2: Implementing Slowly Changing Dimensions to track historical changes in customer and seller attributes.

🥇 Gold Layer (Analytical)
Framework: Kimball Dimensional Modeling.

Output: High-performance Star Schema with Surrogate Keys, optimized for BI tools and complex SQL joins.

📐 2. Data Modeling (Star Schema)
The architecture is built around a Star Schema to simplify queries and enhance performance. 🌟

Dimensions (Who, What, Where, When):

dim_customers: Geographic and historical data of clients.

dim_products: Enriched product details with English categories.

dim_sellers: Seller location and performance attributes.

dim_date: A custom-generated time-dimension with a hierarchy (Year > Quarter > Month > Day).

Fact Tables (Quantitative Measures):

fact_sales: Revenue, price, and payment metrics.

fact_delivery: Logistics performance (Actual vs. Estimated delivery).

fact_reviews: Customer satisfaction and feedback scores.

⚙️ 3. Detailed ETL Pipeline (The Process)
📥 Phase 1: Extract
We use SQLAlchemy to interface with the SQLite source. Dataframes are loaded into memory for efficient processing.

🔄 Phase 2: Transform
This is where the heavy lifting happens:

Date Generation: Programmatically creating a 4-year date range with analytical flags (e.g., is_weekend).

Enrichment: Joining product categories with translation maps.

Surrogate Keys: Generating sk columns (Integer-based) to replace complex UUIDs/Hashes for faster indexing.

Lead Time Calculation: Calculating delivery_accuracy and actual_delivery_time to measure operational efficiency.

📤 Phase 3: Load
Data is pushed to PostgreSQL using a strict hierarchy:

Dimensions First: To satisfy Referential Integrity.

Facts Last: Linking all transactions to the validated dimensions.

Default Keys: Inserting a "Record 0" in the date dimension to handle NULL timestamps in the source.

🔍 4. Business Insights (SQL Analysis)
The warehouse is designed to answer critical business questions via SQL:

📈 Sales Trends: "How are sales trending month-over-month?"

👑 Customer Value: "Who are our top 10% customers by revenue?"

🚚 Logistics: "Which states have the highest average delivery delay?"

🛍️ Product Performance: "Which categories drive the highest profit margins?"

🛠️ 5. Tech Stack
Language: Python 🐍

Database Source: SQLite 🗄️

Data Warehouse: PostgreSQL 🐘

Libraries: Pandas, SQLAlchemy, Psycopg2.

Design: Kimball Dimensional Modeling & Medallion Architecture.

🚀 6. How to Run
Clone the repository.

Ensure you have PostgreSQL running locally.

Update the engine_url in the script with your credentials.

Run the ETL notebook/script.

Query the tables using pgAdmin or any BI tool!

Built with ❤️ for Data Engineering Excellence.