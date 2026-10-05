from sqlalchemy.orm import Session

from app.orders.models.order import Order


class OrderRepository:

    def get_all(self, db: Session):
        return db.query(Order).all()

    def get_by_id(self, db: Session, order_id: int):
        return db.query(Order).filter(
            Order.id == order_id
        ).first()

    def create(self, db: Session, order: Order):
        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    def delete(self, db: Session, order: Order):
        db.delete(order)
        db.commit()