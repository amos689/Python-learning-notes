#question 14
s = input('请输入一个字符串：')
a = len(s)
i = 0
count = 1    
while i <= (a/2):
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break

if count == 1:
    print('您所输入的字符串是回文')
else:
    print('您所输入的字符串不是回文')