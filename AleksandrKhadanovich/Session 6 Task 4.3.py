import string


class Cipher():
    
    def __init__(self,password):
        self.password = password
        
        self.out_message = ""
        abc = (string.ascii_lowercase)
        
        for i in abc:
            if i in self.password:
                abc= abc[:(abc.index(i))]+ abc[(abc.index(i)+1):]

        self.new_abc = self.password+abc
        self.abc =(string.ascii_lowercase)

    def encode(self, message):
        self.message = message
        self.out_message = ''

        for letter in message:
            if letter.lower() in self.abc:
                if letter.isupper():
                    self.out_message = self.out_message + (self.new_abc [self.abc.index(letter.lower())]).upper()
                else:
                    self.out_message = self.out_message + (self.new_abc [self.abc.index(letter)])
            else:
                self.out_message = self.out_message + letter

        print (self.out_message)

    def decode(self, message):
        self.message = message
        self.out_message = ''

        for letter in message:
            if letter.lower() in self.abc:
                if letter.isupper():
                    self.out_message = self.out_message + (self.abc [self.new_abc.index(letter.lower())]).upper()
                else:
                    self.out_message = self.out_message + (self.abc [self.new_abc.index(letter)])
            else:
                self.out_message = self.out_message + letter

        print (self.out_message)



cipher = Cipher('crypto')
cipher.encode("Hello world")


cipher.decode("Fjedhc dn atidsn")






            
        


        
   
 
