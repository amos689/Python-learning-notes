'''
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
返回从字符串中读取的字节。
	
file.readline([size])
读取整行，包括 "\n" 字符
返回从字符串中读取的字节。
	
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 
实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
返回列表，包含所有的行。
readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 
如果碰到结束符 EOF 则返回空字符串。
(单个文本也能用for...in...结构进行处理)
'''

tx=open("E:\learning notes\C_learing\pyexperiment\week7\A2.txt","r",encoding="UTF-8")
for ln in tx.readlines():   #一次性全部读入，如果文本量过大不推荐，占用内存
    print(ln,end="")
print("\n\n")
#发现直接试图让其输出两次不能完成，原因是指针已经移动，其不再指向首字符
#方法1(不推荐)：关闭再打开
'''
tx.close()
tx=open("E:\learning notes\C_learing\pyexperiment\week7\A2.txt","r",encoding="UTF-8")
for i in tx:
    print(i,end="")
tx.close()
'''
#方法2(推荐)：使用seek函数
tx.seek(0)
for i in tx:
    print(i,end="")
tx.close()