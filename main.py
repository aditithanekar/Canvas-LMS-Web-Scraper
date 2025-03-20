import pandas as pd
from zybooks import Zybooks 
from canvas import Canvas 
import glob


zybooks_files = glob.glob("zybooks/*")

if len(zybooks_files) != 1:
    raise Exception("Zybooks Folder must have exactly 1 file.")

canvas_files = glob.glob("canvas/*")

if len(canvas_files) != 1:
    raise Exception("Canvas Folder must have exactly 1 file.")

canvas = Canvas(canvas_files[0])
reading_columns = canvas.df.filter(regex=fr'Chapter \d+ Readings \(\d+\)').fillna(0).columns
challenge_columns = canvas.df.filter(regex=fr'Chapter \d+ Challenges \(\d+\)').fillna(0).columns

zybooks = Zybooks(zybooks_files[0])
zybooks.participation(reading_columns)
zybooks.challenges(challenge_columns)

merge = pd.merge(canvas.df, zybooks.output, on="SIS User ID", how="left")

merge.filter(regex=fr'_y|_x').fillna(0).columns

for column in merge.filter(regex=fr'_y|_x').fillna(0).columns:
    merge[column.replace("_x", "").replace("_y", "")] = merge[column]
    merge.drop(columns=[column], inplace=True)

merge.to_csv('outputs/result.csv', index=False)