ht,wt=eval(input())
bmi=wt/pow(ht,2)
print("BMI值为{}".format(bmi))
who,cn='',''
if bmi<18.5:
    who,cn='偏瘦','偏瘦'
elif 18.5<=bmi<24:
    who,cn='正常','正常'
elif 24<=bmi<25:
    who,cn='正常','偏胖'
elif 25<=bmi<28:
    who+='偏胖'
    cn+='偏胖'
elif 28<=bmi<30:
    who,cn='偏胖','肥胖'
else:
    who,cn='肥胖','肥胖'
print("WHO:{}, CN:{}".format(who,cn))