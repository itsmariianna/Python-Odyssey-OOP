class DynamicArray:

    # Initialization
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity


    # Dynamic Resizing
    def resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.data[i]

        self.data = new_array
        self.capacity = new_capacity


    # Appending to array
    def append(self, value) -> None:
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1


    # Capacity
    def capacity(self) -> int:
        return self.capacity
    

    # Element Access and Mutation
    def __getitem__(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            return self.data[index]

    def __setitem__(self, index: int, value) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            self.data[index] = value


    # String Representations
    def __str__(self) -> str:
        return f"[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"

    def __repr__(self) -> str:
        return f"DynamicArray({self.data[:self.size]})"


    # Length and Capacity
    def __len__(self) -> int:
        return self.size

    
    # Arithmetic Operations
    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            return NotImplemented
        result = DynamicArray(self.size + other.size)
        result.size = self.size + other.size
        for i in range(self.size):
            result.data[i] = self.data[i]
        for i in range(other.size):
            result.data[self.size + i] = other.data[i]
        return result

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Unsupported operation")
        for i in range(other.size):
            self.append(other.data[i])
        return self


    # Rich Comparisons
    # Equality (==)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.data[i] != other.data[i]:
                return False
        return True
        
    # Inequality (!=)
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.data[i] != other.data[i]:
                return True
        return False

    # Less than (<)
    def __lt__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size < other.size:
            return True
        elif self.size > other.size:
            return False
        elif self.size == other.size:
            for i in range(self.size):
                if self.data[i] < other.data[i]:
                    return True
                elif self.data[i] > other.data[i]:
                    return False
        return False

    # Less or equal (<=)
    def __le__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size < other.size:
            return True
        elif self.size > other.size:
            return False
        elif self.size == other.size:
            for i in range(self.size):
                if self.data[i] < other.data[i]:
                    return True
                elif self.data[i] > other.data[i]:
                    return False
        return True

    # Greater than (>)
    def __gt__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size > other.size:
            return True
        elif self.size < other.size:
            return False
        elif self.size == other.size:
            for i in range(self.size):
                if self.data[i] > other.data[i]:
                    return True
                elif self.data[i] < other.data[i]:
                    return False
        return False
    
    # Greater or euqal (>=)
    def __ge__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size > other.size:
            return True
        elif self.size < other.size:
            return False
        elif self.size == other.size:
            for i in range(self.size):
                if self.data[i] >= other.data[i]:
                    return True
                elif self.data[i] < other.data[i]:
                    return False
        return True



    # Iteration Support
    def __iter__(self):
        for i in range(self.size):
            yield self.data[i]


    # Hash Support
    def __hash__(self) -> int:
        raise TypeError("DynamicArray is mutable and cannot be hashed.")


# Example Usage
if __name__ == '__main__':

    arr1 = DynamicArray()
    arr1.append(1)
    arr1.append(2)
    arr1.append(3)
    arr1.append(4)

    arr2 = DynamicArray()
    arr2.append(5)
    arr2.append(6)
    arr2.append(7)
    arr2.append(8)

    arr3 = arr1 + arr2
    print(arr3)

    arr1 += arr2
    print(arr1)

    print(arr1.__len__())

    arr2.__setitem__(2, 134)
    print(arr2)

    print(arr3.__getitem__(4))
    
