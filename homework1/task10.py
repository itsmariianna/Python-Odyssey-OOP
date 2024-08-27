#  Create a generator exception_propagator(iterable) that yields each item in iterable. If an item is "error", raise a ValueError exception with the message “An error occurred!“. Test this generator with a list containing the string "error".

def exception_propagator(iterable):
    for i in iterable:
        if i.lower() == 'error':
            raise ValueError("An error occurred!")
        yield i

ls = ['hello', 'python', 'spam', 'error', 'apple']
res = exception_propagator(ls)

try:
    for i in res:
        print(i)
except ValueError as e:
    print(f'ERROR: {e}')
