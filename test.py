def str(a):
    if len(a)>2:
        if a[-3:] != 'ing':
            a = a + 'ing'
        else:
            a = a + 'ly'
    return a

a = input('enter string:')
result = str(a)
print(result)

