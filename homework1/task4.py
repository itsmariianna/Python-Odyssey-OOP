# Use a generator expression to create a generator that yields the squares of numbers from 1 to 20. Iterate through this generator to print all squared values.

generator_squares = (x**2 for x in range(1, 21))
for i in generator_squares:
    print(i)
