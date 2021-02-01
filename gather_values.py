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


def gather_values(bitstrings):
    '''
    A function that can produce the following output from x:

    {'10': [1, 1, 1, 1, 1],
    '11': [1, 1, 1, 1, 1, 1],        
    '01': [1, 1, 1],                 
    '00': [0, 0, 0, 0, 0, 0]}        
    '''
    import collections

    assert(isinstance(bitstrings, list))
    for sstr in bitstrings:
        assert isinstance(sstr, str)

    map = map_bitstring(bitstrings)

    outputD = {}
    
    for index, sstr in enumerate(bitstrings):
        n0 = n1 = 0
        k = bitstrings[index]

        
        
        for i in k:
            if int(i) == 0:
                n0 += 1
            elif i !=0:
                n1 +=1
        if n0 > n1:
            if k not in outputD.keys():
                # judge whether key exists
                outputD[k] = [] 
            outputD[k].append(0)
        if n0 <= n1:
            if k not in outputD.keys():
                # judge whether key exists
                outputD[k] = [] 
            outputD[k].append(1)


    return outputD


x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
print(gather_values(x))
