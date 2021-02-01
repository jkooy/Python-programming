import math
import numbers

class Polynomial(object):
    '''
    Create a Python class that can implement a univariate 
    polynomial with degree at least one (Polynomial) over the 
    field of integers (only!) with the following operations and interfaces.
    '''

    def __init__(self, input_dict = None ):
        assert isinstance(input_dict, dict)
        for i, value in input_dict.items():
            assert isinstance(i, int)
            assert isinstance(value, int)

        self.sdict = input_dict

    def __repr__(self):
        smax = max(self.sdict.keys())
        smin = min(self.sdict.keys())
        slist = []

        if smin < 0:
            for i in range(smin, smax+1):
                if i in self.sdict:
                    slist.append(self.sdict[i])
                else:
                    slist.append(0)

        if smin >= 0:
            for i in range(smax + 1):
                if i in self.sdict:
                    slist.append(self.sdict[i])
                else:
                    slist.append(0)

        returnList = []
        for i, n in enumerate(slist):
            if n !=0:
                if i == 0:
                    returnList += str(n).strip()
                elif i == 1:
                    if n == 1:
                        returnList += ' + ' + 'x'
                    else:
                        returnList += ' + ' + str(n) + ' x'
                else:
                    if n == 1:
                        returnList += ' + ' + 'x^' + '(' + str(i) + ')'
                    else:
                        returnList += ' + ' + str(n) + ' x^' + '(' + str(i) + ')'

        return str(''.join(returnList))
        # return  str(''.join([str(n).strip() if i ==0 else ' + ' + str(n) + ' x^' + str(i) (if n != 0) for i, n in enumerate(slist)])).strip()


    def __add__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)
        mydict = {}
        for key in list(self.sdict.keys()):
            mydict[key] = self.sdict[key]

        if isinstance(other, int):
            if 0 in self.sdict.keys():
                mydict[0] = other + self.sdict[0]
            else:
                mydict[0] = other

        else:
            for key in list(mydict.keys()):
                for key1 in list(other.sdict.keys()):
                    if key == key1:
                        mydict[key] = self.sdict[key] + other.sdict[key]
                    elif key1 not in mydict.keys():
                        mydict[key1] = other.sdict[key1]

        keys = mydict.keys()
        for key in list(keys):
            if mydict[key] == 0:
                mydict.pop(key, None)

        return Polynomial(mydict)


    def __sub__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        mydict = {}
        for key in list(self.sdict.keys()):
            mydict[key] = self.sdict[key]

        if isinstance(other, int):
            if 0 in mydict.keys():
                mydict[0] = self.sdict[0] - other
            else:
                mydict[0] = other

        else:
            for key in list(mydict.keys()):
                for key1 in list(other.sdict.keys()):
                    if key == key1:
                        mydict[key] = self.sdict[key] - other.sdict[key]
                    elif key1 not in mydict.keys():
                        mydict[key1] = -other.sdict[key1]

        keys = mydict.keys()
        for key in list(keys):
            if mydict[key] == 0:
                mydict.pop(key, None)

        return Polynomial(mydict)


    def __rsub__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)
        mydict = {}

        for index, value in self.sdict.items():
            mydict[index] = -value

        new = Polynomial(mydict)
        other = -other
        return new.__sub__(other)


    def __mul__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        mydict = {}

        # integer multiplication
        if isinstance(other, int):
            for key in self.sdict.keys():
                mydict[key] = self.sdict[key] * other

        # polynomial multiplication
        else:
            for key in list(self.sdict.keys()):
                for key1 in list(other.sdict.keys()):
                    mult = self.sdict[key] * other.sdict[key1]
                    mult_degree = key + key1
                    # check if degree already in store
                    degree_list = list(mydict.keys())
                    if mult_degree in degree_list:
                        mydict[mult_degree] = mydict[mult_degree] + mult
                    else:
                        mydict[mult_degree] = mult

        return Polynomial(mydict)

    def __rmul__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        return self.__mul__(other)


    def __eq__(self, other):
        # judge whether equal
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        # check integer
        if (isinstance(other, int)):
            temp = self.sdict
            value = 0
            for index, values in temp.items():
                value = values
            return value == 0

        if self.sdict == other.sdict:
            return True
        return False

    def __truediv__(self, other):
        # check appropriate types
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        max_key_num = []
        max_key_dom = []
        output = {}
        temp = {}
        num = self.sdict
        dom = other.sdict
        i = 0
        n = 0
        ev = 0

        while n == 0:
            # q/p
            for key in num:
                max_key_num.append(key)
            for key in dom:
                max_key_dom.append(key)

            # find degree of denom and num
            if len(max_key_num) == 0:
                b = 0
            else:
                b = max(max_key_num)

            if len(max_key_dom) == 0:
                a = 0
            else:
                a = max(max_key_dom)

            # if divior has bigger degree than dividend, error
            if (a > b):
                n = 1
                raise NotImplementedError

            c = b - a  # getting the difference

            b = num[b]
            a = dom[a]
            d = math.gcd(a, b)

            if (d == 1):
                d = b
                ev = 1
            elif (d != 1 and ev == 0 and b == a):
                d = 1
            else:
                d = int(b / a)

            temp[c] = d
            output.update(temp)

            div = Polynomial(temp)
            temp_dom = Polynomial(dom)

            output1 = temp_dom.__mul__(div)
            temp_num = Polynomial(num)

            f = temp_num.__sub__(output1)
            max_key_num = []

            tempp = f.sdict
            for key in tempp:
                max_key_num.append(key)

            if len(max_key_num) == 0:
                b = 0
            else:
                b = max(max_key_num)

            if len(tempp) == 0:
                remainder = 0
            else:
                remainder = tempp[b]

            if (remainder != 0 and b == 0):
                raise NotImplementedError

            if (b == 0):
                new = Polynomial(output)
                n = 1
                return new

            if (b < a):
                n = 1
                raise NotImplementedError

            num = f.sdict

            i = i + 1
            max_key_num.clear()
            temp = {}
            ev = 0

    def subs(self, sub_int):
        total = 0
        for key in list(self.sdict.keys()):
            mult = (sub_int ** key) * self.sdict[key]
            total = total + mult

        return total

p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
q=Polynomial({0:8,1:2,2:8,4:4})
print(repr(p))
print(p*3) # integer multiply)
print(3*p)
print(p+q)
print(p*4 + 5 - 3*p - 1)
print(type(p-p))
print(p*q)
print(p.subs(10))
print((p-p) == 0)
print(p == q)
p=Polynomial({0:8,1:0,3:4})
print(repr(p))
p = Polynomial({2:1,0:-1})
q = Polynomial({1:1,0:-1})
print(p/q)
print(p  / Polynomial({1:1,0:-3}))

