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

p={'000': 0.125, '001': 0.125, '010': 0.125, '011': 0.125, '100': 0.125, '101': 0.125, '110': 0.125, '111': 0.125}
print(get_sample(nbits=3,prob=p,n=4))
