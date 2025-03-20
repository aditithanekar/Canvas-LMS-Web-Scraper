import pandas as pd
import re

class Zybooks:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.output = self.df[["Primary email", "School email"]].copy()
        self.output["SIS User ID"] = self.output["School email"].fillna(self.output["Primary email"]).str.split("@").str[0].str.lower()
        self.output.drop(columns=["Primary email", "School email"], inplace=True)

        # Manual Data Cleaning
        self.output.loc[self.output['SIS User ID'] == 'aparna.petluri', 'SIS User ID'] = 'apetl004'
        self.output.loc[self.output['SIS User ID'] == 'iancatren', 'SIS User ID'] = 'icatr001'

    
    def _aggregate(self, type, include, double, names):
        groups = {}
        sections = {}

        pattern = fr'^\d+\.\d+ - {type} \(\d+\)$'
        columns = [col for col in self.df.columns if re.match(pattern, col)]

        for column in columns:
            chapter = int(column.split(".")[0])
            section = int(column.split(".")[1].split(" ")[0])
            points = int(column.split("(")[1].replace(")", ""))

            if section in include[chapter]:
                scalar = 2 if section in double[chapter] else 1

                if chapter in groups:
                    groups[chapter] += points * scalar
                    sections[chapter].append(str(section))
                else:
                    groups[chapter] = points   
                    sections[chapter] = [str(section)]

        for chapter in groups:
            self.output[names[chapter - 1]] = (self.df.filter(regex=fr'^{chapter}\.({"|".join(sections[chapter])}) - {type} \(\d+\)$') / 100).sum(axis = 1) / len(sections[chapter]) * groups[chapter]

    def participation(self, columns):
        include = {
            1: set([1, 2, 3, 4, 5, 6, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
            2: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
            3: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14]),
            4: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            5: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
            6: set([1, 2, 3, 4, 5]),
            7: set([1, 2, 3, 4, 5, 6, 7, 8]),
            8: set([2, 3, 4, 5, 6, 7, 8, 9, 10]),
            9: set([1, 2, 3, 4, 5, 6]),
            10: set([1, 2, 3])
        }

        double = {
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set([2]),
            6: set(),
            7: set(),
            8: set(),
            9: set(),
            10: set()
        }

        self._aggregate("Participation", include, double, columns)

    def challenges(self, columns):
        include = {
            1: set([1, 3, 9, 13, 15, 18, 19, 20, 21, 22, 24]),
            2: set([2, 11, 12, 13, 14, 15, 16]),
            3: set([1, 2, 4, 5, 7, 8, 9, 11]),
            4: set([1, 3, 4, 5, 6]),
            5: set([1, 2, 3, 4, 6, 7, 8, 9, 10, 11]),
            6: set([2, 3, 4, 5]),
            7: set([1, 2, 3, 5, 6, 7]),
            8: set([2, 3, 4, 5, 9]),
            9: set([3, 4, 5, 6]),
            10: set([1, 2, 3])
        }

        double = { key: set() for key in range(1, 11) }

        self._aggregate("Challenge", include, double, columns)
