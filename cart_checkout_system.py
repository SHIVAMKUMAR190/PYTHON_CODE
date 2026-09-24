catalog = {
    "P101": ("Mechanical Keyboard", 65.0),
    "P102": ("USB-C Cable", 12.0),
    "P103": ("Gaming Mouse", 45.0),
    "P104": ("Desk Mat", 20.0),
}

customer_cart = [("P101", 1), ("P102", 3), ("P104", 2)]
discount_codes = {"SAVE10", "FALL2026", "VIP50"}
applied_code = "SAVE10"

cart_breakdown = []
subtotal = 0.0
items_ordered = set()

for pid, qty in customer_cart:
    if pid in catalog:
        name, unit_price = catalog[pid]
        line_total = unit_price * qty
        subtotal += line_total
        items_ordered.add(name)

        cart_breakdown.append(
            {"id": pid, "product": name, "qty": qty, "total": line_total}
        )

discount_rate = 0.10 if applied_code in discount_codes else 0.0
discount_amt = subtotal * discount_rate
shipping_fee = 0.0 if subtotal > 100.0 else 10.0
final_total = (subtotal - discount_amt) + shipping_fee

status_tier = "Gold Customer" if final_total > 120.0 else "Standard Customer"

order_summary = {
    "items_count": len(cart_breakdown),
    "subtotal": round(subtotal, 2),
    "discount_applied": discount_amt > 0,
    "discount_amount": round(discount_amt, 2),
    "shipping": shipping_fee,
    "grand_total": round(final_total, 2),
    "tier": status_tier,
}

print("ORDER BREAKDOWN:")
for item in cart_breakdown:
    print(item)

print("\nUNIQUE ITEMS ORDERED:")
print(items_ordered)

print("\nCHECKOUT SUMMARY:")
for key, val in order_summary.items():
    print(f"{key}: {val}")
