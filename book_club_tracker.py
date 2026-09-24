borrowed_records = [
    ("Alice", ("1984", "Fiction")),
    ("Bob", ("Dune", "Sci-Fi")),
    ("Charlie", ("1984", "Fiction")),
    ("Diana", ("Clean Code", "Tech")),
]

genre_limits = {"Fiction": 5, "Sci-Fi": 3, "Tech": 2}
unique_books = set()
member_summary = {}

for member, book_info in borrowed_records:
    title, genre = book_info
    unique_books.add(title)

    allowed_days = genre_limits[genre] if genre in genre_limits else 7
    priority = "High" if allowed_days <= 3 else "Normal"

    member_summary[member] = {
        "title": title,
        "genre": genre,
        "due_in_days": allowed_days,
        "priority": priority,
    }

print("MEMBER BORROW DETAILS:")
for name, info in member_summary.items():
    print(name, "->", info)

print("\nUNIQUE BOOKS BORROWED:")
print(list(unique_books))
