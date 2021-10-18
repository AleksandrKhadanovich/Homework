import cmd,sys

class Gold_conj(cmd.Cmd):    
    prompt = '%: '
    intro = "Program for prooving Goldbach's conjecture. For list of commands enter 'help'"
    doc_header = "Possible commands"
    misc_header = "Process any integer"
    undoc_header = "To process number enter 'check number' \nFor example: check 90 \nTo quit press 'q'"


    def isinteger(self, x): # checks if the entered value is integer
        self.x=x
        while True:
            try:
                self.x= int(self.x)
            except ValueError as j:
                print ("It is not integer")
                self.x = input('Enter number ______  ')
                continue
            else:
                break

        if self.x < 4:
            print ('The number is smaller than 4.')
            k= input('Enter another one ______  ')
            Gold_conj.isinteger (self, k)            

        elif self.x%2!= 0:
            print ('The number is not even.')
            k= input('Enter another one ______  ')
            Gold_conj.isinteger (self, k)
        else:
            pass                 
        return self.x

    def isprime(self, n): # checks if the entered integer is prime
        while True:
            try:
                n= int(n)
            except ValueError as j:
                print ("It is not integer")
                n = input('Enter number ______  ')
                continue
            else:
                break
        
        k=0        
        for j in range (2,n):
            if n%j==0:
                k+=1
            if k!=0:                
                return False                
        if k==0:
            return True
                        

    def do_check (self, m):        
        "Check if Goldbach's conjecture is verified. Enter an even number from 4."        
        if Gold_conj.isinteger (self, m):                        
            self.m=int (self.x)
            cnt=0
            a=1
            b=self.m - 1
            for i in range (self.m):
                if Gold_conj.isprime (self, a) and Gold_conj.isprime (self, b):
                    print (f"{self.x} consists of prime {a} and prime {b} \n")
                    cnt+=1
                    break
                else:
                    a+=1
                    b-=1
            if cnt==0:
                print (' Goldbach"s mistake ')
            
    def do_q(self, arg):
        "Enter q to quit"
        sys.exit(1)
   
    def do_EOF(self, line):
        return True    
    
if __name__ == '__main__':
    Gold_conj().cmdloop()

