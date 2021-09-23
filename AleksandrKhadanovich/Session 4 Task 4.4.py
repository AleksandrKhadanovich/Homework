def split_by_index (a, b):
    z=[]
    f=0
    for i in b:
        z.append (a[f:i])
        f=i
        x= a[i:]
    if x:
        z.append (x)
     
    return (z)
   
print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))


   
    
