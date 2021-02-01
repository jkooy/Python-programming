def get_trapped_water(seq):
    '''
    given an array of non-negative integers that represents a two-dimensional elevation map 
    where each element is unit-width wall and the integer value is the height. Suppose rain 
    fills all available gaps between two bordering walls.
    Compute how many units of water remain trapped between the walls in the map.
    For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
    Here's another example for the sequence [3, 0, 1, 3, 0, 5] where the answer is 8,
    '''
    assert isinstance(seq, list)
    # assert (isinstance(i,int) for i in seq)
    # assert (i>=0 for i in seq)

    water = 0
    Seq = len(seq)

    for i in range(1, Seq - 1):
        maxLeft = seq[i]
        maxRight = maxLeft 

        for j in range(i):
            maxLeft = max( maxLeft, seq[j] )

        for k in range(i + 1, Seq):
            maxRight = max( maxRight, seq[k] )

        water += min( maxLeft, maxRight ) - seq[i]
    return water


# seq = [2, 1, 2]
# print(get_trapped_water(seq))
# seq = [3, 0, 1, 3, 0, 5]
# print(get_trapped_water(seq))
# seq = [2, 1, 1, 4, 1, 2]
# print(get_trapped_water(seq))
# # print(get_trapped_water(seq) == (get_trapped_water2(seq)))
# seq = [5, 1, 1, 1, 1, 4]
# print(get_trapped_water(seq))
# # print(get_trapped_water(seq) == (get_trapped_water2(seq)))
# seq = [1, 1, 1, 1, 1, 1]
# print(get_trapped_water(seq))
# # print(get_trapped_water(seq) == (get_trapped_water2(seq)))
# seq = [0, 0, 0, 0, 0, 0]
# print(get_trapped_water(seq))
# # print(get_trapped_water(seq) == (get_trapped_water2(seq)))
# seq = [6, 4, 2, 3, 5, 7]
# print(get_trapped_water(seq))
# # print(get_trapped_water(seq) == (get_trapped_water2(seq)))