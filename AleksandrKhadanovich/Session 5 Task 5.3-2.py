def get_ordered_stud(file_path):
    with open (file_path,'r') as reader, open (r'data\sorted_stud.csv', 'w') as writer:
        text = reader.readlines()


        a=[]
        for i in range (len (text)-1):
            a.append(int((text [i+1].split(','))[1]))                    
        a=sorted(a, reverse=1)
        print(len(a))
        L=[]
        

        for item in a:
           for i in range (len (text)-1):
                if int((text [i+1].split(','))[1]) == item and (text [i+1]) not in L:
                    L.append((text [i+1]))
                    writer.write (str (text [i+1]))
                    break
   



  
  

print(get_ordered_stud(r'data/students.csv'))



     



   


































