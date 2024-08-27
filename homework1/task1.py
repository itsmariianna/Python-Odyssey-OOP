# Create a generator function fibonacci_generator(n) that yields the first n Fcibonacci numbers. Test your generator by printing all numbers yielded by it.

def fibonacci_generator(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a = b
        b = a + b
        count += 1
        
for i in fibonacci_generator(8):
    print(i, end = " ")
