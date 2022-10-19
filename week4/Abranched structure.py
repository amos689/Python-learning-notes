# 1.普通的分支结构
guess=eval(input())
if guess==99:
    print("yes")
else:
    print("no")
    
# 2.紧凑的分支结构(<语句1> if <条件> else <语句2>)
inp=eval(input())
print("{}".format("yes" if inp==66 else "no"))