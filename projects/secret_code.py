import random
import string

def g_alpha(length):
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return a

def rev(x):
    return g_alpha(3) + x[-1::-1] + g_alpha(3)

def code(y):
    first_element = y[0]
    y = g_alpha(3) + y[1:] + first_element + g_alpha(3)
    return y

def decode(z):
    last_element = z[-4]
    z = last_element + z[3:-4]  
    return z

c = input('code\\decode:')
b = input('enter strings:')
words = b.split(' ')

if c == 'code':
    nword = []
    for b in words:
        if len(b) < 3:
            m = rev(b)
            nword.append(m)
        else:
            m = code(b)
            nword.append(m)
    print(' '.join(nword))
else:
    nword = []
    for b in words:
        if len(b) < 3:
            m = rev(b)
            nword.append(m)
        else:
            m = decode(b)
            nword.append(m)
    print(' '.join(nword))
