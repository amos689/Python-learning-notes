yuan = input()
if yuan[0:3] in ["RMB"]:
    print("USD{:.2f}".format(eval(yuan[3:])/6.78))#符号名后[]中没有先导就默认从第0个开始，没有后导就默认直接进行到结束
elif yuan[:3] in ['USD']:#在python中，单引号和双引号对字符串是没有区别的
    print("RMB{:.2f}".format(eval(yuan[3:])*6.78))