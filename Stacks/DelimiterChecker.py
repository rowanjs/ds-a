# opening delimiters that occur later should be closed before those occurring earlier
# delimiter: "{}", "[]", "()"
# c[ d]  correct 
# a{ b[ c] d} e  correct 
# a{ b( c] d} e  not correct; ] doesn't match ( 
# a[ b{ c} d] e}  not correct; nothing matches final } 
# a{ b( c) not correct; nothing matches opening {

from SimpleStack import Stack

stack = Stack(100)

expr = input()
errors = 0

for i, ele in enumerate(expr):
    if ele in "{[(":
        if stack.isFull():
             raise Exception("Stack overflow on expression")
        else:
            stack.push(ele)
    elif ele in "}])":
        if stack.isEmpty():
             print(f"Error: {ele} at positon {i} has no matching left delimiter")
             errors += 1
        else:
            left = stack.pop()
            if not (
                left == "{" and ele == "}" or
                left == "(" and ele == ")" or
                left == "[" and ele == "]"):
                    print(f'Error: {ele} at position {i} does not match left delimiter {left}')
                    errors += 1

if stack.isEmpty() and errors == 0:
    print(f'Delimiters balance in expression {expr}')
elif not stack.isEmpty():
     print("Expression missing right delimiters for", stack)







