import pandas as pd
import re

class Canvas:
    def __init__(self, filename):
        self.df = pd.read_csv(filename) 
