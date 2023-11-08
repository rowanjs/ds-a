from SimpleStack import *

words = input('Please write down the word you would like to reverse: ')

stack = Stack(100)

if not stack.isFull():
    for word in words:
        stack.push(word)

reverse = ''
while not stack.isEmpty():
    reverse += stack.pop()

print('The reverse of', words, 'is', reverse)