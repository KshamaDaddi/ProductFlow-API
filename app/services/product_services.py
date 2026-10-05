from sqlalchemy.orm import Session

from app.models.product import Product
from app.repository.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def get_all_products(self, db: Session):
        return self.repository.get_all(db)

    def get_product_by_id(self, db: Session, product_id: int):
        return self.repository.get_by_id(db, product_id)

    def create_product(self, db: Session, product_data):
        new_product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            quantity=product_data.quantity
        )

        return self.repository.create(db, new_product)

    def update_product(self, db: Session, product_id: int, product_data):
        existing_product = self.repository.get_by_id(db, product_id)

        if existing_product is None:
            return None

        existing_product.name = product_data.name
        existing_product.description = product_data.description
        existing_product.price = product_data.price
        existing_product.quantity = product_data.quantity

        return self.repository.update(db, existing_product)

    def delete_product(self, db: Session, product_id: int):
        existing_product = self.repository.get_by_id(db, product_id)

        if existing_product is None:
            return False

        self.repository.delete(db, existing_product)

        return True
    
    def reduce_product_quantity(self, db: Session, product_id: int, quantity: int):
        product = self.repository.get_by_id(db, product_id)

        if product is None:
            return None

        if product.quantity < quantity:
            raise ValueError("Insufficient product quantity available")

        product.quantity -= quantity

        return self.repository.update(db,product)
    
    def increase_product_quantity(self, db: Session, product_id: int, quantity: int):
        product = self.repository.get_by_id(db, product_id)

        if product is None:
            return None

        product.quantity += quantity

        return self.repository.update(db,product)