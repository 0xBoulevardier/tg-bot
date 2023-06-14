print("Hello, World!")

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(num) for num in numbers]

print(squared_numbers)
