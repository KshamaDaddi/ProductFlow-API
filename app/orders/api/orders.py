
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.orders.schemas.order import OrderCreate, OrderResponse
from app.orders.services.order_service import OrderService
from app.orders.repository.order_repository import OrderRepository
from app.orders.services.product_client import ProductClient


def get_order_service() -> OrderService:
    return OrderService(
        repository=OrderRepository(),
        product_client=ProductClient()
    )


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    order_service: OrderService = Depends(get_order_service)
):
    try:
        created_order = order_service.create_order(db, order)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if created_order is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return created_order


@router.get("/", response_model=list[OrderResponse])
def get_all_orders(
    db: Session = Depends(get_db),
    order_service: OrderService = Depends(get_order_service)
):
    return order_service.get_all_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(
    order_id: int,
    db: Session = Depends(get_db),
    order_service: OrderService = Depends(get_order_service)
):
    order = order_service.get_order_by_id(db, order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    order_service: OrderService = Depends(get_order_service)
):
    deleted = order_service.delete_order(db, order_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {"message": "Order deleted successfully"}

