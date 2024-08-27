# Implement a generator function custom_map(func, iterable) that mimics the behavior of the built-in map() function. It should apply func to each item in iterable and yield the results one by one. Test your function with a sample list and a lambda function that squares each element.

def custom_map(func, iterable):
    for i in iterable:
        yield func(i)

square = lambda x: x ** 2
ls = [1, 2, 3, 4, 5]
res = custom_map(square, ls)

for i in res:
    print(i)
