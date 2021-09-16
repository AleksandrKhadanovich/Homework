a= int (input ('Enter min value of the first interval ______    '))
b= int (input ('Enter max value of the first interval ______    '))
c= int (input ('Enter min value of the second interval ______    '))
d= int (input ('Enter max value of the second interval ______    '))
if a > b or c > d:
    print ('Неверный ввод')
else:
    for j in range (d-c+1):
        print ('', c+j, sep= '\t', end = '')
        
        
    for i in range(b - a + 1):
        print ('\n',a+i, end = '\t')
        for k in range (d - c +1):
            print ((a+i)*(c+k), '', sep ='\t', end = '')
            

            

