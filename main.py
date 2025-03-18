import pandas as pd
from zybooks import Zybooks 
from canvas import Canvas 
import glob
import re

def grade_calc(column, points):
    return (column / 100 ) * points

zybooks_files = glob.glob("zybooks/*")

if len(zybooks_files) == 0:
    raise Exception("Zybooks Folder must not be empty.")

canvas_files = glob.glob("canvas/*")

if len(canvas_files) != 1:
    raise Exception("Canvas Folder must have exactly 1 file.")

canvas = Canvas(canvas_files[0])
canvas_data = canvas.get_df()

# canvas_data["Chapter 1 Readings (795699)"] = 0
# canvas_data["Chapter 1 Challenges (795698)"] = 0
canvas_data["Chapter 2 Readings (795703)"] = 0
# canvas_data["Chapter 2 Challenges (795702)"] = 0
canvas_data["Chapter 3 Readings (795705)"] = 0
# canvas_data["Chapter 3 Challenges (795704)"] = 0
canvas_data["Chapter 4 Readings (795707)"] = 0
# canvas_data["Chapter 4 Challenges (795706)"] = 0
canvas_data["Chapter 5 Readings (795709)"] = 0
canvas_data["Chapter 5 Challenges (795708)"] = 0
canvas_data["Chapter 6 Readings (795711)"] = 0
canvas_data["Chapter 6 Challenges (795710)"] = 0
canvas_data["Chapter 7 Readings (795713)"] = 0
canvas_data["Chapter 7 Challenges (795712)"] = 0
canvas_data["Chapter 8 Readings (795715)"] = 0
canvas_data["Chapter 8 Challenges (795714)"] = 0
canvas_data["Chapter 9 Readings (795717)"] = 0
canvas_data["Chapter 9 Challenges (795716)"] = 0
canvas_data["Chapter 10 Readings (795701)"] = 0
canvas_data["Chapter 10 Challenges (795700)"] = 0

for zybook in zybooks_files:

    challenges = re.search(r'Challenges', zybook)
    zybooks = Zybooks(zybook)

    participation_column, participation_points = zybooks.get_participation()
    challenges_column, challenges_points = zybooks.get_challenges()

    zybooks_data = pd.read_csv(zybook, usecols=['Primary email','School email', participation_column, challenges_column])

    reading_name = canvas.get_reading(zybooks.chapter())
    challenge_name = canvas.get_challenge(zybooks.chapter())

    zybooks_data["SIS Login ID"] = zybooks_data["School email"].str.split("@").str[0].str.lower()

    zybooks_data[reading_name] = zybooks_data[participation_column]
    zybooks_data[challenge_name] = zybooks_data[challenges_column]

    if challenges is not None:
        merge = pd.merge(canvas_data[["SIS Login ID", reading_name]], zybooks_data[["SIS Login ID", challenge_name]], on="SIS Login ID", suffixes=('_df1', '_df2'), how="left")

        merge[f"{challenge_name}_df1"] = pd.to_numeric(merge[f"{challenge_name}_df1"], errors="coerce").fillna(0)
        merge[f"{challenge_name}_df2"] = pd.to_numeric(merge[f"{challenge_name}_df2"], errors="coerce").fillna(0)

        canvas_data[challenge_name] = merge[f"{challenge_name}_df1"] + merge[f"{challenge_name}_df2"]
    else:
        merge = pd.merge(canvas_data[["SIS Login ID", reading_name]], zybooks_data[["SIS Login ID", reading_name]], on="SIS Login ID", suffixes=('_df1', '_df2'), how="left")

        merge[f"{reading_name}_df1"] = pd.to_numeric(merge[f"{reading_name}_df1"], errors="coerce").fillna(0)
        merge[f"{reading_name}_df2"] = pd.to_numeric(merge[f"{reading_name}_df2"], errors="coerce").fillna(0)

        canvas_data[reading_name] = merge[f"{reading_name}_df1"] + merge[f"{reading_name}_df2"]
    
canvas_data.to_csv('outputs/result.csv', index=False)