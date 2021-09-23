z=[]
def sorting(m, k = ' ', numb = 0):
    if m.find (k)== -1:
        z.append(m)
    else:
        if numb!=0:
            
            z.append (m[:(m.index(k))])
            x=m[(m.index(k)+1):]
            if numb ==1:
                z.append (x)
            else:
                numb-=1
                sorting (x,k,numb)
                
      
        else:
            z.append (m[:(m.index(k))])
            x=m[(m.index(k)+1):]
            sorting (x,k)
        
    return (z)

        

c= input( 'Enter string ____  ')
    

def mysplit (a, maxsplit= 0):
    l= sorting (c, a, numb=maxsplit)
    return (l)
        
print (mysplit(',',maxsplit = 3))
    
