def get_sample(nbits=3, prob=None, n=1):
    '''
    Given a number of bits, write the get_sample function 
    to return a list n of random samples from a finite probability mass 
    function defined by a dictionary with keys defined by a specified number of bits.
     For example, given 3 bits, we have the following dictionary that defines the probability of 
     each of the keys. The values of the dictionary correspond of the probability of drawing any one of these. 
     For example, if all of these were equally likely, then here is the corresponding dictionary p
    '''
    import random
    assert isinstance(nbits, int)
    assert isinstance(n, int)
    assert isinstance(prob, dict)
    assert (nbits>0)
    assert (n>0)
    assert (len(prob) == 2**nbits)
    assert (len(y) == nbits for y in prob.keys())
    assert (sum([value for key,value in prob.items()])==1)
    
    return_samples = random.sample(list(prob),n)
    return return_samples
    
def map_bitstring(bitstrings):
    '''
    Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps 
    each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. 
    Otherwise, map that bitstring to 1. The output of your function is a dictionary of the 
    so-described key-value pairs.
    '''
    assert isinstance(bitstrings, list)
    assert len(bitstrings)>0

    for sstr in bitstrings:
        assert isinstance(sstr, str)

    newBitstring = {}

    for sstr in bitstrings:
        if sstr.count('1') > sstr.count('0'):
            newBitstring[sstr] = 1
        elif sstr.count('1') <= sstr.count('0'):
            newBitstring[sstr] = 0
    return newBitstring


def gather_values(bitstring):
    assert(isinstance(bitstring,list)), 'the input should be of type list'
    
    d = dict()
    for i in range(len(bitstring)):
        key = bitstring[i]
        num_0 = 0
        num_1 = 0
        if key not in d.keys():
            d[key] = list()
        for j in key:
            if int(j)==0:
                num_0 += 1
            else:
                num_1 += 1
        if num_0>num_1:
            d[key].append(0)
        else:
            d[key].append(1)
    return d


x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']

print(gather_values(x))