prime_list = list()

def primelist(num):
    i = 1
    j = 3
    prime_list = []
    while i <= num:
        d = 0
        for k in range(3,int(j**0.5)+1,2):
            if j % k == 0:
                d += 1
        if d == 0:
            prime_list.append(j)
            i += 1
        j += 2
    return prime_list     

# prints n prime numbers
print(primelist(10000))
         
