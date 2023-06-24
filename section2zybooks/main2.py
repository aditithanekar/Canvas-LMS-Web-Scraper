import math
import pandas as pd
import csv
#os library --for file input name
zybooks_csv_file = 'section2zybooks/UCRCS010CSpring2023_Program_4_report_2023-06-20_2046.csv' #exported for all sections
canvas_csv_file = 'canvasdata.csv'

zybooks_data = pd.read_csv(zybooks_csv_file, usecols=['Primary email', 'Percent grade'])
canvas_data = pd.read_csv(canvas_csv_file)

point_total = 15


def grade_calc(percent, denominator):
    return math.ceil((percent*denominator)/100)

 
# On zybook_csv there is School Email -- (netID until the @ delim)
# map it to canvas_csv file -  column with SIS Login ID
# then if key found-- then enter roundednum using grade_calc() into its columnIndex to input to 
# the only columns you'll need: from zybooks -- School Email and Percent Grade
# canvas columns you'll need: 

for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #key to check mapping
    rounded_num = 0 
    
    for zyrow in zybooks_data.itertuples():
        netid = zyrow[1].split('@',1) #getting netid from zybooks col 1(School email)
        netid = netid[0]
        
        if(str(netid).lower() == str(sisloginID).lower()):
            rounded_num = grade_calc(zyrow[2],point_total) #zybooks col 2 has percent grade
            
    #you have to change the assignment column value when you change the assignment or section-
    if(pd.isnull(canvas_data.loc[canvas_row[0], 'Program 4 (zybook) (522527)'])):
        canvas_data.loc[canvas_row[0], ['Program 4 (zybook) (522527)']] = [rounded_num] #canvas_row[0] are indices of rows
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('canvasdata.csv', index=False)