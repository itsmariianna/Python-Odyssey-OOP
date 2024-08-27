# Create a generator function custom_filter(func, iterable) that mimics the behavior of the built-in filter() function. It should yield items from iterable where func(item) returns True. Test this function with a list of integers and a lambda function that checks if the number is even.

def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

even = lambda x: x % 2 == 0
ls = [1, 2, 3, 4, 5, 6]
res = custom_filter(even, ls)

for i in res:
    print(i)
