def write_columns(data,fname):
    '''
    This function can write the following formula to three columns to a comma-separated file:
    '''
    
    assert (isinstance(data, list))
    assert (isinstance(fname, str))
    assert len(fname)>0
    assert len(data)>0
    for i in data:
        assert(isinstance(i, int) or isinstance(i, float))

    f = open(fname,'w')
#    open the file
    for i in data:
#        formulas
        data_1 = i*1.0
        data_2 = i**2*1.0
        data_3 = (data_1+data_2)/3.0
        f.write('%.2f,%.2f,%.2f\n' % (data_1,data_2,data_3))
    f.close()
    return 0
