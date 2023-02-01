from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: { "message": "Not found" }})

products_list = ["Product 1", "Product 2", "Product 3", "Product 4"]

@router.get("/")
async def products():
    return ["Product 1", "Product 2", "Product 3", "Product 4"]

@router.get("/{id}")
async def products(id: int):
    return products_list[id]