def get_top_performers(file_path, number_of_top_students=5):
    with open (file_path,'r') as reader:
        text = reader.readlines()
        #text= [i.rstrip() for i in text]
        
        a=[]
        for i in range (len (text)-1):
            a.append(float((text [i+1].split(','))[2]))                    
        a=sorted(a, reverse=1)

        L=[]
        for g in a[:(number_of_top_students)]:
           for i in range (len (text)-1):
                if float((text [i+1].split(','))[2]) == g and (text [i+1].split(','))[0] not in L:
                    L.append((text [i+1].split(','))[0])

                    
        print(L) # For any case) 'Josephina Medina' has a higher mark then 'Joseph Head' 
  

print(get_top_performers(r'data/students.csv'))







   


































