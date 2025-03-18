import pandas as pd
import re


class Zybooks:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)   

    def get_df(self):
        return self.df
        
    def chapter(self):
        columns = ['Primary email','School email', self._get_zybooks_column()]
        for column in self.df[columns]:
            m = re.search(r'(\d+)[.](\d+).*', column)
            if m is not None:
                return int(m.group(1))
        raise RuntimeError("Not Found")
    
    def _get_zybooks_column(self):
        for column in self.df.columns:
            m = re.search(r'(\d+)[.](\d+).*', column)
            if m is not None:
                return m.group(0)
        raise RuntimeError("Not Found")
    
    def get_participation(self):
        for column in self.df.columns:
            m = re.search(r'Points earned \(out of (\d+)\)', column)

            if m is not None:
                return (m.group(0), int(m.group(1)))

    def get_challenges(self):
        for column in self.df.columns:
            m = re.search(r'Points earned \(out of (\d+)\)', column)

            if m is not None:
                return (m.group(0), int(m.group(1)))

