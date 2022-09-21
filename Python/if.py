x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative number changed to zero')
elif x == 0:            # no switch or case in Python
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')