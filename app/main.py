from fastapi import FastAPI, HTTPException
from typing import List
from .models import Item
from .database import db

app = FastAPI(
    title="FastAPI Example",
    description="A modern FastAPI project template",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Example"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return db.get_all_items()

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = db.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return db.create_item(item)

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    updated_item = db.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if not db.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"} 