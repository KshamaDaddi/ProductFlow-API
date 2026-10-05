from typing import Protocol

from sqlalchemy.orm import Session

from app.orders.models.order import Order


class OrderRepositoryInterface(Protocol):

    def get_all(self, db: Session):
        ...

    def get_by_id(self, db: Session, order_id: int):
        ...

    def create(self, db: Session, order: Order):
        ...

    def delete(self, db: Session, order: Order):
        ...

