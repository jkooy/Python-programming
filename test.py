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
    
    water = []
    water = 0
    for i, value in enumerate(seq[1:]):
        c = i
        vwall = seq[0]
        d_max = seq[c]
        while d_max < value:
            c -= 1
            water += min(value, vwall) - d_max
            # water.append(min(value, vwall) - d_max)
            d_max = max(d_max, seq[c])
            if d_max == vwall:
                break
        vwall = max(vwall, value)
    # return sum(water)
    return water

    
def get_trapped_water(seq):
    '''
    :param seq: input, list
    :return: int
    '''
    assert isinstance(seq,list)
    n=len(seq)
    # left[i] contains height of tallest bar to the left of i th bar including itself
    left_bar = seq[:]
    right_bar = seq[:]
    trap_water = 0
    for i in range(1, n):
        left_bar[i] = max(left_bar[i - 1], seq[i])    
    for i in range(n-2, -1, -1):
        right_bar[i] = max(right_bar[i + 1], seq[i])
    for i in range(1, n):
        trap_water += min(left_bar[i], right_bar[i]) - seq[i]
    return trap_water

seq = [2, 1, 1, 4, 1, 2]
print(get_trapped_water(seq))
seq = [5, 1, 1, 1, 1, 4]
print(get_trapped_water(seq))
seq = [2, 1, 2]
print(get_trapped_water(seq))
seq = [3, 0, 1, 3, 0, 5]
print(get_trapped_water(seq))
