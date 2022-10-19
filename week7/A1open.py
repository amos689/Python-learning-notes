'''
open() 函数用于创建或打开指定文件，并返回文件对象，该函数的常用语法格式如下：
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
此格式中，用 [] 括起来的部分为可选参数，即可以使用也可以省略。其中，各个参数所代表的含义如下：
file：表示要创建的文件对象。
file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区（本节后续会详细介绍）。
encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）。
(以下是四种基本打开方式)
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑
    即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
x	写模式，新建一个文件，如果该文件已存在则会报错。
(以下除了+可以单独使用，其他的必须与上面四种配套使用)
+	打开一个文件进行更新(可读可写)。
b	二进制模式。
t	文本模式 (默认)。
'''
tf=open("E:\\learning notes\\C_learing\\pyexperiment\\week7\\A1.txt","r",encoding="utf-8")
print(tf.readline())
b=tf.readline()
print("true" if bool(b) == False else "false",type(b))
tf.close