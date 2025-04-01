from typing import List, Optional
from .models import Item

class InMemoryDB:
    def __init__(self):
        self.items: List[Item] = []
        self.current_id: int = 1

    def get_all_items(self) -> List[Item]:
        return self.items

    def get_item(self, item_id: int) -> Optional[Item]:
        return next((item for item in self.items if item.id == item_id), None)

    def create_item(self, item: Item) -> Item:
        item.id = self.current_id
        self.current_id += 1
        self.items.append(item)
        return item

    def update_item(self, item_id: int, item: Item) -> Optional[Item]:
        index = next((i for i, x in enumerate(self.items) if x.id == item_id), None)
        if index is None:
            return None
        item.id = item_id
        self.items[index] = item
        return item

    def delete_item(self, item_id: int) -> bool:
        index = next((i for i, x in enumerate(self.items) if x.id == item_id), None)
        if index is None:
            return False
        self.items.pop(index)
        return True

# Create a singleton instance
db = InMemoryDB() 