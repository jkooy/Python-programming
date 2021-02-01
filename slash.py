def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    a function that can produce a uniformly 
    random forward or backslashed image (i.e., Numpy array) of at
     least two non-zero pixels. Here is some code that generates the following figure.
    '''
    assert isinstance(m, int)
    assert m >= 2   #at least two non-zero pixels
    assert isinstance(n, int)
    assert n >=2  # at least two non-zero pixels
    assert isinstance(direction, str) 
    assert direction == 'back' or direction == 'forward'
    

    import numpy as np
    import random
    # from matplotlib.pylab import subplots, cm 

    M = np.zeros((m,n))
    if m >= n:
        max = n
    else:
        max = m
    # maximum size


    leng = random.randint(2,max)
    diag = np.eye(leng)
        
    if direction == 'forward':
        diag = np.fliplr(diag)

    if m == leng:
        m_start = 0
    else: 
        m_start = random.randint(0, m - leng)

    if n == leng:
        n_start = 0
    else:
        n_start = random.randint(0,n - leng)

    M[m_start:(m_start + diag.shape[0]), n_start:(n_start+diag.shape[1])] += diag
    return M

print(gen_rand_slash(m=6,n=6,direction='back'))
# print(get_sample(nbits=3,prob=p,n=4))

# from matplotlib.pylab import subplots
# from matplotlib.pylab import subplots, cm 
# fig,axs=subplots(3,3,sharex=True,sharey=True)
# for ax in axs.flatten():
#     print(gen_rand_slash(m=6,n=6,direction='back'))
#     ax.imshow(gen_rand_slash(),cmap=cm.gray_r)
