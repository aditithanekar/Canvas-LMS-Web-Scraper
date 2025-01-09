import math
import pandas as pd

#os library --for file input name
zybooks_csv_file = 'UCRCS010CMillerFall2024_report_2024-10-31_0012_PDT.csv' #change filename to zybooks csv report export
canvas_csv_file = '2024-10-31T0014_Grades-CS_010C_001_24F.csv' #change this filename to the canvas file you're inputting to

zybooks_data = pd.read_csv(zybooks_csv_file, usecols=['Primary email','School email', '2.28 - Lab (10)']) #take only necessary cols
canvas_data = pd.read_csv(canvas_csv_file)

point_total = 10

def grade_calc(percent, denominator):
    return math.ceil((percent*denominator)/100)


for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #key to check mapping
    rounded_num = 0 
    #num2 = 0
    
    for zyrow in zybooks_data.itertuples():
        
        netid = str(zyrow[2]).split('@',1) #getting netid from zybooks col 1(School email)
        #print(str(zyrow[1]))
        if(netid[0] == "nan"):
            netid = str(zyrow[1]).split('@',1) # if null, use Primary email col
        netid = netid[0]
        
        # how to take care of data that is unclean manually:
        # if(netid=='emailaddressbefore the @ sign if it is a non netid address'):
        #     netid = netid.replace('the non-netid email address', 'netid')
        
        print(netid)
        if(str(netid).lower() == str(sisloginID).lower()):
            if(pd.isnull(zyrow[3])):
                rounded_num=0
            else:
                rounded_num = grade_calc(zyrow[3],point_total) #zybooks col 2 has percent grade
            #num2 = grade_calc(zyrow[4],point_total)
            
            
    #you have to change the assignment column value when you change the assignment or section-
    #section 1lab5 = 'Lab 5 Zybook (610485)' Lab 7 Zybook (619232),Lab 8 Zybook (619233),Lab 9 Zybook (619234),Program 3 Zybook (619235),Program 4 Zybook (619236),Program 2 Zybook (619237)
    
    #section 2: Lab 5 Zybook (610487),Lab 6 Zybook  (610488),Lab 7 Zybook (619238),Lab 8 Zybook (619239),Lab 9 Zybook (619240),Program 3 Zybook (619241),Program 4 Zybook (619242),Program 2 Zybook (619243)
    
    lab6 ='Program 1 Zybook (619610)'
    #if(pd.isnull(canvas_data.loc[canvas_row[0], lab6])):
    canvas_data.loc[canvas_row[0], [lab6]] = [rounded_num] #canvas_row[0] are indices of rows
    #if(pd.isnull(canvas_data.loc[canvas_row[0], lab6])):
    #canvas_data.loc[canvas_row[0], [lab6]] = [num2]
#this is what's there for export after the changes have been made
canvas_data.to_csv('canvasdata.csv', index=False)