import time
samay = time.strftime('%H:%M:%S')
hrs = int(time.strftime('%H'))
if (hrs<12 and hrs>=0):
    print('good morning')
elif(hrs>=12 and hrs<5):
    print('good afternoon')
else:
    print('good night')
print(samay)
