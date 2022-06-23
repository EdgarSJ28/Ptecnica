from fastapi import APIRouter
from fastapi import FastAPI
from crud_db import delete_hash, save_hash
from product import Product
from crud_db import get_hash

#CRUD de la API con la db

router = APIRouter()

fake_db = [
{
  "id": "7a31ce8e-8fed-48d8-95b1-3d9c93256079",
  "metric": 6,
  "date": "2022-06-22 22:39:26.684823"
}
]

@router.post("/create", response_model = Product)
def create(product: Product):
    try:
        fake_db.append(product.dict())
        save_hash(key=product.dict()["id"], data=product.dict())
        return product
    except Exception as e:
        return e

@router.get("/get/{id}")
def get(id: str):
    try:
        data = get_hash(key=id)
        if len(data) == 0:
            product = list(filter(lambda field: field["id"] == id, fake_db))[0]
            save_hash(key=id, data=product)
            return product
        return data
    except Exception as e:
        return e

@router.delete("/delete/{id}")
def delete(id: str):
    try:
        keys = Product.__fields__.keys()
        delete_hash(key=id, keys=keys)
        product = list(filter(lambda field: field["id"] == id, fake_db))
        if len(product) != 0:
            fake_db.remove(product)

        return {
            "message": "success" 
        }
    except Exception as e:
        return e