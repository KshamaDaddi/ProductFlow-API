from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def get_all(self, db: Session):
        return db.query(Product).all()

    def get_by_id(self, db: Session, product_id: int):
        return db.query(Product).filter(
            Product.id == product_id
        ).first()
    def create(self, db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    def update(self,db:Session,product:Product):
        db.commit()
        db.refresh(product)
        return product
    def delete(self,db:Session,product:Product):
        db.delete(product)
        db.commit()
