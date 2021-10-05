def most_common_words(filepath, number_of_words=3):
    import string
    with open (filepath,'r') as reader:
        text = str (reader.readlines())

        redundant = string.punctuation
        for i in text:
            for j in i:
                if j in redundant:
                    text = text.replace(j, ' ')
        text = text.split(' ')       

        d={}
        for i in text:
            if len(i)>0 and i!= 'n' and (i not in d.keys()):
                d[i] = text.count(i)
        
        s = sorted (list (d.values ()))
        L=[]
        for g in s[-(number_of_words):]:
            for i, j in d.items():
                if j == g:
                    L.append(i)
                    del d [i]
                    break
    return L

        

            
print(most_common_words(r'data/lorem_ipsum.txt'))








   


































