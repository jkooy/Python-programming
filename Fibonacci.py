def fibonacci(n):
    '''
    The Fibonacci numbers are defined by the following recursion: 
    F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1. Write a 
    generator to compute the first n Fibonacci numbers. For example, 
    for n=10, the output for list(fibonacci(n)) should be 
    [1,1,2,3,5,8,13,21,34,55].
    '''
    
    assert (isinstance(n, int))
    assert (n>0)
    
    f1 = 1
    f2 = 1
    m = 1
    while m<=n:
        yield f1
        # use yield to swap and generate the next one
        f1, f2 = f2, f1+f2
        m += 1
    return 0