from typing import Protocol


class ProductClientInterface(Protocol):

    def get_product(self, product_id: int):
        ...

    def reduce_quantity(self, product_id: int, quantity: int):
        ...

    def increase_quantity(self, product_id: int, quantity: int):
        ...

