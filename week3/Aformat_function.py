'''引导，填充，对齐，宽度'''
print("{1:=^20}".format('python','AK','WA'))
#1表示从零数第一个变量，'='是填充符，>右对齐，<左对齐，^居中对齐，20总宽度


'''千位分隔符，数字精度，类型'''
print("{:,.2f}".format(123456.7896))
#,表示插入符合英国人的三位数一逗号分隔符，.2f表示输出两位
print("{0:b}  {0:c}  {0:d}  {0:o}  {0:x}  {0:X}".format(425))
#当有多个大括号却只有一个format数字时必须在：前加0，b是二进制输出
#c是对应字符输出，d是整形输出，o是八进制输出，x和X是十六进制小和大写输出
print("{0:.3e}  {0:E}  {0:.2f}  {0:.2%}".format(31.4156))
#e,E表示科学计数法大/小写输出，f表示浮点数输出，%表示百分比输出
#由输出结果，除了%以外其他数均可.x来表示'化简到最简后'再保留x位小数