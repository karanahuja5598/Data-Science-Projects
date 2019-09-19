#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:00:32 2019

@author: karanahuja
"""

import pandas
import matplotlib.pyplot as plt

def ward_count(df,	col,	value, unique_id, ward_num):
    '''Returns count of unique_id in	df ward_num rows w/entry value in column 
    col.'''
    rows = df[df[col] == value]
    if ward_num not in rows['Ward'].values:
        return 0
    grouped = rows.groupby('Ward')
    return grouped[unique_id].count()[ward_num]

def make_ward_dictionary(df,col,value,unique_id):
    '''Uses ward_count function to make and return dictionary whose keys are 
    ward numbers.'''
    mydict = {}
    fileref = open(df)
    df2 = pandas.read_csv(fileref)
    col2 = col
    value2 = value
    unique_id2 = unique_id
    for ward_num in range(1,51):
        mydict[ward_num] = ward_count(df2,col2,value2,unique_id2,ward_num)
    return mydict

x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5,6,7,8,9,10]
mydict2 = {}
fileref2 = open("Crimes_-_2010_to_present.csv")
df3 = pandas.read_csv(fileref2)
for ward_num in range(1,51):
        mydict2[ward_num] = ward_count(df3,'Primary Type','NARCOTICS',
               'Case Number',ward_num)

intensity = [[mydict2[1],mydict2[2],mydict2[3],mydict2[4],mydict2[5]],
             [mydict2[6],mydict2[7],mydict2[8],mydict2[9],mydict2[10]],
             [mydict2[11],mydict2[12],mydict2[13],mydict2[14],mydict2[15]],
             [mydict2[16],mydict2[17],mydict2[18],mydict2[19],mydict2[20]],
             [mydict2[21],mydict2[22],mydict2[23],mydict2[24],mydict2[25]],
             [mydict2[26],mydict2[27],mydict2[28],mydict2[29],mydict2[30]],
             [mydict2[31],mydict2[32],mydict2[33],mydict2[34],mydict2[35]],
             [mydict2[36],mydict2[37],mydict2[38],mydict2[39],mydict2[40]],
             [mydict2[41],mydict2[42],mydict2[43],mydict2[44],mydict2[45]],
             [mydict2[46],mydict2[47],mydict2[48],mydict2[49],mydict2[50]]] 

plt.figure(1)
plt.pcolor(x,y,intensity)
plt.viridis()
plt.colorbar()
plt.title('Narcotics By Ward in Chicago')
plt.xlabel('Ward Number Mod 5 on Right')

x1 = [0,1,2,3,4,5]
y1 = [0,1,2,3,4,5,6,7,8,9,10]
mydict3 = {}
fileref3 = open("311_Service_Requests_-_Vacant_and_Abandoned_Buildings_Reported.csv")
df4 = pandas.read_csv(fileref3)
for ward_num in range(1,51):
        mydict3[ward_num] = ward_count(df4,'SERVICE REQUEST TYPE',
               'Vacant/Abandoned Building','SERVICE REQUEST NUMBER',ward_num)

intensity1 = [[mydict3[1],mydict3[2],mydict3[3],mydict3[4],mydict3[5]],
             [mydict3[6],mydict3[7],mydict3[8],mydict3[9],mydict3[10]],
             [mydict3[11],mydict3[12],mydict3[13],mydict3[14],mydict3[15]],
             [mydict3[16],mydict3[17],mydict3[18],mydict3[19],mydict3[20]],
             [mydict3[21],mydict3[22],mydict3[23],mydict3[24],mydict3[25]],
             [mydict3[26],mydict3[27],mydict3[28],mydict3[29],mydict3[30]],
             [mydict3[31],mydict3[32],mydict3[33],mydict3[34],mydict3[35]],
             [mydict3[36],mydict3[37],mydict3[38],mydict3[39],mydict3[40]],
             [mydict3[41],mydict3[42],mydict3[43],mydict3[44],mydict3[45]],
             [mydict3[46],mydict3[47],mydict3[48],mydict3[49],mydict3[50]]]

plt.figure(2)
plt.pcolor(x1,y1,intensity1)
plt.viridis()
plt.colorbar()
plt.title('Vacant/Abandoned Buildings By Ward in Chicago')
plt.xlabel('Ward Number Mod 5 on Right')

narcoticslist = list(mydict2.values())

narcoticsmax = max(narcoticslist)

vacantlist = list(mydict3.values())

vacantmax = max(vacantlist)

narcoticsval = {}

vacantval = {}

for ward_num in mydict2:
    narcoticsval[ward_num] = mydict2[ward_num] / narcoticsmax
for ward_num in mydict3:
    vacantval[ward_num] = mydict3[ward_num] / vacantmax
mydict4 = {}

for ward_num in narcoticsval and vacantval:
    mydict4[ward_num] = narcoticsval[ward_num] + vacantval[ward_num]
    
x2 = [0,1,2,3,4,5]
y2 = [0,1,2,3,4,5,6,7,8,9,10]

intensity2 = [[mydict4[1],mydict4[2],mydict4[3],mydict4[4],mydict4[5]],
             [mydict4[6],mydict4[7],mydict4[8],mydict4[9],mydict4[10]],
             [mydict4[11],mydict4[12],mydict4[13],mydict4[14],mydict4[15]],
             [mydict4[16],mydict4[17],mydict4[18],mydict4[19],mydict4[20]],
             [mydict4[21],mydict4[22],mydict4[23],mydict4[24],mydict4[25]],
             [mydict4[26],mydict4[27],mydict4[28],mydict4[29],mydict4[30]],
             [mydict4[31],mydict4[32],mydict4[33],mydict4[34],mydict4[35]],
             [mydict4[36],mydict4[37],mydict4[38],mydict4[39],mydict4[40]],
             [mydict4[41],mydict4[42],mydict4[43],mydict4[44],mydict4[45]],
             [mydict4[46],mydict4[47],mydict4[48],mydict4[49],mydict4[50]]]

plt.figure(3)
plt.pcolor(x2,y2,intensity2)
plt.viridis()
plt.colorbar()
plt.title('Predictive Policing By Ward in Chicago')
plt.xlabel('Ward Number Mod 5 on Right')
