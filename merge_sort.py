a = [78,45,1,6,2,99,123,0,-5,334,17,25,-23]

b = [6,8,4]
c = [7,5,9]

def merge(d,e):
    f =[]
    i = j = 0
    while i < len(d) and j < len(e):
        if d[i] < e[j]:
            f.append(d[i]) 
            i += 1
        else:
            f.append(e[j])
            j += 1
    if i == len(d):
        f.extend(e[j:])
    else:
        f.extend(d[i:])   
    return f

print(merge(b,c))

def merge_sort(g):

    if len(g) <= 1:
        return g

    left,right = merge_sort(g[:len(g)//2]),merge_sort(g[len(g)//2:])   

    return merge(left,right)

print(merge_sort(a))