# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


def sayHelo(name):
    print(f"hello, {name}!")


def getSum(num1, num2):
    total = num1 + num2
    return total


num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

getSum = lambda x, y: x + y
print(getSum(num1,num2))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression. Very similar to JS arrow functions
