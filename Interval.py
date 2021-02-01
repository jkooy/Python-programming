class Interval(object):
    '''
    A interval function that represents a one-dimensional open interval on the real line. This main purpose of this class is to simplify overlapping continuous intervals. The code below should get you started but there are a lot of missing pieces that you will have to figure out.

    '''
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b

    def __repr__(self):
        return 'Interval(' + str(self._a) + ',' + str(self._b) + ')'

    def __eq__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        return self._a == other._a and self._b == other._b

    def __lt__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if (self._a > other._b):
            return True
        else:
            return False

    def __gt__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if (self._a < other._b):
            return True
        else:
            return False

    def __ge__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if (self._a <= other._b):
            return True
        else:
            return False

    def __le__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if (self._a >= other._b):
            return True
        else:
            return False

    def intersect(self, other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if(other._a<=self._a) and (self._a < other._b):
            return True
        elif self._a<other._a and other._a<self._b:
                return True
        else:
            return False

    def __add__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        if(self.intersect(other)):
            return Interval(min(self._a, other._a), max(self._b, other._b))
        else:
            return [Interval(self._a, self._b), Interval(other._a,other._b)]

a = Interval(1,3) 
b = Interval(2,4) 
c = Interval(5,10) 
d = Interval(2,3)+Interval(1,2) 
print(a + b)  
print(b+c)
print(d)