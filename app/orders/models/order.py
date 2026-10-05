from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.product import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    product_id: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)