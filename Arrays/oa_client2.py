from orderedarray import *

# Part 1: testing the merge method
def second(x):
    return x[1]

arr1 = OrderedRecordArray(10,key=second)
arr1_items = [('x',1.0),('y',174.3),('z',165.3),('o',111)]
for tup in arr1_items:
    arr1.insert(tup)
print(arr1)
print(len(arr1))

arr2 = OrderedRecordArray(15,key=second)
arr2_items = [('d',2.03),('a',174.5),('e',65.6),('g',777),('p',0)]
for tup in arr2_items:
    arr2.insert(tup)
print(arr2)
print(len(arr2))

arr_merged = arr1.merge(arr2)
print('\n',arr_merged)
print(len(arr_merged))

def first(x):
    return x[0]

arr3 = OrderedRecordArray(5, key=first)
arr3_items = [('z',23.03),('ab',14.5)]
for tup in arr3_items:
    arr3.insert(tup)
arr_merged_diff_key = arr1.merge(arr3)
print('\n',arr_merged_diff_key)
print(len(arr_merged_diff_key))






