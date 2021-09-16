s = (input ()).lower() #with method count()
d= {}
for i in s:
   a = s.count(i)
   if i in d:
      pass
   else:
      d[i]=a
print (d)   
   





s = input () # without method count()
s = s.lower()
a=0
d={}
for i in range(len(s)):
   b=s[i]
   for j in s:
      if j==b:
         a+=1
         d[b] = a
   a=0
print (d)
   






        
        

    
               
                
