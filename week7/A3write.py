'''
writelines() 方法用于向文件中写入一序列的字符串。
这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
换行需要制定换行符 \n。

write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，
否则报错：TypeError: a bytes-like object is required, not 'str'。
'''
f=open("E:\learning notes\C_learing\pyexperiment\week7\A3.txt",'a+',encoding="UTF-8")
lst=['\n','美国','中国','俄罗斯']
f.writelines(lst)
#也可以这样，直接变成字符串写入
f.write("".join(lst))
f.write('\n很好很牛逼')
f.seek(0)
for i in f:
    print(i,end='')
f.write("".join(["hhh","kkk"]))
f.close()