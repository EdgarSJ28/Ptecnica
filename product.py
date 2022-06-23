import random
from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

#modelo del dispositivo electrico

def generate_uuid():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

def generate_metric():
    return int(random.randint(0,20))

class Product(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    metric: int = Field(default_factory=generate_metric)
    date: str = Field(default_factory=generate_date)


cc = Product()
print(cc.dict()["id"])