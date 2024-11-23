
def reverse_number(x:int)->int:
    if x < -(2**31) or x > 2**31 - 1: # check
        return 0
    else:
        if x>0:
            reversed_x = int(str(x)[::-1])  # reverses a positive number
        else:
            reversed_x = -int(str(abs(x))[::-1]) # reverses a negative number
        if reversed_x < -(2**31) or reversed_x > 2**31 - 1:  # check
            return 0
        return reversed_x

print(reverse_number(int(input())))