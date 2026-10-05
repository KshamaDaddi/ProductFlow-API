from app.orders.services.product_client import ProductClient
client=ProductClient()
product=client.get_product(1)
print(product)