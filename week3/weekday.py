str='星期一星期二星期三星期四星期五星期六星期日'
num=eval(input("请输入现在是第几天："))
pos=(num-1)*3
print(str[pos:pos+3]+'好耶！')
for i in range(12):
    c=chr(9800+i)
    print(c)
print(chr(9803))
