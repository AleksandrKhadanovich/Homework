def get_pairs(lst):  # -> List[Tuple]
    if len (lst)==1:
        return None
    else:
        newlst= []
                        
        for i in range(len(lst) -1):
            
            if (i+1)> (len(lst)):
                break
            else:
                pcs= (lst[i],lst[i+1])
                newlst.insert (i, pcs)

    return (newlst)


print (get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs([1]))
  
    
