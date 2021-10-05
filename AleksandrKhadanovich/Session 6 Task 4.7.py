import decimal
from decimal import Decimal

class Money:   
    def __init__ (self, summ, currency):
        self.summ = Decimal(summ)        #(Base - BYN=1)
        self.currency=currency
        exchange_rate= {'EUR': Decimal(3.1), 'USD':Decimal (2.6), 'BYN':Decimal(1)}
        self.exchange_rate=exchange_rate

    def convert(self, from_currency, to_currency, amount): 
        amount = amount / self.exchange_rate[to_currency]
        out_amount = round(amount * self.exchange_rate[from_currency], 2)
        return Decimal (out_amount)

    def __str__(self):
        return f"{self.summ} {self.currency}"

    def __add__ (self, other):
        if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return Money (self.summ + other.summ, self.currency)
        else:
            return Money (self.summ + other, self.currency)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)   

    def __sub__(self,other):
        if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return Money (self.summ - other.summ, self.currency)
        else:
            return Money (self.summ - other, self.currency)

    def __mul__(self,other):
        if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return Money (self.summ * other.summ, self.currency)
        else:
            return Money (self.summ * other, self.currency)
    
    def __truediv__(self, other):
        if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return Money (round((self.summ / other.summ),2), self.currency)
        else:
            return Money (round((self.summ / other),2), self.currency)
    
    def __eq__(self, other):
       if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return (round(self.summ),2) == other.summ 

    def __ne__(self, other):
       if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return self.summ != other.summ
        
    def __lt__(self, other):
       if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return self.summ < other.summ       

    def __gt__(self, other):
       if isinstance  (other, Money):
            other.summ = Money.convert(self, other.currency, self.currency, other.summ)
            return self.summ > other.summ      

    
    
y= Money (10, 'BYN')
x= Money (11, 'USD')
z= Money (12.5, 'EUR')


#print (x+y-z)
#print(x+2)
#print(x+y+z)
print(z*x/y)
#print (y+z/2)
#print (y>z)
#print (y<z)
#print (y!=z)
#print (z==y)
#lst=[x,y,z]
#print(sum (lst))

        

