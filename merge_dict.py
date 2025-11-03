
from collections import defaultdict

dicts = [
    {'a': 1, 'b': 2, 'd': 5},
    {'b': 3, 'c': 4, 'd': 6},
    {'a': 7, 'c': 8, 'e': 9}
]

merged = defaultdict(list)

for d in dicts:
    for key, value in d.items():
        merged[key].append(value)

# Convert back to regular dict if needed
merged = dict(merged)

print(merged)
