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

x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
print(map_bitstring(x))
