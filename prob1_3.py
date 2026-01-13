import csv
import sqlite3

paathh = "E:/assignment/userrs_listt.csv"

dbb = sqlite3.connect("E:/assignment/userrss.db")
curr = dbb.cursor()

curr.execute("create table if not exists userinfoo (naame text, emaill text)")

filee = open(paathh, "r")
readd = csv.reader(filee)

headd = next(readd)

for roww in readd:
    naamee = roww[0]
    emailll = roww[1]
    curr.execute("insert into userinfoo values (?,?)", (naamee, emailll))

dbb.commit()
dbb.close()

print("success")
