class Even_exc(Exception):
    pass


class Noteven(Even_exc):
    def __init__(self):
        self.z = "The number not even"
        print (self.z)

   
class Toosmall(Even_exc):
    def __init__(self):
        self.z = "The number too small"
        print (self.z)


class NotEnteg(Even_exc):
    def __init__(self):
        self.z = "The number is not integer"
        print (self.z)

        
def evencheck ():
    while True:
        a= input('Enter number ______  ')
        try:
            a= int(a)
        
        except ValueError as j:
                print ("The number is not integer")
                continue
        else:
            break

    if a < 2:
        raise Toosmall
    elif a%2!= 0:
        raise Noteven
    else:
        print ('The number is even!')


evencheck ()
