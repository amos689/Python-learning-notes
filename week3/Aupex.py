def dayup(up):
    org=1
    for i in range(365):
        if i % 7 in [6,0]:
            org*=(1-0.01)
        else:
            org*=(1+up)
    return org
fac1=0.01
while dayup(fac1) < 37.78:
    fac1+=0.001
print("A君需要每天努力：%.3lf"%(fac1),end="")
好='才能超过B君'
print("%s%.3lf"%(好,fac1))
耶=2*好
print("%s"%(耶))
耶=好+'好耶！'
print("%s"%(耶))