import collections
import string
import re
import random
def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
    
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    messager = message.replace(' ', "")
    assert messager.isalpha()
    assert message.islower()     # `message` is a lowercase string without any punctuation
    assert isinstance(fname, str)
    with open(fname,'r') as f:
        fread = f.readlines()

    # print(fread)

    fpost =  [re.sub('[%s]'%string.punctuation and '\n','',l) for l in fread]  # Strip out all of the punctuation and make everything lowercase.

    # print('fpost', fpost)

    
    vocab = collections.defaultdict(list)
    for i,m in enumerate(fpost):
        for j,w in enumerate(m.split()):
          vocab[w].append((i, j))

    messageo = [re.sub('[%s]'%string.punctuation and '\n','',l) for l in message]
    # message = ''.join([re.sub('[%s]'%string.punctuation and '\n','',l) for l in message])

    # print(message)

    for k, v in vocab.items():
        random.shuffle(v)

    # count = {}
    count = collections.defaultdict(int)
    for msg in messageo:
        # if msg not in count:
        #     count[msg] = 1
        # else:
        #     count[msg] += 1
        count[msg] += 1
    
    
    print(count)

    for i in count:
        assert count[i] <= len(vocab), 'In case of repeated words, you should have a randomized scheme to ensure that no message contains the same 2-tuple, even if the same word appears multiple times in the message. If there is only one occurrence of a word in the text and the message uses that word repeatedly so that each occurrence of the word cannot have a unique 2-tuple, then the message should be rejected (i.e., assert against this).'

    word = message.split()
    vocabL = []
    for msg in word:
        assert msg in vocab.keys()    #assert every word in the vocab
        vocabL.append(vocab[msg].pop())
    
    return vocabL



def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
    
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''

    assert isinstance(inlist, list)
    assert(isinstance(fname,str))
    assert len(inlist) > 0
    
    with open(fname,'r') as f:
        fread = f.readlines()

    message = ''
    for i in inlist:
        assert isinstance(i, tuple)
        assert len(i) == 2
        (index, content) = i
        l = fread[index].split()  #get the line with the index
        message +=  str(l[content]) + ' '
    
    return message.strip()


# test = "let us not say we met late at the night about the secret"
# em = encrypt_message(test,'pg5200.txt')
# decrypt = decrypt_message(em, 'pg5200.txt')
# print(em)
# print(decrypt)
# print(test == decrypt)