#Script to test orderedarray module
from orderedarray import *

def second(x):
    return x[1]

maxSize = 1000
arr = OrderedRecordArray(maxSize, second)

#insert 10 items
records = [('a', 3.1), ('b', 7.5), ('c', 6.0), ('d', 3.1), ('e', 1.4), ('f', -1.2), ('g', 0.0), ('h', 7.5), ('i', 7.5), ('j', 6.0)]
for rec in records:
    arr.insert(rec)

print("Array containing", len(arr), "items:\n", arr)

delete_records = [('c', 6.0), ('g', 0.0), ('g', 0.0), ('b', 7.5), ('i', 7.5)]

for rec in delete_records:
    print("Deleting", rec, "returns", arr.delete(rec))

print("Array after deletions has", len(arr), "items:\n", arr)

for key in [4.4, 6.0, 7.5]:
    print(f'find ( {key} ) returns {arr.find(key)} and get ( {arr.find(key)} ) returns {arr.get(arr.find(key))}')