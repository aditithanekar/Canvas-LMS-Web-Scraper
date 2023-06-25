import math
import pandas as pd
import csv

gradescope_csv_file = 'gradescope/lab2Manual_grade.csv' #change filename based on export csv
canvas_csv_file = 'gradescope/2023-05-01T0155_Grades-CS_010C_003_23S.csv' #change filename based on section

gradescope_data = pd.read_csv(gradescope_csv_file, usecols=['Email', 'Score']) # use only necessary cols
canvas_data = pd.read_csv(canvas_csv_file)

for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #key to check mapping
    rounded_num = 0 
    
    for gsrow in gradescope_data.itertuples():
        if(isinstance(gsrow[1],str)):
            netid = gsrow[1].split('@',1) #getting netid from zybooks col 1(School email)
            netid = netid[0]
        
        if(str(netid).lower() == str(sisloginID).lower()):
            print(gsrow[2])
            rounded_num = gsrow[2] #gradescope col 2 has score points
            
    #you have to change the assignment column value when you change the assignment or section-
    canvas_data.loc[canvas_row[0], ['Lab 2 (quality)  (516533)']] = [rounded_num] #canvas_row[0] are indices
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('labquality.csv', index=False)
