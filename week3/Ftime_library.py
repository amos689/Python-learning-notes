import time as t
start=t.perf_counter()
scale=10
#print("{:-^20}".format('执行开始'))
print("执行开始".center(20,'-'))
#返回一个长度为width,两边用fillchar(单字符)填充的字符串
#即字符串str居中，两边用fillchar填充
#若字符串的长度大于width,则直接返回字符串str
for i in range(scale+1):
    a='*'*i
    b='.'*(10-i)
    c=i*10
    print("\r{:^3}% [{}->{}]".format(c,a,b),end='')  #宽度为三，居中对齐
    t.sleep(0.1)
    if (i==10):
        print("")
end=t.perf_counter()
print("{:-^20}\n共用时{:.6f}s".format('执行结束',(end-start)))