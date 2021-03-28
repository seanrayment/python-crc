class PolyGF2:
    '''
    A class that represents binary strings as polynomials. Implements
    operations in mod 2. This is effectively binary arithmetic with no carries,
    and can be used in CRC computations.
    '''

    def __init__(self, binary_string):
        binary_string = binary_string.lstrip('0')
        self.polynomial = ['1' if int(c) else '0' for c in binary_string]

    def bitstring(self):
        return ''.join(self.polynomial)

    def __str__(self):
        out = []
        for i in range(len(self.polynomial)):
            exp = len(self.polynomial) - 1 - i
            if self.polynomial[i] == '1':
                out.append(f'x^{exp}')
        if len(out) == 0:
            return '0'
        return ' + '.join(out)

    def to_int(self):
        if len(self.polynomial) == 0:
            return 0
        return int(''.join(self.polynomial), 2)

    def __add__(self, other):
        num1 = self.to_int()
        num2 = other.to_int()
        binary_result = bin(num1 ^ num2) # e.g. '0b10110'
        return PolyGF2(binary_result[2:])

    def __sub__(self, other):
        return self + other

    def __eq__(self, other):
        return self.polynomial == other.polynomial

    def __ge__(self, other):
        return len(self.polynomial) >= len(other.polynomial)

    def remainder(self, other):
        remainder = PolyGF2('0')
        for i in range(len(self.polynomial)):
            remainder = (remainder << 1) + PolyGF2(self.polynomial[i])
            multiplier = PolyGF2('1') if remainder >= other else PolyGF2('0')
            product = multiplier * other
            remainder = remainder - product

        return remainder

    def __lshift__(self, other):
        return PolyGF2(''.join(self.polynomial + ['0' for i in range(other)]))

    def __mul__(self, other):
        sum_list = []
        smaller = None
        bigger = None
        if self >= other:
            smaller = other
            bigger = self
        else:
            smaller = self
            bigger = other
        for i, val in enumerate(reversed(smaller.polynomial)):
            if val == '1':
                sum_list.append(bigger << i)
        sum = PolyGF2('0')
        for poly in sum_list:
            sum = sum + poly
        return sum
