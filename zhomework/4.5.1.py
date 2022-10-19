z_str='http://sports.sina.com.cn/'
count1=0
for i in z_str:
    if i=='t':
        count1+=1
print('t出现{}次'.format(count1))
print(z_str.index('com')+1)
z_str=z_str.replace('.','-')
print(z_str)
print(z_str[7:13],''.join(reversed(z_str[-9:-13:-1])))
z_str=z_str.upper()
print(z_str)
count2=0
for i in z_str:
    count2+=1
print(count2)
z_str+="index"
print(z_str)
