from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db

from app.schemas.product import ProductCreate, ProductResponse



from app.services.product_services import ProductService
product_service=ProductService()

router=APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return product_service.create_product(db, product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/", response_model=list[ProductResponse])
def get_products(db:Session=Depends(get_db)):
    products=product_service.get_all_products(db)
    return products

@router.get("/{product_id}",response_model=ProductResponse)
def get_product(product_id:int,db:Session=Depends(get_db)):
    product=product_service.get_product_by_id(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{product_id}/quantity")
def reduce_product_quantity(
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):
    try:
        product = product_service.reduce_product_quantity(
            db,
            product_id,
            quantity
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@router.patch("/{product_id}/quantity/increase")
def increase_product_quantity(
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):
    product = product_service.increase_product_quantity(
        db,
        product_id,
        quantity
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    try:
        updated_product = product_service.update_product(
            db,
            product_id,
            product
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product
    
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = product_service.delete_product(db, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}