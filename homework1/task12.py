# Develop a generator function custom_zip(*iterables) that mimics the behavior of the built-in zip() function. It should yield tuples containing items from each iterable passed as arguments, stopping when the shortest iterable is exhausted. Test your generator with two or more lists of different lengths.

def custom_zip(*iterables):
    min_len = min(len(i) for i in iterables)
    for i in range(min_len):
        ls = []
        for j in iterables:
            ls.append(j[i])
        yield tuple(ls)

ls1 = [1, 2, 3, 4, 8]
ls2 = [4, 5, 6, 7]
res = custom_zip(ls1, ls2)

for i in res:
    print(i)
