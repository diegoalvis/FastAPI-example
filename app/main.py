from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="FastAPI Example",
    description="A modern FastAPI project template",
    version="1.0.0"
)

# Pydantic models for request/response
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage
items_db = []
current_id = 1

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Example"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    global current_id
    item.id = current_id
    current_id += 1
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    index = next((i for i, x in enumerate(items_db) if x.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[index] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    index = next((i for i, x in enumerate(items_db) if x.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db.pop(index)
    return {"message": "Item deleted successfully"} 