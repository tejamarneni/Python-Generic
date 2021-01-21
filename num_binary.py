# This function gives the binary of a given positive number

def binary_of(num):
    strval = ''
    if num == 0:
        return 0
    else:    
        while num != 0:
            rem = num % 2  #captures the remainder of the number
            num = int(num/2)
            strval += str(rem) #casting the remainder as string
        strval = strval[::-1] #reversing the string
        return strval

print(binary_of(117))      