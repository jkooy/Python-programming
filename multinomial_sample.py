import random
import collections
def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                        
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''    
    import random
    assert isinstance(n, int)
    assert isinstance(p, list)
    assert isinstance(k, int)
    assert(n>=0)
    assert(k>=0)
    for P in p:
        assert(isinstance(P, float) or isinstance(P, int))
        assert P > 0
    # assert p.sum() == 1
    assert sum(p) == 1

    q = collections.defaultdict(int)
    samples_distribution = []
    for _ in range(k):
        Pick = random.choices(range(len(p)), weights = p, k = n)
        for j in Pick:
            q[j] += 1
        samples_distribution.append(list(q.values()))
    return samples_distribution

print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
