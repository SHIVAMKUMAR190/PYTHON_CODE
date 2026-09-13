user_roles = {"Shivam": {"admin", "editor"}, "Guest": {"viewer"}}
user = "Shivam"
access = "Full Access" if "admin" in user_roles.get(user, set()) else "Restricted"
print(access)