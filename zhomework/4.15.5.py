#question 5
grade=["优","良","中","及格","不及格"]
score=eval(input("请输入一个分数"))
if score>=90:
    print(grade[0])
elif score>=80:
    print(grade[1])
elif score>=70:
    print(grade[2])
elif score>=60:
    print(grade[3])
else:
    print(grade[4])