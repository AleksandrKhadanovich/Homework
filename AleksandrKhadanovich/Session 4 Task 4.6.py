def get_shortest_word(s):
    import string
    for i in s:
        if i in string.whitespace:
            s = s.replace(i, ' ')
        if string.whitespace in i:
            s = s.replace(string.whitespace, ' ')
    print (s)    
    m=s.split(' ')
    
    n=''
    for i in m:
        if len(i)> len(n):
            n= i

    return (n)

    
print(get_shortest_word('Python is simple and effective!'))
print (get_shortest_word('Any pythonista like namespaces a lot.'))
  
    
