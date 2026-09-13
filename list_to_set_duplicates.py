raw = [1, 2, 2, 3, 4, 4, 4, 5]
unique = set(raw)
has_dupes = "Duplicates" if len(raw) != len(unique) else "Unique"
print(unique)
print(has_dupes)