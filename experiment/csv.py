import csv
import random as rd
import datetime as dt
with open("data1.csv", 'w', encoding="UTF8", newline="") as fp:
    wr = csv.writer(fp)
    wr.writerow(['日期', "销量"])
    datadate = dt.date(2020, 1, 1)
    for i in range(100):
        amount = 500+i*5+rd.randint(5, 50)
        wr.writerow([str(datadate), amount])
        datadate = datadate+dt.timedelta(days=1)
with open("data1.csv", 'r', encoding="UTF8") as fp:
    for line in csv.reader(fp):
        print(*line)
