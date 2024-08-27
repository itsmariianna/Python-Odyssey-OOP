# Write a generator function prime_generator(n) that yields prime numbers up to n. Use this generator to print all prime numbers less than 100.

def prime_generator(n):
    for i in range(2, n):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            yield i
            
for i in prime_generator(100):
    print(i, end = " ")
