from time import sleep
import random
from datetime import datetime
import itertools as it
import types

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(p,limit=3):
    '''
    The last line is interesting because is shows that the producer's seconds value output was an even number for the first six iterations. Your tracker generator should also receive input that changes the existing limit,

    >>> t = tracker(p,limit=3)
    >>> next(t)
    0
    >>> next(t)
    0
    >>> t.send(5)
    1
    >>> list(t)
    [1, 1, 1, 1, 2, 3, 4, 5]
    '''

    assert isinstance(p, types.GeneratorType)
    assert isinstance(limit, int)
    assert limit > 0

    counter = 0

    while(counter < limit):

        n = next(p)

        
        if int(n.seconds) % 2 !=0: #convert to int and judge
            counter += 1

        new_limit = yield(counter)
        
        if new_limit is not None:
            limit = new_limit


# p = producer()
# t = tracker(p,limit=3)
# next(t)
# next(t)
# # print(next(t))
# # print(next(t))
# print(t.send(5))
# print(list(t))
