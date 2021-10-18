def endless_generator():
    i=1
    while True:
        if i%2!=0:
            yield (i)
        i+=1
            



gen = endless_generator()
while True:
    print(next(gen))

