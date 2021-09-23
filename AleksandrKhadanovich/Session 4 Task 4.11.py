dict_1={'a' : 100, 'b' : 200}
dict_2={'a' : 200, 'c' : 300}
dict_3={'a' : 300, 'd' : 100}

dicts=(dict_1, dict_2,dict_3)

def combine_dicts(*args):
    newdict={}
    for i in args:
        for j in i.keys():
            if j not in newdict.keys():
                newdict [j] = i[j]
            else:
                newdict [j] = newdict[j]+ i[j]
        
    return (newdict)

print (combine_dicts(dict_1, dict_2))
print (combine_dicts(dict_1, dict_2, dict_3))







        


