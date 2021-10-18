class MyNumberCollection:           
    def __init__(self, start, end=None, step=None):
        self.lst = []        
        self.start = start
        self.end=end
        if step and isinstance (step,int):
            self.step =step
        else:
            self.step = 1
                           
        if not self.end:
            try:
                iterator = iter(self.start)
            except TypeError:
                print (f"{start} is not iterable collection")
            else:                               
                if all (isinstance (i, int) for i in self.start):                   
                    self.lst = list (self.start)
                else:
                    print (f"TypeError: MyNumberCollection supports only numbers!")                   
                    #raise TypeError               
        if self.end:
            
            if isinstance (self.start, int) and isinstance (self.end, int):
                for i in range(self.start,self.end, self.step):                    
                    (self.lst).extend ([i])
                (self.lst).append (self.end)                
            else:
                print (f"{start} and {end} should be integers")
                raise ValueError
        self.count = 0
                    
    def __iter__(self):
        return self               
            
    def __str__(self):
        return str(self.lst)
    
    def __next__(self):
        if self.count < len(self.lst):
            item = self.lst[self.count]
            self.count = self.count + 1
            return item
        else:
            raise StopIteration       
    
    def __add__(self, other):               
        self.new_lst = list(self.lst) + list(other)              
        return self.new_lst

    def append (self, other):
        if isinstance (other,int):
            self.lst.append (other)
            return self.lst
        else:
            print (f"{other} - object is not a number!")
            #raise TypeError                

    def __getitem__(self, key):
        return self.lst[key]**2

col1 = MyNumberCollection (0,5,2)
print (col1)

col2 = MyNumberCollection ((1,2,3,4,5))
print (col2)

col3 =MyNumberCollection ((1,2,3,'4',5))

col1.append (7)
print (col1)

col2.append ('string')

print(col1 + col2)

print (col1)

print (col2)

print (col2[4])

for item in col1:
    print (item, end = ' ')



