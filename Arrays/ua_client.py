#Client used to execute code
from unorderedarray import Array

# maxsize = 10
# array = Array(maxsize)
# array.insert('foo')
# array.insert('dunk')
# array.insert(57)
# array.insert(1756)
# array.insert(0.1)
# array.insert(789.967)
# array.insert('lingo')
# array.traverse()
# print(f'Maximum numeral value is {array.getMaxNum()}')
# print(array.deleteMaxNum())
# print(f'Maximum numeral value is {array.getMaxNum()}')

#create an descending sorting using deleteMaxNum
# sorted_desc = Array(maxsize)
# for i in range(len(array)):
#     val = array.deleteMaxNum()
#     if val is not None:
#         sorted_desc.insert(val)

# sorted_desc.traverse()

maxsize = 10
array = Array(maxsize)
array.insert('foo')
array.insert('dude')
array.insert('foo')
array.insert('foo')
array.insert('flute')
array.insert('dude')
array.insert('flute')
array.insert('flute')
array.insert('dude')
array.removeDupes()
array.traverse()


