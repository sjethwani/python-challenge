
import os
import csv

def normalizeDate(date):
    month,year = date.split("-")
    
    if int(year) < 100:
        year = "20" + year
    normalize_date = month + "-" + year
    return (normalize_date)
    
csvpath1 = 'C:/Users/sj875b/Desktop/DataAnalytics/python-challenge/PyBank/budget_data_2.csv'
csvpath2 = 'C:/Users/sj875b/Desktop/DataAnalytics/python-challenge/PyBank/budget_data_1.csv'
total_revenue = 0
dictRevenue = {}
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""



# Method 2: Improved Reading using CSV module

with open(csvpath1, newline='') as csvfile1:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader1 = csv.reader(csvfile1, delimiter=',')
   next(csvreader1,None)
   

   # Read each row of data after the header
   for row in csvreader1:
       row[0] = normalizeDate(row[0])
       #dictRevenue[row[0]] = 0
       dictRevenue[row[0]] = int(row[1])
       total_revenue = total_revenue + int(row[1])
       
#print(dictRevenue)
       
with open(csvpath2, newline='') as csvfile2:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader2 = csv.reader(csvfile2, delimiter=',')
   next(csvreader2,None)
   

   # Read each row of data after the header
   for row in csvreader2:
       row[0] = normalizeDate(row[0])
       
       dictRevenue[row[0]] += int(row[1])
       total_revenue = total_revenue + int(row[1])


for key in dictRevenue:
    if dictRevenue[key] > greatest_increase:
        greatest_increase = dictRevenue[key]
        greatest_increase_month = key

for key in dictRevenue:
    if dictRevenue[key] < greatest_decrease:
        greatest_decrease = dictRevenue[key]
        greatest_decrease_month = key      
        
print(dictRevenue) 
print("Financial Analysis")
print("------------------")
print ("Total Months " + str(len(dictRevenue)))
print ("Total Revenue $" + str(total_revenue))
print ("Greatest Increase in Revenue " + greatest_increase_month + " $" + str(greatest_increase))
print ("Greatest Decrease in Revenue " + greatest_decrease_month + " $" + str(greatest_decrease))

f = open('PyBank.txt','w')
f.write("Financial Analysis\n")
f.write("------------------\n")
f.write("Total Months " + str(len(dictRevenue))+"\n")
f.write("Total Revenue $" + str(total_revenue)+"\n")
f.write("Greatest Increase in Revenue " + greatest_increase_month + " $" + str(greatest_increase)+"\n")
f.write("Greatest Decrease in Revenue " + greatest_decrease_month + " $" + str(greatest_decrease)+"\n")
f.close()

    










