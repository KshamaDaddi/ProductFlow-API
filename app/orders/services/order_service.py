
from sqlalchemy.orm import Session

from app.orders.models.order import Order
from app.orders.interfaces.order_repository import OrderRepositoryInterface
from app.orders.interfaces.product_client import ProductClientInterface


class OrderService:

    def __init__(
        self,
        repository: OrderRepositoryInterface,
        product_client: ProductClientInterface
    ):
        self.repository = repository
        self.product_client = product_client

    def get_all_orders(self, db: Session):
        return self.repository.get_all(db)

    def get_order_by_id(self, db: Session, order_id: int):
        return self.repository.get_by_id(db, order_id)

    def create_order(self, db: Session, order_data):
        product = self.product_client.get_product(
            order_data.product_id
        )

        if product is None:
            return None

        if order_data.quantity > product["quantity"]:
            raise ValueError("Insufficient product quantity")

        updated_product = self.product_client.reduce_quantity(
            order_data.product_id,
            order_data.quantity
        )

        if updated_product is None:
            return None

        try:
            new_order = Order(
                product_id=order_data.product_id,
                quantity=order_data.quantity
            )

            return self.repository.create(db, new_order)

        except Exception:
            self.product_client.increase_quantity(
                order_data.product_id,
                order_data.quantity
            )
            raise

    def delete_order(self, db: Session, order_id: int):
        existing_order = self.repository.get_by_id(db, order_id)

        if existing_order is None:
            return False

        self.repository.delete(db, existing_order)

        return True

