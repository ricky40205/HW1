# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '107011229.csv'
#cwb_filename = 'sample_input.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
target_data1 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
target_data2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
target_data3 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
target_data4 = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

#target_data = data[1]


#=======================================


# Part. 4

#=======================================0
ans = []
# Print result
x=len(target_data)

a=float(target_data[0]['TEMP'])
for i in range(x):
    #print(target_data[i]['TEMP'])
    
    if(a<float(target_data[i]['TEMP'])):
        a=float(target_data[i]['TEMP'])
    

if(a==(-99 or -999)): 
    a='NONE'

ans.append(['C0R190', a])
#=======================================1
x=len(target_data1)

a=float(target_data1[0]['TEMP'])
for i in range(x):
    #print(target_data1[i]['TEMP'])
    
    if(a<float(target_data1[i]['TEMP'])):
        a=float(target_data1[i]['TEMP'])


if(a==(-99 or -999)): 
    a='NONE'

ans.append(['C0A880', a])
#=======================================2
x=len(target_data2)

a=float(target_data2[0]['TEMP'])
for i in range(x):
    #print(target_data2[i]['TEMP'])
    
    if(a<float(target_data2[i]['TEMP'])):
        a=float(target_data2[i]['TEMP'])


if(a==(-99 or -999)): 
    a='NONE'

ans.append(['C0F9A0', a])
#=======================================3
x=len(target_data3)

a=float(target_data3[0]['TEMP'])
for i in range(x):
    #print(target_data3[i]['TEMP'])
    
    if(a<float(target_data3[i]['TEMP'])):
        a=float(target_data3[i]['TEMP'])
    


if(a==(-99 or -999)): 
    a='NONE'

ans.append(['C0G640', a])
#=======================================4
x=len(target_data4)

a=float(target_data4[0]['TEMP'])
for i in range(x):
    #print(target_data4[i]['TEMP'])
    
    if(a<float(target_data4[i]['TEMP'])):
        a=float(target_data4[i]['TEMP'])
    


if(a==(-99 or -999)): 
    a='NONE'


ans.append(['C0X260', a])
#=========print==result===================


print(ans)