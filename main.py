from fastapi import FastAPI
from products import router

app = FastAPI()

app.include_router(router, prefix="/products")