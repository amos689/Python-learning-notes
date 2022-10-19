#二者效果一样
ls1=[]
ls2=[]
for i in range(1,6):
    if i%2==0:
        continue
    for j in range(1,6):
        if j%2==0:
            ls1.append((i,j))
print(ls1)

ls2=[(i,j) for i in range(1,6) if i%2 for j in range(1,6) if not j%2]
print(ls2)