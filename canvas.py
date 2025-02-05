import pandas as pd
import re

class Canvas:
    def __init__(self, filename):
        self.df = pd.read_csv(filename) 

    def get_df(self):
        return self.df
    
    def list_labs(self):
        for column in self.df.columns:
            matches = re.search(r'Lab [(\d+)] Zybook [(](\d+)[)].*', column)
            if matches is not None:
                return matches.group(0)
          
    def get_lab(self, chapter):
        for column in self.df.columns:
            matches = re.search(r'Lab ' + str(chapter)+' Zybook [(](\d+)[)].*', column)
            if matches is not None:
                return matches.group(0)
            
    def get_program(self, chapter):
        for column in self.df.columns:
            matches = re.search(r'Program ' + str(chapter)+' Zybook [(](\d+)[)].*', column)
            if matches is not None:
                return matches.group(0)
        
    def get_reading(self, chapter):
        for column in self.df.columns:
            matches = re.search(r'Chapter ' + str(chapter)+' Readings [(](\d+)[)].*', column)
            if matches is not None:
                return matches.group(0)
            
    def get_challenge(self, chapter):
        for column in self.df.columns:
            matches = re.search(r'Chapter ' + str(chapter)+' Challenges [(](\d+)[)].*', column)
            if matches is not None:
                return matches.group(0)
        
