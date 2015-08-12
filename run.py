import csv
import os
import argparse
from IatiActivities import *

parser = argparse.ArgumentParser(description='Prepares the error report from iati aidstream activities')
parser.add_argument('-i','--infile', help='File name of the input csv filepath.', required=True)
parser.add_argument('-o','--outfile', help='File name of the output csv file. Prepares csv in "out" folder.', required=True)
results = parser.parse_args()

infilename = results.infile;
outfilename = os.path.join("out", results.outfile);


outfile = open(outfilename, 'w')
csvwriter = csv.writer(outfile, delimiter=',',quotechar='"')

with open(infilename, "rU") as infile:
    rowCount = 0
    errorRows = 0
    csvreader = csv.reader(infile, delimiter=',')
    for row in csvreader:
        if rowCount == 0:
            #header 
            rowCount += 1
            row.extend(["Error", "Error Desc"])
            csvwriter.writerow(row)
            continue
        activityRow = IatiActivityRow(row)
        activityRow.process()        
        if activityRow.hasError():
            errorRows += 1
            errors = activityRow.getErrors()
            row.extend([1, errors])
        else:
            row.extend(["", ""])
        csvwriter.writerow(row)
        rowCount += 1

print "Total Rows: ", rowCount
print "Total Errors Rows: ", errorRows
    
