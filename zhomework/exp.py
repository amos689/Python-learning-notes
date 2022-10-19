stu=input()
ls=[]
wok=stu.split(";")
for i in wok:
    ls.append(i.split(","))
name1,xuehao1,score1=ls[0][0],ls[0][1],ls[0][2]
name2,xuehao2,score2=ls[1][0],ls[1][1],ls[1][2]
name3,xuehao3,score3=ls[2][0],ls[2][1],ls[2][2]
for i in ls:
    if len(i[0]) <=1:
        print("{}名字不合法".format(i[0]))
for i in ls:
    if i[1][0]=="0":
        print("学号{}0开头".format(i[1]))
    for j in i[1]:
        if ord(j)<48 or ord(j)>57:
            print("学号{}存在非数字".format(i[1]))
            break
for i in ls:
    if len(i[1])<10:
        print("学号{}长度不合法".format(i[1]))
for i in ls:
    try:
        if not isinstance(eval(i[2]),int):
            print("成绩{}含非数字".format(i[2]))
    except:
        print("成绩{}含非数字".format(i[2]))
students_info=list()
for i in wok:
    students_info.append(i.split(",",1))
for i in students_info:
    tmp=str(i[1])
    i[1]=tuple(tmp.split(","))
students_info=tuple(students_info)
print(students_info)
for i in ls:
    print("学号{}对应的学生姓名为{}，其成绩为{}".format(i[1],i[0],i[2]))