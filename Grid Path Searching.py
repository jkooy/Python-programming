def count_paths(m,n,blocks):
    '''
    This functiom starts at the upper left and only moving downwards and rightwards, find the number of connected paths between the top-left square and the bottom right square by traversing only the intermediate squares with the . symbol. The start and end positions are never be marked with #
    '''
    assert m>0
    assert n>0
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(blocks, list)
    # assert all((all(isinstance(j, int) for j in i) and isinstance(i,tuple)) for i in blocks)

    
    def path(m0,n0,blocks):
    # recursive
        if (m0, n0) in blocks:
            return 0
        elif (m0, n0) == (0,1) or (m0, n0) == (1, 0):
            return 1
        elif m0 > 0 and n0 > 0:        
            return path(m0-1, n0, blocks) + path(m0, n0-1, blocks)
        elif m0 > 0 and n0 == 0:
            return path(m0-1, n0, blocks)
        elif m0 == 0 and n0 > 0:
            return path(m0, n0-1, blocks)

    return path(m-1, n-1, blocks)

# result = count_paths(3,4,[(0,3),(1,1)])
# print(result)
