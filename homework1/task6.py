# Create a generator function repeat_element(element, times) that yields the given element a specified number of times. Test this generator with different inputs.

def repeat_element(element, times):
    for i in range(times):
        yield element

input_1 = repeat_element("hello", 3)
for i in input_1:
    print(i)

input_2 = repeat_element(4, 6)
for i in input_2:
    print(i)
    
input_3 = repeat_element([1, 2, 3, 4], 4)
for i in input_3:
    print(i)
