a=eval(input("请输入以','为分隔的自然数列表:"))
a.sort(reverse=True)
if abs(a[0])>abs(a[-1]):
    print(a[0])
else:
    print(a[-1])