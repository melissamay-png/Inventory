inventory = [
    {"item": "N95 Masks", "category": "PPE", "quantity": 250, "reorder_level": 100},
    {"item": "Syringes", "category": "Medical Supplies", "quantity": 1200, "reorder_level": 500},
    {"item": "IV Bags", "category": "Fluids", "quantity": 75, "reorder_level": 120},
    {"item": "Surgical Gloves", "category": "PPE", "quantity": 500, "reorder_level": 700},
    {"item": "Saline Solution", "category": "Fluids", "quantity": 150, "reorder_level": 150},
    {"item": "Ventilator Tubing", "category": "Respiratory", "quantity": 60, "reorder_level": 40}
]

print("=" * 60)
print("HOSPITAL INVENTORY REPORT")
print("=" * 60)

low_stock_count = 0

for item in inventory:

    status = (
        "LOW STOCK"
        if item["quantity"] < item["reorder_level"]
        else "OK"
    )

    print(
        item["item"],
        "-",
        item["category"],
        "-",
        item["quantity"],
        "-",
        status
    )

    if status == "LOW STOCK":
        low_stock_count += 1

print("\n" + "=" * 60)
print("LOW STOCK ITEMS")
print("=" * 60)

for item in inventory:
    if item["quantity"] < item["reorder_level"]:
        print(
            f"{item['item']} ({item['category']}) - "
            f"{item['quantity']} units "
            f"(Reorder Level: {item['reorder_level']})"
        )

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("Total Inventory Items:", len(inventory))
print("Items Needing Reorder:", low_stock_count)
