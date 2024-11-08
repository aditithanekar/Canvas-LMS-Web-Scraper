import math
import pandas as pd
import re


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
    
    def participationCol(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            m = re.search(r'Participation total [(](\d+)[)].*', column)
            if m is not None:
                return m.group(0)
            
    def participationPoints(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            m = re.search(r'Participation total [(](\d+)[)].*', column)
            if m is not None:
                return m.group(1)

    def challengeCol(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            m = re.search(r'Challenge total [(](\d+)[)].*', column)
            if m is not None:
                return m.group(0)
            
    def challengePoints(self):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            m = re.search(r'Challenge total [(](\d+)[)].*', column)
            if m is not None:
                return m.group(1)

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
        result = {}
        for column in csv.columns:
            colnames = re.search(r'Lab ' + str(labchapter)+' Zybook [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
            
    def find_program(self, labchapter):
        csv = pd.read_csv(self.filename)
        result = {}
        for column in csv.columns:
            colnames = re.search(r'Program ' + str(labchapter)+' Zybook [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
        
    def find_reading(self, labchapter):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            colnames = re.search(r'Chapter ' + str(labchapter)+' Readings [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
            
    def find_challenge(self, labchapter):
        csv = pd.read_csv(self.filename)
        for column in csv.columns:
            colnames = re.search(r'Chapter ' + str(labchapter)+' Challenges [(](\d+)[)].*', column)
            if colnames is not None:
                return colnames.group(0)
        


#os library --for file input name
zybooks_csv_file = 'ch10.csv' #change filename to zybooks csv report export
canvas_csv_file = 'canvasdata.csv' #change this filename to the canvas file you're inputting to

zybooks = zybookDownload(zybooks_csv_file)
canvas = canvasGradebook(canvas_csv_file)


zybooks_data = pd.read_csv(zybooks_csv_file, usecols=['Primary email','School email', zybooks.participationCol(), zybooks.challengeCol()]) #take only necessary cols
canvas_data = pd.read_csv(canvas_csv_file)

reading_total = int(zybooks.participationPoints())
challenge_total = int(zybooks.challengePoints())

print(zybooks.participationCol())
print(zybooks.challengeCol())
print(reading_total)
print(challenge_total)

reading_name = canvas.find_reading(zybooks.chapter())
challenge_name = canvas.find_challenge(zybooks.chapter())

print(reading_name)
print(challenge_name)

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
        

        if(netid=='devin.phung'):
            netid = netid.replace('devin.phung', 'dphun009')
        elif(netid=='jpate'):
            netid = netid.replace('jpate', 'jpate135')
        
        #print(netid)
        if(str(netid).lower() == str(sisloginID).lower()):
            reading_points = grade_calc(zyrow[3],reading_total)
            challenge_points = grade_calc(zyrow[4], challenge_total)
            #grade_calc(zyrow[3],point_total) #zybooks col 2 has percent grade
            
            
    #you have to change the assignment column value when you change the assignment or section-
    reading_name = canvas.find_reading(zybooks.chapter())
    challenge_name = canvas.find_challenge(zybooks.chapter())
    #if(pd.isnull(canvas_data.loc[canvas_row[0], reading_name])):
    canvas_data.loc[canvas_row[0], [reading_name]] = [reading_points] #canvas_row[0] are indices of rows
    print("read")

    #if(pd.isnull(canvas_data.loc[canvas_row[0], challenge_name])):
    canvas_data.loc[canvas_row[0], [challenge_name]] = [challenge_points] #canvas_row[0] are indices of rows
    print("hi")
    
#this is what's there for export after the changes have been made
canvas_data.to_csv('canvasdata.csv', index=False)