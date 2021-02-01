import itertools as it

def next_permutation(t:tuple)->tuple:
    '''
    Given a permutation of any length, generate the next permutation in 
    lexicographic order. For example, this are the permutations for [1,2,3] 
    in lexicographic order.
    '''
    # assert isinstance(t, tuple)
    # assert (isinstance(i, int) for i in t)
    assert type(t) == tuple
    for i in range(len(t)):
        assert type(t[i]) == int
    assert len(set(t)) == len(t)

    t = list(t)
    for i in range(len(t)-1, -1, -1):   
        # The last permutation should wrap aruond to the first.     
        if t[i-1] < t[i]:
            break

    if i != 0:
        for j in range(len(t)-1, -1, -1):
            if t[j]>t[i-1]:
                break 
        t[i-1], t[j]= t[j], t[i-1]
    t[i:]=reversed(t[i:])
    return tuple(t)

# print(list(it.permutations([1,2,3])))
# print(next_permutation((2,3,1)))
# print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))
# print(next_permutation((3,2,1,0)))