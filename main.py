# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from datetime import date

ftime = date.today().strftime('%m/%d').split('/')
fyear = int(date.today().strftime('%Y'))

celebrate = False

with open('bd.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        person = row[0]
        bdyear = int(row[1].split('/')[-1])
        age = fyear - bdyear
        bd = row[1].split('/')[:-1]
        if ftime == bd:
            print person, 'is turning', age, 'today!!!'
            celebrate = True

if not celebrate:
    print "Nothing to celebrate :("