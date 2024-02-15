# Checking subset and superset:

set1 = {1, 2, 3, 4}
set2 = {2, 3}

# Subset
is_subset = set2.issubset(set1)
print("Is set2 a subset of set1?", is_subset)

# Superset
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)
