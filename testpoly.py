import math


class Polynomial(object):
    '''
    Class to solve polynomial problem
    '''

    def __init__(self, the_dict=None):
        # check that what is passed in is a dictionary
        assert isinstance(the_dict, dict)
        # check that values are type int
        for index, value in the_dict.items():
            assert isinstance(index, int)
            assert isinstance(value, int)

        self.the_dict = the_dict

    def __repr__(self):
        eq_str = ''
        had_prev = False

        # sort the dictionary
        dict_items = self.the_dict.items()
        sorted_items = sorted(dict_items)

        for key in range(len(sorted_items)):
            if sorted_items[key][0] == 0:
                eq_str = eq_str + str(sorted_items[key][1]) + ' '
                had_prev = True
                if sorted_items[key][1] == 0:
                    eq_str = ''
                    had_prev = False
            elif sorted_items[key][0] == 1:
                if sorted_items[key][1] != 0:
                    if had_prev:
                        eq_str = eq_str + '+ '
                    if sorted_items[key][1] != 1:
                        eq_str = eq_str + str(sorted_items[key][1]) + ' '
                    eq_str = eq_str + 'x '
                    had_prev = True
            else:
                if sorted_items[key][1] != 0:
                    if had_prev:
                        eq_str = eq_str + '+ '
                    eq_str = eq_str + str(sorted_items[key][1]) + ' x^(' + str(sorted_items[key][0]) + ') '
                    had_prev = True
        eq_str = eq_str.strip()

        return eq_str

    def __mul__(self, other):
        # check appropriate types
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        new_dict = {}

        # integer multiplication
        if isinstance(other, int):
            for key in self.the_dict.keys():
                new_dict[key] = self.the_dict[key] * other

        # polynomial multiplication
        else:
            for key in list(self.the_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    mult = self.the_dict[key] * other.the_dict[key1]
                    mult_degree = key + key1
                    # check if degree already in store
                    degree_list = list(new_dict.keys())
                    if mult_degree in degree_list:
                        new_dict[mult_degree] = new_dict[mult_degree] + mult
                    else:
                        new_dict[mult_degree] = mult

        return Polynomial(new_dict)

    def __rmul__(self, other):
        # check appropriate types
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        return self.__mul__(other)

    def __add__(self, other):
        '''Method to add a polynomial and another or a polynomial and an int'''
        new_dict = {}
        # populate new dict with self values
        for key in list(self.the_dict.keys()):
            new_dict[key] = self.the_dict[key]

        # adding an integer
        if isinstance(other, int):
            if 0 in self.the_dict.keys():
                new_dict[0] = other + self.the_dict[0]
            else:
                new_dict[0] = other

        # adding a polynomial
        else:
            for key in list(new_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        new_dict[key] = self.the_dict[key] + other.the_dict[key]
                    elif key1 not in new_dict.keys():
                        new_dict[key1] = other.the_dict[key1]

        # remove any zeroes from dictionary
        keys = new_dict.keys()
        for key in list(keys):
            if new_dict[key] == 0:
                new_dict.pop(key, None)

        return Polynomial(new_dict)

    def __sub__(self, other):
        # check appropriate values
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        new_dict = {}
        # populate new dict with self values
        for key in list(self.the_dict.keys()):
            new_dict[key] = self.the_dict[key]

        # subtracting integer
        if isinstance(other, int):
            if 0 in new_dict.keys():
                new_dict[0] = self.the_dict[0] - other
            else:
                new_dict[0] = other

        # subtracting a polynomial
        else:
            for key in list(new_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        new_dict[key] = self.the_dict[key] - other.the_dict[key]
                    elif key1 not in new_dict.keys():
                        new_dict[key1] = -other.the_dict[key1]

        # remove any zeroes from dictionary
        keys = new_dict.keys()
        for key in list(keys):
            if new_dict[key] == 0:
                new_dict.pop(key, None)

        return Polynomial(new_dict)

    def __rsub__(self, other):
        # check appropriate types
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)
        new_dict = {}

        for index, value in self.the_dict.items():
            new_dict[index] = -value

        new = Polynomial(new_dict)
        other = -other
        return new.__sub__(other)

    def __eq__(self, other):
        ''' Check if polynomials are equal to each other or equal to 0'''

        # check appropriate types
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        # check integer
        if (isinstance(other, int)):
            temp = self.the_dict
            value = 0
            for index, values in temp.items():
                value = values
            return value == 0

        if self.the_dict == other.the_dict:
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
        num = self.the_dict
        dom = other.the_dict
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

            tempp = f.the_dict
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

            num = f.the_dict

            i = i + 1
            max_key_num.clear()
            temp = {}
            ev = 0

    def subs(self, sub_int):
        total = 0
        for key in list(self.the_dict.keys()):
            mult = (sub_int ** key) * self.the_dict[key]
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