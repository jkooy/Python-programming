def slide_window(x,width,increment):
    '''
    Implement a sliding window for an arbitrary input list. 
    The function should take the window width and the window increment as inputs and 
    should produce a sequence of overlapping lists from the input list. 
    For example, given x=list(range(15)), the following is the output given a 
    window width of 5 and window increment of 2.
    '''
    
    assert (isinstance(x, list))
    assert (isinstance(width, int))
    assert (isinstance(increment, int) or isinstance(increment, float))
    assert (width > 0 and increment > 0)
    assert (width <= len(x))
    
    olist = []
    start = 0.0
    while start <= (len(x) - width):
        start_int = int(start) + (start%1 > 0)
        olist.append(x[start_int:(start_int + int(width))])
        # judge the bouding box
        start += increment
        if start > len(x) - int(width):
            break
    return olist

# print(slide_window(list(range(18)),5, 2))