def foo(lst):
    k=[]
    m=1
    for i in lst:
        for j in lst:
            if lst.index(i)!= lst.index(j):
                m=m*j
        k.append(m)
        m=1
    return (k)


    
print(foo([1, 2, 3, 4, 5]))
print (foo ([3, 2, 1]))
  
    
