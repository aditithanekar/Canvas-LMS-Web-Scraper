import math
import pandas as pd
import csv

sheets_csv_file = 'attendance-demos/CS010C 23S Week1 (Responses) - Form Responses 1 (3).csv' #exported for all sections
canvas_csv_file = 'demodata.csv'

sheets_data = pd.read_csv(sheets_csv_file, usecols=["NetID (Your R'Web Username)", 'Lab9 Demo']) #use only necessary columns
canvas_data = pd.read_csv(canvas_csv_file)



for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #sisLoginID is netid in canvas (key to map)
    rounded_num = 0
    
    for sheet_row in sheets_data.itertuples():
        netid = sheet_row[1].split('@',1) #getting netid from zybooks col 1(School email)
        netid = netid[0]
        
        if(str(netid).lower() == str(sisloginID).lower()):
            rounded_num = sheet_row[2] # col 2 has point value
            
    #you have to change the assignment column value when you change the assignment or section-
    if(rounded_num!=0):
        if(pd.isnull(canvas_data.loc[canvas_row[0], 'Lab 9 (demo) (541984)'])):
            canvas_data.loc[canvas_row[0], ['Lab 9 (demo) (541984)']] = [rounded_num] #canvas_row[0] are indices
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('demodata.csv', index=False)
