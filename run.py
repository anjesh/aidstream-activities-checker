import csv
from IatiActivities import *

outfile = open('data/iati-activites-with-errors.csv', 'w')
csvwriter = csv.writer(outfile, delimiter=',',quotechar='"')

infilename = "data/iati_activities-2015.02.16.csv"
with open(infilename, "rU") as infile:
    rowCount = 0
    errorRows = 0
    csvreader = csv.reader(infile, delimiter=',')
    for row in csvreader:
        if rowCount == 0:
            #header 
            rowCount += 1
            csvwriter.writerow(row)
            continue
        activityRow = IatiActivityRow(row)
        activityRow.process()        
        if activityRow.hasError():
            errorRows += 1
            errors = activityRow.getErrors()
            row.append(errors)
        else:
            row.append("")
        csvwriter.writerow(row)
        rowCount += 1

print "Total Rows: ", rowCount
print "Total Errors Rows: ", errorRows
    
