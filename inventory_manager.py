inventory = {
    "item_101": ("Laptop", 1200, 8),
    "item_102": ("Mouse", 25, 45),
    "item_103": ("Monitor", 300, 15),
    "item_104": ("Keyboard", 75, 5),
    "item_105": ("Headset", 110, 0),
}

categories = {
    "electronics": {"Laptop", "Monitor"},
    "accessories": {"Mouse", "Keyboard", "Headset"},
}

stock_report = {}
low_stock_alerts = set()
total_valuation = 0

for item_id, details in inventory.items():
    name, price, qty = details
    status = "Out of Stock" if qty == 0 else ("Low Stock" if qty < 10 else "In Stock")
    
    if qty < 10:
        low_stock_alerts.add(name)
        
    item_val = price * qty
    total_valuation += item_val
    
    stock_report[item_id] = {
        "name": name,
        "price": price,
        "quantity": qty,
        "status": status,
        "value": item_val,
        "category": "Electronics" if name in categories["electronics"] else "Accessories"
    }

highest_val_item = max(
    stock_report.items(),
    key=lambda x: x[1]["value"]
)[1]["name"] if stock_report else "None"

print("INVENTORY REPORT:")
for k, v in stock_report.items():
    print(k, v)

print("\nALERTS & SUMMARY:")
print("Total Inventory Value:", total_valuation)
print("Top Value Asset:", highest_val_item)
print("Restock Priority Items:", low_stock_alerts)