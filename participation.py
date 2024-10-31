import math
import pandas as pd

#os library --for file input name
zybooks_csv_file = 'UCRCS010CMillerFall2023_report_2023-12-15_1217_PST.csv' #change filename to zybooks csv report export
canvas_csv_file = 'canvasdata.csv' #change this filename to the canvas file you're inputting to

zybooks_data = pd.read_csv(zybooks_csv_file, usecols=['Primary email','School email', 'Participation total (117)', 'Challenge total (20)']) #take only necessary cols
canvas_data = pd.read_csv(canvas_csv_file)

reading_total = 117
challenge_total = 20

def grade_calc(percent, denominator):
    return math.ceil((percent*denominator)/100)


for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #key to check mapping
    reading_points = 0 
    challenge_points = 0
    
    for zyrow in zybooks_data.itertuples():
        
        netid = str(zyrow[2]).split('@',1) #getting netid from zybooks col 1(School email)
        #print(str(zyrow[1]))
        if(netid[0] == "nan"):
            netid = str(zyrow[1]).split('@',1) # if null, use Primary email col
        netid = netid[0]
        

        if(netid=='benjamin.nguyen004'):
            netid = netid.replace('benjamin.nguyen004', 'bnguy280')
        elif(netid=='kaylatran201'):
            netid = netid.replace('kaylatran201', 'ktran369')
        
        #print(netid)
        if(str(netid).lower() == str(sisloginID).lower()):
            reading_points = grade_calc(zyrow[3],reading_total)
            challenge_points = grade_calc(zyrow[4], challenge_total)
            #print(reading_points)
            #grade_calc(zyrow[3],point_total) #zybooks col 2 has percent grade
            
            
    #you have to change the assignment column value when you change the assignment or section-
    reading_name = 'Chapter 8 Readings (619603)'
    challenge_name = 'Chapter 8 Challenges (619604)'
    if(pd.isnull(canvas_data.loc[canvas_row[0], reading_name])):
        canvas_data.loc[canvas_row[0], [reading_name]] = [reading_points] #canvas_row[0] are indices of rows
        print("read")

    if(pd.isnull(canvas_data.loc[canvas_row[0], challenge_name])):
        canvas_data.loc[canvas_row[0], [challenge_name]] = [challenge_points] #canvas_row[0] are indices of rows
        print("hi")
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('canvasdata.csv', index=False)