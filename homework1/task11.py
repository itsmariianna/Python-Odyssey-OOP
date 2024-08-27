# Write a generator function custom_reduce(func, iterable, initializer=None) that mimics the behavior of functools.reduce(). It should yield intermediate results of applying func cumulatively to the items of iterable, optionally starting with initializer. Test this function with a list of numbers and a lambda function that adds two numbers.

def custom_reduce(func, iterable, initializer = None):
    iterator = iter(iterable)
    if initializer is None:
        try:
            i = next(iterator)
        except StopIteration:
            return
    else:
        i = initializer
        yield i
    for item in iterator:
        i = func(i, item)
        yield i

adds_two_numbers = lambda x, y: x + y
ls = [1, 2, 3, 4, 5, 6, 7]
res = custom_reduce(adds_two_numbers, ls)

for i in res:
    print(i)
