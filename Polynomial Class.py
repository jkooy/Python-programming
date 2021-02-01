import math
import numbers

class Polynomial(object):
    '''
    Create fi Python class that can implement fi univariate 
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
        for i, judge in enumerate(slist):
            if judge !=0:
                if i == 0:
                    returnList += str(judge).strip()
                elif i == 1:
                    if judge == 1:
                        returnList += ' + ' + 'x'
                    else:
                        returnList += ' + ' + str(judge) + ' x'
                else:
                    if judge == 1:
                        returnList += ' + ' + 'x^' + '(' + str(i) + ')'
                    else:
                        returnList += ' + ' + str(judge) + ' x^' + '(' + str(i) + ')'

        return str(''.join(returnList))
        # return  str(''.join([str(judge).strip() if i ==0 else ' + ' + str(judge) + ' x^' + str(i) (if judge != 0) for i, judge in enumerate(slist)])).strip()


    def __add__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)
        mydict = {}
        for key in self.sdict:
            mydict[key] = self.sdict[key]

        if isinstance(other, int):
            if 0 in self.sdict:
                mydict[0] = other + self.sdict[0]
            else:
                mydict[0] = other
        else:
            for key in list(mydict.keys()):
                for keyo in other.sdict:
                    if key == keyo:
                        mydict[key] = self.sdict[key] + other.sdict[key]
                    elif keyo not in mydict.keys():
                        mydict[keyo] = other.sdict[keyo]

        for key in mydict:
            if mydict[key] == 0:
                del mydict[key]

        return Polynomial(mydict)


    def __sub__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        mydict = {}
        for key in self.sdict:
            mydict[key] = self.sdict[key]

        if isinstance(other, int):
            if 0 in mydict:
                mydict[0] = self.sdict[0] - other
            else:
                mydict[0] = other

        else:
            for key in list(mydict.keys()):
                for keyo in other.sdict:
                    if key == keyo:
                        mydict[key] = self.sdict[key] - other.sdict[key]
                    elif keyo not in mydict.keys():
                        mydict[keyo] = -other.sdict[keyo]

        temp2 = mydict
        for key in list(temp2.keys()):
            if mydict[key] == 0:
                del mydict[key]

        return Polynomial(mydict)


    def __mul__(self, other):
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        mydict = {}

        if isinstance(other, int):
            for key in self.sdict:
                mydict[key] = self.sdict[key] * other

        else:
            for key in self.sdict:
                for keyo in other.sdict:
                    mult = self.sdict[key] * other.sdict[keyo]
                    tmult = key + keyo
                    tempdd = mydict.keys()
                    if tmult in tempdd:
                        mydict[tmult] = mydict[tmult] + mult
                    else:
                        mydict[tmult] = mult
        return Polynomial(mydict)

    def __truediv__(self, other):
        #  p/q    polynomial divided by polynomial
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        ldom = []
        output = {}
        number = self.sdict
        dom = other.sdict
        judge = 0
        while judge == 0:
            lnum = []
            temp = {}
            cov = 0
            for key in number:
                lnum.append(key)
            if len(lnum) == 0:
                se = 0
            else:
                se = max(lnum)      
            for key in dom:
                ldom.append(key)
            if len(ldom) == 0:
                fi = 0
            else:
                fi = max(ldom)
            if  fi > se:
                judge = 1
                raise NotImplementedError
            c = se - fi  
            se = number[se]
            fi = dom[fi]
            d = math.gcd(fi, se)  # find maximum common number
            if  d == 1:
                d = se
                cov = 1
            elif cov == 0 and se == fi:
                d = 1
            else:
                d = int( se / fi )
            temp[c] = d
            output[c] = d

            domomi = Polynomial(dom)
            div = Polynomial(temp)
            mulr = domomi.__mul__(div)
            temp_num = Polynomial(number)
            subr = temp_num.__sub__(mulr)
            lnum = []
            
            for key in subr.sdict.keys():
                lnum.append(key)
            if len(lnum) == 0:
                se = 0
            else:
                se = max(lnum)
            tsdict = subr.sdict
            if len(subr.sdict) == 0:
                remainder = 0
            else:
                remainder = tsdict[se]

            if (remainder != 0 and se == 0):
                # p  / Polynomial({1:1,0:-3}) # raises NotImplementedError
                raise NotImplementedError
            elif  se == 0:
                judge += 1
                return Polynomial(output)
            elif  se < fi:
                judge += 1
                raise NotImplementedError
            number = subr.sdict


    def __rmul__(self, other):
        # Exception has occurred: TypeError unsupported operand type(s) for *: 'int' and 'Polynomial'
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)
        return self.__mul__(other)

    def subs(self, sub_int):
        # substitute in integers and evaluate
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(sub_int, int)
        total = 0
        for key in self.sdict:
            total += (sub_int ** key) * self.sdict[key]
        return total

    def __eq__(self, other):
        # judge whether equal
        assert isinstance(self, Polynomial) or isinstance(self, int)
        assert isinstance(other, Polynomial) or isinstance(other, int)

        if isinstance(other, int):
            temp = self.sdict
            value = 0
            for key in self.sdict:
                value += self.sdict[key]
            return value == 0

        return self.sdict == other.sdict

# p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
# q=Polynomial({0:8,1:2,2:8,4:4})
# print(repr(p))
# print(p*3) # integer multiply)
# print(3*p)
# print(p+q)
# print(p*4 + 5 - 3*p - 1)
# print(type(p-p))
# print(p*q)
# print(p.subs(10))
# print((p-p) == 0)
# print(p == q)
# p=Polynomial({0:8,1:0,3:4})
# print(repr(p))
# p = Polynomial({2:1,0:-1})
# q = Polynomial({1:1,0:-1})
# print(p/q)
# print(p  / Polynomial({1:1,0:-3}))

