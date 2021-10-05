def call_once(func):
    n=0
    def wrapper_call_once(a,b):
        nonlocal n
        try:
            k=func(a,b)
            #print (k)
            n+=k
            n= str(n)
            print (n)
        except:
            print (n)
    return wrapper_call_once

@call_once
def sum_of_numbers(a,b):
    return a+b
    

sum_of_numbers(13,42)
sum_of_numbers(999,100)    
sum_of_numbers(134,412)







