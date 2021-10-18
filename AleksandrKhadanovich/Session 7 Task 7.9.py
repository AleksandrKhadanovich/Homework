class EvenRange:
    def __init__(self, start, end):
        if isinstance (start, int) and isinstance (end, int):
            if start < end:
                self.start = start
                self.end = end
            else:
                print (f"{start} is more than {end}")
                raise ValueError
        else:
            print (f"{start} and {end} shold be numbers")
            raise ValueError
        if self.start%2!=0:
            self.start= self.start+1       
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            out = self.start
            self.start= self.start+2
            return out
        else:
            if self.start== self.end or self.start== self.end +1:
                self.start= self.start+2
                return '"Out of numbers!"'
            else:
                raise StopIteration
                                           
    def __str__ (self):
        return str(self)
    

er1=EvenRange (7,11)
print (next (er1))
print (next(er1))
print(next(er1))


er2=EvenRange(3,14)
for number in er2:
    print (number, end = ' ')


    
