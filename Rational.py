from fractions import Fraction

class Rational:
    '''
    a class of rational numbers (ratio of integers) with the following interfaces and behaviours
    '''
    def __init__(self, x, y):
        assert (isinstance(x, int)),'integers'
        assert (isinstance(y, int)),'integers'
        self.x = x
        self.y = y

    def __repr__(self):
        frac = Fraction(self.x, self.y)
        if self.y == 1 or frac._denominator == 1:
            # Rational(10,1)
            return str('%d'%frac._numerator)
        else:
            return str('%d/%d'%(frac._numerator, frac._denominator))
    
    def __int__(self):
        # convert to int
        return int(self.x / self.y)


    def __rtruediv__(self, other):
        # -1/r
        # unsupported operand type(s) for /: 'int' and 'Rational'
        if isinstance(other, int) or isinstance(other, float):
            deno1 = Fraction(self.x, self.y)
            deno2 = Fraction(other)
            recipro = deno2 / deno1
            return Rational(Fraction(recipro)._numerator, Fraction(recipro)._denominator)
        else:
            recipro = Fraction(other.x, other.y) / Fraction(self.x, self.y)
            return Rational(Fraction(recipro)._numerator, Fraction(recipro)._denominator)


    def __float__(self):
        # convert to float
        return float(self.x / self.y) 
   
    def __sub__(self, other):
        minus = Fraction(self.x, self.y) - Fraction(other.x, other.y)
        return Rational( Fraction(minus)._numerator, Fraction(minus)._denominator )


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            nomi = Fraction( self.x, self.y ) * Fraction( other ) #if number multiply nominator
            return Rational( Fraction(nomi)._numerator, Fraction(nomi)._denominator )
        else:
            fracForm = Fraction( self.x * other.x, self.y * other.y )
            return Rational( fracForm._numerator, fracForm._denominator )


    def __add__(self, other):
        plus = Fraction(self.x, self.y) + Fraction(other.x, other.y)
        return Rational(Fraction(plus)._numerator, Fraction(plus)._denominator)


    def __truediv__(self, other):
        # unsupported operand type(s) for /: 'Rational' and 'int'
        if isinstance(other, int) or isinstance(other, float):
            recipro = Fraction( self.x, self.y ) / Fraction(other)
            return Rational(Fraction(recipro)._numerator, Fraction(recipro)._denominator)

        else: 
            recipro = Fraction(other.x, other.y)/Fraction(self.x, self.y)
            return Rational(Fraction(recipro)._numerator, Fraction(recipro)._denominator)


    def __lt__(self, other):
        # '<' not supported between instances of 'Rational' and 'Rational'
        a = Fraction(self.x, self.y)
        b = Fraction(other.x, other.y)

        # return (a < b)

        if a == b:
            return NotImplemented
        else:
            return (a < b)

    def __neg__(self):
    # bad operand type for unary -: 'Rational'
        return Rational(- self.x, self.y)

    def __eq__(self, other):
    # implement the == operation
        return (self.x == other.x) and (self.y == other.y)


r = Rational(3,4)
# print(repr(r))
# print(-1/r)
# print(float(-1/r))
# print(int(r))
# print(int(Rational(10,3)))
# print(Rational(10,3) * Rational(101,8) - Rational(11,8))
# print(sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)]))
# print(Rational(100,10))
# print(-Rational(12345,128191) + Rational(101,103) * 30/ 44)
