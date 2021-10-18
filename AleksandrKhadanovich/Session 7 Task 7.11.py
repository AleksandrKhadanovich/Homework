def endless_fib_generator():
    i=1
    b=0
    c=0
    while True:
        yield (i)
        c=b
        b=i
        i=b+c
            
gen = endless_fib_generator()
while True:
    print(next(gen))




