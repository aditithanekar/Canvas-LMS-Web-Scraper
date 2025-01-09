import re
import math
import pandas as pd

class zybookDownload:
    def __init__(self, filename):
        self.filename=filename        
        
    def chapter(self):
        zybooks_col = self.zybooksCol()
        cols_to_read = ['Primary email','School email', zybooks_col]
        csv = pd.read_csv(self.filename, usecols=cols_to_read)
        for column in csv.columns:
            m = re.search(r'(\d+)[.](\d+).*', column)
            if m is not None:
                #print(m.group(0))
                return int(m.group(1))
        raise RuntimeError("not found")
    
    def zybooksCol(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            m = re.search(r'(\d+)[.](\d+).*', column)
            if m is not None:
                return m.group(0)
        raise RuntimeError("not found")
    
    def participation(self):
        csv = pd.read_csv(self.filename)
        result = {}
        for column in csv.columns:
            m = re.search(r'(\d+)[.](\d+) - Participation [(](\d+)[)].*', column)
            if m is not None:
                result[int(m.group(2))] = int(m.group(3))
                
        return result
    
    def point_total(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            colnames = re.search(r'Lab total [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(1)


class canvasGradebook:
    def __init__(self, filename):
        self.filename=filename   
    
    def list_labs(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            colnames = re.search(r'Lab [(\d+)] Zybook [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
          
    def find_lab(self, labchapter):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            colnames = re.search(r'\[zyBooks\] LAB ' + str(labchapter)+': .*', column)
            # colnames = re.search(r'Lab ' + str(labchapter)+' Zybook [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
            
    def find_program(self, labchapter):
        csv = pd.read_csv(self.filename)
        result = {}
        for column in csv.columns:
            colnames = re.search(r'\[zyBooks\] PROGRAM ' + str(labchapter)+': .*', column)
            if colnames is not None:
                return colnames.group(0)
        


#os library --for file input name

zybooks_csv_file = 'prog4-617.csv' #change filename to zybooks csv report export
canvas_csv_file = 'canvasdata.csv' #change this filename to the canvas file you're inputting to
zybooks = zybookDownload(zybooks_csv_file)
canvas = canvasGradebook(canvas_csv_file)

zybooks_col = zybooks.zybooksCol()
print(zybooks_col)
print(zybooks.chapter())

canvas_col_name = canvas.find_program(4)
#canvas_col_name = canvas.find_lab(zybooks.chapter())
#canvas_col_name = "PROGRAM 1: Josephus Problem (690728)"
print(canvas_col_name)
cols_to_read = ['Primary email','School email', zybooks_col]
print(cols_to_read)

zybooks_data = pd.read_csv(zybooks_csv_file, usecols=cols_to_read) #take only necessary cols
zybooks_data = zybooks_data[cols_to_read]
canvas_data = pd.read_csv(canvas_csv_file)

point_total = 10

def grade_calc(percent, denominator):
    return math.ceil((percent*denominator)/100)


for canvas_row in canvas_data.itertuples():
    sisloginID = canvas_row[3] #key to check mapping
    rounded_num = 0 
    
    for zyrow in zybooks_data.itertuples():
        
        netid = str(zyrow[2]).split('@',1) #getting netid from zybooks col 1(School email)
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
            
            
    #you have to change the assignment column value when you change the assignment or section-
 
    #if(pd.isnull(canvas_data.loc[canvas_row[0], lab6])):
    canvas_data.loc[canvas_row[0], [canvas_col_name]] = [rounded_num] #canvas_row[0] are indices of rows
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('canvasdata.csv', index=False)