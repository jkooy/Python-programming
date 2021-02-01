import random
import os

def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''

    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert n > 0
    assert n < 1000   # n is 000, 001, ..., 999
    


    with open(fname, 'r') as fread:
        lines = fread.readlines()
        #read lines

    length = os.stat(fname).st_size
    #get size of the file
    ave = length/n

    stack = []
    ll = []
    lenstack = 0
    count = 0

    for i, line in enumerate(lines):
        if lenstack <= ave:
            lenstack += len(line)
            stack.append(i)
        else:
            ll.append(stack.pop())
            count += 1
            # last line is the division
            lenstack = len(lines[i-1]) + len(line)
            if n <= len(ll):
                break

    ll.append(len(lines)) 

    print(ll)
    print(lenstack)
    
    ll0 = [0] + ll
    for i, y in enumerate(ll):
        with open(fname + '_' + str(i).zfill(3) + '.txt', 'wt') as fwrite:
            for l in (lines[ll0[i]:ll0[i+1]]):
                fwrite.write(str(l))
                if i == len(ll):
                    break


            # if i == 0:
            #     fwrite.write(str(lines[0:ll[i]]))
            # else:
            #     print(i)
            #     if i+1 == len(ll):
            #             break
            #     else:
            #         for l in (lines[ll[i]:ll[i+1]]):
            #             fwrite.write(str(l))
                    

# split_by_n("pg5200.txt",n=3)
