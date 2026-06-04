"""Inventory management system."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Item:
    """Represents an inventory item."""

    def __init__(self, name: str, quantity: int = 1, category: str = "General", unit: str = "units"):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.unit = unit
        self.added_date = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "quantity": self.quantity,
            "category": self.category,
            "unit": self.unit,
            "added_date": self.added_date,
        }

    @classmethod
    def from_dict(cls, data: Dict):
        item = cls(data["name"], data["quantity"], data["category"], data["unit"])
        item.added_date = data.get("added_date", item.added_date)
        return item

    def __repr__(self):
        return f"{self.name} ({self.quantity} {self.unit})"


class Inventory:
    """Main inventory management class."""

    def __init__(self, storage_file: str = "inventory_data.json"):
        self.storage_file = storage_file
        self.items: Dict[str, Item] = {}
        self.load()

    def add_item(self, name: str, quantity: int = 1, category: str = "General", unit: str = "units") -> str:
        """Add or update an item in inventory."""
        name_lower = name.lower()
        if name_lower in self.items:
            self.items[name_lower].quantity += quantity
            return f"Updated {name}: now {self.items[name_lower].quantity} {self.items[name_lower].unit}"
        else:
            self.items[name_lower] = Item(name, quantity, category, unit)
            return f"Added {quantity} {unit} of {name} to inventory"

    def remove_item(self, name: str, quantity: Optional[int] = None) -> str:
        """Remove an item or reduce quantity."""
        name_lower = name.lower()
        if name_lower not in self.items:
            return f"Item '{name}' not found in inventory"

        item = self.items[name_lower]
        if quantity is None or quantity >= item.quantity:
            del self.items[name_lower]
            return f"Removed {name} from inventory"
        else:
            item.quantity -= quantity
            return f"Removed {quantity} {item.unit} of {name}. Remaining: {item.quantity} {item.unit}"

    def get_item(self, name: str) -> Optional[Item]:
        """Get an item by name."""
        return self.items.get(name.lower())

    def search_by_category(self, category: str) -> List[Item]:
        """Search items by category."""
        return [item for item in self.items.values() if item.category.lower() == category.lower()]

    def search_by_name(self, name: str) -> List[Item]:
        """Search items by partial name match."""
        name_lower = name.lower()
        return [item for item in self.items.values() if name_lower in item.name.lower()]

    def list_all(self) -> str:
        """Get a formatted list of all items."""
        if not self.items:
            return "Inventory is empty"
        result = "Current Inventory:\n"
        for item in self.items.values():
            result += f"  - {item.name}: {item.quantity} {item.unit} ({item.category})\n"
        return result

    def get_total_items(self) -> int:
        """Get total quantity of items."""
        return sum(item.quantity for item in self.items.values())

    def save(self):
        """Save inventory to JSON file."""
        data = {name: item.to_dict() for name, item in self.items.items()}
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        """Load inventory from JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.items = {name: Item.from_dict(item_data) for name, item_data in data.items()}
