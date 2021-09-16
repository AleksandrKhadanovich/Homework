"""As far as dictionary may contain nested dictionaries
this program print all unique values of ALL dictionaries."""

#lst = [8, {'suc': 1, 'ret': {'376': {'typ': 'bu', 'amo': 0, 'rat': 0.03}, '240': {'type': 'sell', 'status': 0}}}]
lst=[{'V':'S001'},{'V':'S002'},{'VI':'S001'},{'VI':'S005'},{'VII':'S005'},{'V':'S009'},{'VIII':'S007'}]
     

a=set()

def func (**kwargs):
    for i,j in kwargs.items():
        if not isinstance(i, dict):
            pass
        else:
            func(**i)
        if not isinstance(j, dict):
            a.add(j)
            pass
        else:
            func(**j)

    return a

for z in lst:
    if isinstance (z, dict):
        func(**z)
print (a)
    

 
