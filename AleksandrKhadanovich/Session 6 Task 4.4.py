class Bird:
    def __init__(self,name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")


class FlyingBird (Bird):
    def __init__(self,name,ration=None):
        Bird.__init__(self,name)
        self.ration = ration
        if ration== None:
            self.ration = 'Corn'

    def __str__(self):
         return str(f"{self.name} can walk and fly")

    def eat(self):
        print (f"It eats mostly {self.ration}")

class NonFlyingBird (Bird):
    def __init__(self,name,ration=None):
        Bird.__init__(self,name)
        self.ration = ration
        if ration== None:
            self.ration = 'Seed'
            
    def eat(self):
        print (f"It eats {self.ration}")
        
    def fly(self):
        print(f"{self.name} bird can not fly")
        
    def swim(self):
        print (f"{self.name} can swim")

class SuperBird(Bird):
    
    def __init__(self,name,ration=None):
        Bird.__init__(self,name)
        if ration== None:
            self.ration = 'fish'

    def eat(self):
        print (f"It eats {self.ration}")


    def __str__(self):
         return str(f"{self.name} can walk, swim and fly"
)
        
    
   
    
b = Bird("Any")
b.walk()


p = NonFlyingBird("Penguin", "fish")
p.swim()

p.fly()

p.eat()


c = FlyingBird("Canary")
print(c)

c.eat()


s = SuperBird("Gull")
print(s)

s.eat()






            
        


        
   
 
