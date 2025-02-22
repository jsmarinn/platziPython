add = lambda a, b: a + b
print(add(2, 3))

multiply = lambda a, b: a * b
print(multiply(5, 4))

numbers = range(11)
squared = lambda a: a ** 2
squared_numbers = [squared(x) for x in numbers]
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)