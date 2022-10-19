#question 11
import csv
with open("price.csv",'r',encoding="UTF8") as f1:
    with open("priceout.csv","w",encoding="UTF8") as f2:
        w=csv.writer(f2)
        r=csv.reader(f1)
        for i in r:
            w.writerow(i)