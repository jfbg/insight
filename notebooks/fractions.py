def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
        
    def show(self):
        print(''.join([str(self.num),"/",str(self.den)]))
        
    def __str__(self):      #what to return for print(class)
        return str(self.num)+"/"+str(self.den)    
    
    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __mul__(self, otherfraction):
        
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)