class Maxval(Exception):
    def __str__(self): return 'Maximal value is reached.'

class Counter:
    
    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop
        self.k=0
        if self.start:
            self.k =self.start
        else:
            self.start = 0 
        
    def increment(self):
        myexc = "My exception string"
        if self.k != self.stop:
            self.k +=  1
        else:
            raise Maxval()
                   
    def get(self):
        print (self.k)

c = Counter(start=42)
c.increment()
c.get()

c = Counter()
c.increment()
c.get()

c.increment()
c.get()

c = Counter(start=42, stop=43)
c.increment()
c.get()

c.increment()
c.get()



            
        


        
   
 
