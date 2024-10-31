import pandas as pd
import re
class zybookDownload:
    def __init__(self, filename):
        self.filename=filename        
        
    def chapter(self):
        csv = pd.read_csv(self.filename)
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
        
        
if __name__ == '__main__':
    chap1download = zybookDownload('UCRCS010CMillerWinter2024_report_2024-01-22_1514_PST.csv')
    canvas_csv = canvasGradebook('2024-01-22T1606_Grades-CS_010C_001_24W.csv')
    
    #print(canvas_csv.list_labs())
    #print(chap1download.filename)
    print(type(chap1download.zybooksCol()))
    #print(chap1download.chapter())
    #print(chap1download.participation())
    #print(chap1download.point_total())
    
    
        
        