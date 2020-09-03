
#method 1

def bubble_sort(a):
    swapped = True
    b = 0
    while swapped:
        swapped = False
        b += 1
        for i in range(0,len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
    print(b)            
    return a

#method 2

def bb_sort(b):
    for i in range(0,len(b)-1):
        for j in range(0,len(b)-i-1):
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
    return b

l = [6,1,8,9,4,2,5,11,23,55,43,26,98,13,14,165,29]
print(l)
print(bubble_sort(l))                
