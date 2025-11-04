a = (3,4,5,(3,2,1),7, (4,5,(4,2),3),5,7)
print(a)


def flatten_tuple(tple):
    lst = list()
    for item in tple:
        if isinstance(item,tuple):
            lst.extend(flatten_tuple(item))
        else:
            lst.append(item)
    return tuple(lst)

r = flatten_tuple(a)
print(r)
