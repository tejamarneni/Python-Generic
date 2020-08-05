# the program is created using lucid programming youtube channel
l1 = [7,8,12,7,23,98,125,854,45]

def binary_search(data,target,low,high):
    data = sorted(data)
    if low > high:
        return False
    else:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low, mid-1)
        else:
            return binary_search(data,target,mid+1,high)            

print(binary_search(l1,45,0,len(l1)-1))          