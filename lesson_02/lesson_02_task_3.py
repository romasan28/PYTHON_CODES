import math
def square (sq):
   return  sq ** 2 if sq % 1 == 0 else math.ceil(sq) ** 2

s = float(input())
ss = square(s)        
print("Площадь квадрата: ",ss)