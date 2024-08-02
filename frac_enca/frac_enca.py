from IPython.display import display, Math
import math

class frac:

    def __init__(self, num, denom):

        if denom == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        self.num = num
        self.denom = denom


    def __repr__(self):
       
       if self.denom == 1:
           return str(self.num)
       else:   
           return str(self.num)+ "/" + str(self.denom)


    def __add__(self, other):

        if isinstance(other, frac):
            if self.denom == other.denom:
                self.num = self.num + other.num
                return frac(self.num, self.denom).simplify()
            
            else:
                self.num *= other.denom
                other.num *= self.denom
                self.denom *= other.denom
                self.num = self.num + other.num
                return frac(self.num, self.denom).simplify()
            
        elif isinstance(other, int):
            other = frac(other, 1)
            return self + other
        else:
            return NotImplemented
    

    def __sub__ (self, other):

        if isinstance(other, frac):
            if self.denom == other.denom:
                self.num = self.num - other.num
                return frac(self.num, self.denom).simplify()
            
            else:
                self.num *= other.denom
                other.num *= self.denom
                self.denom *= other.denom
                self.num = self.num - other.num
                return frac(self.num, self.denom).simplify()
            
        elif isinstance(other, int):
            other = frac(other, 1)
            return self - other
        else:
            return NotImplemented
        
    def __mul__ (self, other):

        if isinstance(other, frac):          
                self.num *= other.num
                self.denom *= other.denom
                return frac(self.num, self.denom).simplify()
            
        elif isinstance(other, int):
            other = frac(other, 1)
            return self * other
        else:
            return NotImplemented
    
    def __truediv__ (self, other):

        if isinstance(other, frac):          
                self.num *= other.denom
                self.denom *= other.num
                return frac(self.num, self.denom).simplify()
            
        elif isinstance(other, int):
            other = frac(other, 1)
            return self * other
        else:
            return NotImplemented
            

    def simplify(self):

        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

        return frac(self.num, self.denom)


    def expand(self, value):

        self.num *= value
        self.denom *= value

        return frac(self.num, self.denom)