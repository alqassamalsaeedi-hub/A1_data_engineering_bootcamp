from sqlalchemy import Column,Integer,Float,ForeignKey,Date,DateTime,Boolean,String
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import create_engine

base = declarative_base()

class DimDate(base):
    __tablename__ = 'dim_date'
    date_sk = Column(Integer, primary_key=True)
    full_date = Column(Date, nullable=False)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    quarter = Column(Integer)
    is_weekend = Column(Boolean)


class DimCustmer(base):
    __tablename__ = 'dim_customers'
    customer_sk = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(50), index=True)
    cutmer_zip_code = Column(String(100))
    customer_city = Column(String(50))
    customer_state = Column(String(50))

    start_date = Column(Date)
    end_date = Column(Date)
    is_current = Column(Boolean, default=True)


class DimProduct(base):
    __tablename__ = 'dim_products'
    product_sk = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String(50), index=True)
    category_name_english = Column(String(100))
    weight_g = Column(Float)
    length_cm = Column(Float)
    height_cm = Column(Float)
    width_cm = Column(Float)

    start_date = Column(Date)
    end_date = Column(Date)
    is_current = Column(Boolean, default=True)


class DimSeller(base):
    __tablename__ = 'dim_sellers'
    seller_sk = Column(Integer, primary_key=True, autoincrement=True)
    seller_id = Column(String(50), index=True)
    city = Column(String(100))
    state = Column(String(10))
    start_date = Column(Date)
    end_date = Column(Date)
    is_current = Column(Boolean, default=True)



class FactSales(base):
    __tablename__ = 'fact_sales'
    sales_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(50))
    
    customer_sk = Column(Integer, ForeignKey('dim_customers.customer_sk'))
    product_sk = Column(Integer, ForeignKey('dim_products.product_sk'))
    seller_sk = Column(Integer, ForeignKey('dim_sellers.seller_sk'))
    order_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    
    price = Column(Float)
    freight_value = Column(Float)
    payment_value = Column(Float)
    payment_installments = Column(Integer)

class FactDelivery(base):
    __tablename__ = 'fact_delivery'
    delivery_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(50))
    customer_sk = Column(Integer, ForeignKey('dim_customers.customer_sk'))
    seller_sk = Column(Integer, ForeignKey('dim_sellers.seller_sk'))
    product_sk = Column(Integer, ForeignKey('dim_products.product_sk'))
    
    order_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    approved_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    carrier_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    delivered_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    estimated_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    
    actual_delivery_time = Column(Integer) 
    delivery_accuracy = Column(Integer)    

class FactReview(base):
    __tablename__ = 'fact_reviews'
    review_sk = Column(Integer, primary_key=True, autoincrement=True)
    review_id = Column(String(50))
    order_id = Column(String(50))
    product_sk = Column(Integer, ForeignKey('dim_products.product_sk'))
    review_date_sk = Column(Integer, ForeignKey('dim_date.date_sk'))
    review_score = Column(Integer)



engine_url = "postgresql+psycopg2://postgres:5114@localhost:5432/olist_dw"

def create_warehouse_schema(engine_url):
    try:
        engine = create_engine(engine_url)
        base.metadata.create_all(engine) 
        print("Warehouse Schema created successfully!")
    except Exception as e:
        print(f"error while creating{e}")


if __name__ == "__main__":
    create_warehouse_schema(engine_url)