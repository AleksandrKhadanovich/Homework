class Sun:
    instance = None    
    @classmethod
    def inst(cls):
        if not cls.instance:
            cls.instance = Sun()
        return cls.instance


a = Sun.inst()
b = Sun.inst()
print(a is b)









class Sun:
   instance = None
   @staticmethod 
   def inst():
      if Sun.instance == None:
         Sun()
      return Sun.instance
         

p = Sun.inst()
f = Sun.inst()
print(p is f)









