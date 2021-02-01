def get_power_of3(n):
    '''
    Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40. In other words, using the set above and the addition and subtraction operations, construct any integer between 1 and 40 without re-using elements. For example, 4 = 1+1+1+1 is not acceptable.
    '''
    assert (isinstance(n,int))
    assert (n>=1)
    assert (n<=40)
    import itertools
    
    Result = [0,0,0,0]
    weights = [1,3,9,27]
    if n==weights[3]:
        Result[3]=1
        print(Result)
        return Result
    elif n==weights[2]:
        Result[2]=1
        print(Result)
        return Result
    elif n==weights[1]:
        Result[1]=1
        print(Result)
        return Result
    elif n==weights[0]:
        Result[0]=1
        print(Result)
        return Result
    else:
        if n>=(27-9-3-1):
            Result[3]=1
            for temp_list in list(itertools.product([-1,0,1],repeat=3)):
                Result[2] = temp_list[2] 
                Result[1] = temp_list[1]
                Result[0] = temp_list[0]
                n_calc = 27 * Result[3] + 9 * Result[2] + 3 * Result[1] + 1 * Result[0]
                if n_calc == n:
                    print(Result)
                    return Result
        elif n>=(9-3-1):
            Result[2]=1
            for temp_list in list(itertools.product([-1,0,1],repeat=3)):
                Result[3] = temp_list[2]
                Result[1] = temp_list[1]
                Result[0] = temp_list[0]
                n_calc = 27 * Result[3] + 9 * Result[2] + 3 * Result[1] + 1 * Result[0]
                if n_calc == n:
                    print(Result)
                    return Result
        else:
            Result[1]=1
            for temp_list in list(itertools.product([-1,0,1],repeat=3)):
                Result[3] = temp_list[2] 
                Result[2] = temp_list[1]
                Result[0] = temp_list[0]
                n_calc = 27 * Result[3] + 9 * Result[2] + 3 * Result[1] + 1 * Result[0]
                if n_calc == n:
                    print(Result)
                    return Result

        
