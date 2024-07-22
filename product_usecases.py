import uuid
from typing import Optional, List

from eshop.businsess_logic.order import Product
from eshop.data_access.product_repo import save,get_many, get_by_id


def product_create(name, price) -> Product:
    product = Product(
        id=str(uuid.uuid4()),
        name=name,
        price=price,
    )
    save(product)

    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)