class HistoryDict:
    def __init__(self, dct):
        self.dct = dct
        self.L=[]
        
    def set_value (self,key, value):
        if len (self.L)<11:
                self.L.append (key)
        else:               
                self.L.pop(0)
                self.L.append (key)        
        self.dct[key]=value               

    def get_history(self):
        print (self.L)
   
d = HistoryDict ({"foo": 42})
d.set_value("bar", 43)
d.get_history()


     
        


        
   
 
