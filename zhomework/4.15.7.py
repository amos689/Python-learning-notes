#question 7
with open("homework7.txt","w") as f:
    word=input("请输入一个字符串")
    word=word.upper()
    f.write(word+"\n")
