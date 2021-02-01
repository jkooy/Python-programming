def write_chunks_of_five(words,fname):
    '''
    Using corpus of 10,000 common English words, create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line. Here are the first 10 lines of ouptut corresponding to the above sample corpus:
    '''
    
    assert (isinstance(words, list))
    assert (isinstance(fname, str))
    assert len(fname)>0
    assert len(words)>0
    for i in words:
        assert(isinstance(i, str))
        assert (not i.replace('.','',1).isdigit())
        assert (i.isalnum())
#    assert the words input

    f = open(fname,'w')
    temp = 1
    for i in words:
        if (temp % 5 == 0):
#        if there are 5
            f.write(i+'\n')
        elif (temp == len(words)):
#        if the length equal to the words length
            f.write(i)
        else:
            f.write(i+' ')
#        create the new file and write in
        temp += 1
    f.close()
    return 0
