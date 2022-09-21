a, b = 0, 1
while a < 1000: # 0 and empty sequences are false. < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to)
    print(a, end=',') # end replaces the standard newline output of print() with a custom string
    a, b = b, a+b  # expressions calculated before assignment