npv=0
for i in range(1,6,1):
    a=eval(input())
    npv+=a/pow(1.1,i)
print(npv)