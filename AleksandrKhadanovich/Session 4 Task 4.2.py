
def ispalindrome ():
    a= input()
    i = 0
    j=-1
    for v in range (len(a)):
        if a [i] != a[j]:
            return ('Not palindrome')
            break
        else:
            i+=1
            j-=1
    return('It is palindrome')
 
print (ispalindrome ())
    

 
