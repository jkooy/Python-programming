import numpy as np
import itertools as it
    
def solvefrob(coefs, b):
    '''
   The Frobenius equation is the Diophantine equation,
    a_1 x_1 +... + a_n x_n = b
    where a_i> 0 are positive integers, b> 0 is a positive integer, and the solution x_i consists of non-negative integers. 
    '''

    assert isinstance( coefs, list )
    # assert (isinstance( i, int ) for i in coefs)
    for i in coefs:
        assert (isinstance( i, int ))
        assert (i > 0)    # i > 0 are positive integers
    assert isinstance( b, int) and b > 0     # b> 0 is a positive integer


    comb = list(it.product(*[np.arange(b//deno+1) for deno in coefs]))
    Clist = np.where((np.array(coefs)*np.array(comb)).sum(1) == b)[0]
    
    return [comb[i] for i in Clist]

# print(solvefrob([1,2,3,5],10))
