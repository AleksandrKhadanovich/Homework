test_strings = ["hello", "world", "python", ]


def test_1(*lst):
    i=0
    k=set(lst[i])

    for i in lst:
        k = k.intersection(set(i)) 
    return (k)

print(test_1(*test_strings))



def test_2(*lst):
    k=set()
    for i in lst:
        for j in i:
            if j not in k:
                k=k.union (set(i))
    return (k)
    
print(test_2(*test_strings))    



def test_3(*lst):
    i=0
    b=set()
    k=set(lst[0+i])
    for j in lst[1+i:]:
        b = b.union(k.intersection(set(j)))
    i+=1
    return (b)
    
print(test_3(*test_strings))



def test_4(*lst):
    b=set()
    import string
    abc=set(string.ascii_lowercase)
    for j in lst:
        for h in j:
            b = b.union(set(h))
    l= abc.difference(b)
    return (l)
 
print(test_4(*test_strings))





































