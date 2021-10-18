class MySquareIterator:
    def __init__(self, data):
        try:
            iterator = iter(data)
        except TypeError:
            print (f" {data} not iterable")
        else:
            if all (isinstance (i, int) for i in data):
                self.data = data
                self.count = 0
            else:
                print (f" {data} items should be integers")
                raise ValueError
       
    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.data):
            raise StopIteration
        square = self.data[self.count] ** 2
        self.count = self.count + 1
        return square
                      

lst=[1,2,3,4,5]
itr = MySquareIterator (lst)
for item in itr:
    print (item, end = ' ')

