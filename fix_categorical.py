import itertools as iter
import itertools as it
import numpy as np
def get_min_split(seq):
    '''
    Given an array of unique positive integers, divide the array into two subsets such that
    the absolute difference between the respective sums of the subsets is as small as possible.
    '''
    assert isinstance(seq, list) or (isinstance(seq, np.ndarray) and seq.ndim == 1)
    assert (isinstance(i, int) for i in seq)
    assert len(seq) == len(set(seq))
    half = sum(seq) / 2
    combine = []
    subtract = []
    outlist = []
    for r in range(1, len(seq)+1):
        mid = list(iter.combinations(seq, r))
        for miditem in mid:
            combine.append(miditem)
            subtract.append(abs(sum(miditem)-half))
    length = len(seq)
    for i, x in enumerate(combine):
        if subtract[i] == min(subtract):
            if length > len(x):
                length = len(x)
    for i, x in enumerate(combine):
        if subtract[i] == min(subtract) and len(x) == length:
            outlist.append( ( sorted(list(x)),sorted(list(set(seq)-set(x) )) ) )
    return outlist


def get_min_split2(seq):
    '''
    Given an array of unique positive integers, this function divides the array into two subsets 
    such that the absolute difference between the respective sums of the subsets is as small as possible.
    '''
    # import random
    assert isinstance(seq, list) or isinstance(seq,(np.ndarray))
    assert [isinstance(i, int) for i in seq]
    assert [i > 0  for i in seq]
    if isinstance(seq, np.ndarray):
        assert(seq.ndim==1),'must be a 1D numpy array'
    setS = set(seq) #unique positive integers
    assert len(seq) > 2 or len(seq) == 2 #two subsets
    assert len(setS) == len(seq)
    
    Dict = {}
    i = 0
    while i <= (int(len(seq) / 2)):
        for key in it.combinations(seq, i):
            Dict[key] = abs(sum(seq) - 2*sum(key))
        i += 1
    mind = min([Dict[d] for d in Dict])
    # print(Dict)
    # for d in Dict.keys():
    #     if Dict[d] == mind:
    #         print(list(d))
    #         print(list(set(seq)- set(d)))
    #         print('true')

    return [(sorted(list(d)), sorted(list(set(seq)- set(d)))) for d in Dict.keys() if Dict[d] == mind]


seq = [20, 25, 5, 10, 15, 45, 22, 23, 46]
#seq = [5, 10, 15, 20, 25]
print(get_min_split(seq) == get_min_split2(seq))
print(get_min_split2(seq))
print(get_min_split(seq))