from fastapi import FastAPI

from app.api.products import router as product_router
from app.orders.api.orders import router as order_router
from app.database.connection import engine
from app.models.product import Base
from app.orders.models.order import Order


Base.metadata.create_all(bind=engine)

app=FastAPI()
print("tables:",Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)
print("Tables after create_all:",Base.metadata.tables.keys())

app.include_router(product_router)
app.include_router(order_router)
@app.get("/")
def root():
    return {"message": "Product API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}