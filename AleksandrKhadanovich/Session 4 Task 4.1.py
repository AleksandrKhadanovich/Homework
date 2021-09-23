
def quotesreplace ():
    a= input()
    c= ''
    for i in a:
        if i =="'":
            c+='"'
        elif i =='"':
            c+="'"
        else:
            c+=i
    return c

print (quotesreplace ())
    

 
