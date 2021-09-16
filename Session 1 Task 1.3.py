
""" According to the task program should accept a comma separated
sequence of words as input. In the example we can see input as words in quotes
and all sequence are in square brackets.
   So I provide two options. 
"""

s = input () # input as a,b,c
words=[i for i in s.split (',')]

s=s.split(',')

r=[]
r.append (s[0])

for i in range (1, len(s)):
   if s[i] not in r:
      r.append (s[i])
   else:
      pass
print (sorted(r)) 






s = input () #input as ['a','b','c']
import ast
s = ast.literal_eval (s)

r=[]
r.append (s[0])

for i in range (1, len(s)):
   if s[i] not in r:
      r.append (s[i])
   else:
      pass
print (sorted(r)) 










   






   






        
        

    
               
                
