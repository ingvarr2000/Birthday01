
import csv
from datetime import date

all_bds = {}
all_years = {}

fdate = date.today().strftime('%m/%d').split('/')
fyear = int(date.today().strftime('%Y'))

with open('bd.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        person = row[0]
        bdyear = int(row[1].split('/')[-1])
        bd = row[1].split('/')[:-1]
        bdstr = '{0}/{1}'.format(bd[0], bd[1])
        all_years[person] = bdyear
        if bdstr in all_bds:
            all_bds[bdstr].append(person)
        else:
            all_bds[bdstr] = [ person ]

print all_bds
print all_years