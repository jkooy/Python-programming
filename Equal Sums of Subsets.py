import numpy as np
import itertools as it
def get_min_split(seq):
    '''
    Given an array of unique positive integers, this function divides the array into two subsets 
    such that the absolute difference between the respective sums of the subsets is as small as possible.
    '''
    # import random
    assert isinstance(seq, list) or isinstance(seq,(np.ndarray))
    # assert [isinstance(i, int) for i in seq]
    # assert [i > 0  for i in seq]
    assert (isinstance(i, int) for i in seq)
    if isinstance(seq, np.ndarray):
        assert(seq.ndim==1),'must be a 1D numpy array'
    setS = set(seq) #unique positive integers
    assert(len(seq)>1)
    # assert len(seq) > 2 or len(seq) == 2 #two subsets
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

# seq = np.array([5, 10, 15, 20, 25])
# seq = [5, 10, 15, 20, 25]
# seq = [20, 25, 5, 10, 15]
# # seq = np.array([5, 10, 15, 20, 45, 25])
# print(get_min_split(seq))
