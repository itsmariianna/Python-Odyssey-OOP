import math
class Fraction:

    #1. Initialization and Simplification
    def __init__(self, numerator: int, denominator: int):
        self.setNumerator(numerator)
        self.setDenominator(denominator)

    # Setter
    def setNumerator(self, value):
        if not isinstance(value, int):
            raise ValueError("Numerator should be an int type")
        self.__numerator = value

    def setDenominator(self, value):
        if not isinstance(value, int) or value == 0:
            raise ValueError("Denominator should be an int type and not eqaul to zero")
        self.__denominator = value

    # Getter
    def getNumerator(self):
        return self.__numerator 
    
    def getDenominator(self):
        return self.__denominator

    # Simplify
    def simplify(self):
        common_divisor = math.gcd(self.__numerator, self.__denominator)
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator


    # 2. String Representations
    def __str__(self) -> str:
        return f'{self.getNumerator()}/{self.getDenominator()}'
    
    def __repr__(self) -> str:
        return f'Fraction({self.getNumerator()}, {self.getDenominator()})'


    # 3. Arithmetic Operations
    # Addition
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.__numerator * other.__denominator) + (self.__denominator * self.__numerator)
            new_denominator = self.__denominator * other.__denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.__numerator * other.__denominator) - (self.__denominator * other.__numerator)
            new_denominator = self.__denominator * other.__denominator
            if new_numerator == 0:
                return 0
            return Fraction(new_numerator, new_denominator)
        return NotImplemented
    
    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.__numerator * other.__numerator
            new_denominator = self.__denominator * other.__denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented
    
    # Division
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.__numerator == 0:
                raise ZeroDivisionError("Can't devide to zero")
            new_numerator = self.__numerator * other.__denominator
            new_deniminator = self.__denominator * other.__numerator
            return Fraction(new_numerator, new_deniminator)
        return NotImplemented
    

    # 4. Rich Comparison Methods
    # Equal to
    def __eq__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator == self.__denominator * other.__numerator:
            return True
        else:
            return False

    # Not equal
    def __ne__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator == self.__denominator * other.__numerator:
            return False
        else:
            return True
        
    # Less than
    def __lt__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator < self.__denominator * other.__numerator:
            return True
        else:
            return False
        

    # Less than or equal to
    def __le__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator <= self.__denominator * other.__numerator:
            return True
        else:
            return False


    # Greater than
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator > self.__denominator * other.__numerator:
            return True
        else:
            return False
    

    # Greater or equal
    def __ge__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.__numerator * other.__denominator >= self.__denominator * other.__numerator:
            return True
        else:
            return False
        
    # 5. Hashing Support
    def __hash__(self) -> int:
        return hash((self.__numerator, self.__denominator))
    

    # 6. Additional Methods
    def __float__(self) -> float:
        float_number = self.__numerator / self.__denominator
        return float_number
    
    def __int__(self) -> int:
        int_number = math.floor(self.__numerator / self.__denominator)
        return int_number

    def __neg__(self) -> int:
        return Fraction(-self.__numerator, self.__denominator)



f1 = Fraction(2, 4)
f2 = Fraction(1, 2)
f3 = Fraction(5, 6)


    
        



