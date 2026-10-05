import httpx
PRODUCT_SERVICE_URL= "http://127.0.0.1:8000"
class ProductClient:
    def get_product(self,product_id:int):
        response=httpx.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        if response.status_code==404:
            return None
        response.raise_for_status()
        return response.json()

    def reduce_quantity(self,product_id:int,quantity:int):
        response=httpx.patch(f"{PRODUCT_SERVICE_URL}/products/{product_id}/quantity",params={"quantity":quantity})
        if response.status_code==404:
            return None
        response.raise_for_status()
        return response.json()
    
    def increase_quantity(self,product_id:int,quantity:int):
        response=httpx.patch(f"{PRODUCT_SERVICE_URL}/products/{product_id}/quantity/increase",params={"quantity":quantity})
        if response.status_code==404:
            return None
        response.raise_for_status()
        return response.json()