#question 9
import random as rd
num = [rd.randint(1, 100) for i in range(20)]
a = sorted(num[:10])
b = sorted(num[10:], reverse=True)
print(a+b)
