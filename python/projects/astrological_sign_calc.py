#astrological sign 

def cal(a,b):
    if b == 'december':
        sign = 'sagittarius' if a < 22 else 'capricorn'
    elif b == 'january':
        sign = 'capricorn' if a < 20 else 'aquarius'
    elif b == 'february':
        sign = 'aquarius' if a < 19 else 'pisces'
    elif b == 'march':
        sign = 'pisces' if a < 21 else 'aries'
    elif b == 'april':
        sign = 'aries' if a < 20 else 'taurus'
    elif b == 'may':
        sign = 'taurus' if a < 21 else 'gemini'
    elif b == 'june':
        sign = 'gemini' if a < 21 else 'cancer'
    elif b == 'july':
        sign = 'cancer' if a < 23 else 'leo'
    elif b == 'august':
        sign = 'leo' if a < 23 else 'virgo'
    elif b == 'september':
        sign = 'virgo' if a < 23 else 'libra'
    elif b == 'october':
        sign = 'libra' if a < 23 else 'scorpio'
    elif b == 'november':
        sign = 'scorpio' if a < 22 else 'sagittarius'
    else:
        print('invalid!!')
    return sign

a = int(input('enter date:'))
b = str(input('enter month:'))

cal(a,b)