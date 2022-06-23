from product import Product
from crud_db import save_hash

#productor para el envio de datos a la bd
#No termiando

def producer():
    while True:
        product = Product()
        save_hash(key=product.dict()["id"], data=product.dict())
 
    

