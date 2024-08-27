# Implement an infinite generator function infinite_sequence() that yields numbers starting from 1 and increments by 1 indefinitely. Use next() to retrieve and print the first 10 numbers from this generator.

def infinite_sequence():
    numbers = 1
    while True:
        yield numbers
        numbers += 1

res = infinite_sequence()

for i in range(10):
    print(next(res))
