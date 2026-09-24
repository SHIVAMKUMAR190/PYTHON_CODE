lst = [1, 2]
tup = (1, 2, 3)
st = {1, 2, 3, 4}
dt = {"a": 1}
largest = "Set" if len(st) > len(tup) and len(st) > len(lst) else "Other"
print(largest)
