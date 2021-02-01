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


def threshold_values(seq,threshold=1):
    '''
    Note that 01 corresponding value was set to 0 because it did not have the top two most frequent values of 1. If there is a tie, then use the smallest value the tied bitstrings to pick the winner. Here is a more detailed example:
    seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '
    1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', 
    '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001'] 
    '''

    import collections 
    assert(isinstance(seq, list))
    assert(isinstance(threshold, int))
    for i in seq:
        assert(isinstance(i, str))
    assert(threshold>0)
    assert(threshold<(2**len(seq[1])))

    G = gather_values(seq)

    # for key, value in G.item():
    for key, value in G.items():
        G[key] = sum(value)

    count = collections.Counter(G)

    # commont = []
    commond = {}
    for c in count.most_common(threshold):
        commond[c[0]] = 1

    for key, value in G.items():
        if key not in commond.keys():
            G[key] = 0
        elif key in commond.keys():
            G[key] = 1
    
    # d = G.items().sort()
    # d = sorted(G)
    d = dict(sorted(G.items(), key=lambda d:d[0]))
    return d
         

seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001'] 
 
print(threshold_values(seq,3) )
#  {'0000': 0, '0001': 0, '0010': 0, '0011': 1, '0100': 0, '0101': 1, '0110': 0, '0111': 0, '1000': 0, '1001': 0, '1010': 1, '1011': 0, '1100': 0, '1101': 0, '1110': 0, '1111': 0} 
