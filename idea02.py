
import csv, re
from datetime import date, timedelta

all_bds = {}
all_years = {}
days_ahead = 7

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

for mydays in range(0,days_ahead):
    fdate = (date.today() + timedelta(days=mydays)).strftime('%m/%d').split('/')
    futdate =  '{0}/{1}'.format(fdate[0], fdate[1])
    if futdate in all_bds:
        print "--- Heads up for", futdate
        for person in all_bds[futdate]:
            age = int(fyear) - int(all_years[person])
            print person, "who turns", age, "years old"
