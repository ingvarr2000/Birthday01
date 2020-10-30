
import csv, re
from datetime import date

all_bds = {}
all_years = {}

fdate = date.today().strftime('%m/%d').split('/')
fyear = int(date.today().strftime('%Y'))

today = '{0}/{1}'.format(fdate[0], fdate[1])

date_patt = re.compile("^[0-9][0-9]/[0-9][0-9]$")

with open('bd.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        person = row[0]
        bdyear = int(row[1].split('/')[-1])
        bd = row[1].split('/')[:-1]
        bdstr = '{0}/{1}'.format(bd[0], bd[1])
        if not date_patt.match(bdstr):
            print "The DoB of", person, "(", bdstr, ") is invalid !!!"
        all_years[person] = bdyear
        if bdstr in all_bds:
            all_bds[bdstr].append(person)
        else:
            all_bds[bdstr] = [ person ]

#print all_bds
#print all_years

if today in all_bds:
    print "Congrats"
    for person in all_bds[today]:
        age = int(fyear) - int(all_years[person])
        print person, "who turns", age, "years old today"
else:
    print "No one to congratulate :("