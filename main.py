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

for zybook in zybooks_files:
    challenges = re.search(r'Challenges', zybook)
    zybooks = Zybooks(zybook)

    participation_column, participation_points = zybooks.get_participation()
    challenges_column, challenges_points = zybooks.get_challenges()

    zybooks_data = pd.read_csv(zybook, usecols=['Primary email','School email', participation_column, challenges_column])
    zybooks_data = zybooks_data.rename(columns = { participation_column: "Participation", challenges_column: "Challenges" })

    reading_name = canvas.get_reading(zybooks.chapter())
    challenge_name = canvas.get_challenge(zybooks.chapter())

    zybooks_data["SIS Login ID"] = zybooks_data["School email"].str.split("@").str[0].str.lower()
    zybooks_data[reading_name] = grade_calc(zybooks_data["Participation"], participation_points)
    zybooks_data[challenge_name] = grade_calc(zybooks_data["Challenges"], challenges_points)

    if challenges is not None:
        canvas_data = canvas_data.drop([challenge_name], axis=1)
        canvas_data = pd.merge(canvas_data, zybooks_data[["SIS Login ID", challenge_name]], on="SIS Login ID")
    else:
        canvas_data = canvas_data.drop([reading_name], axis=1)
        canvas_data = pd.merge(canvas_data, zybooks_data[["SIS Login ID", reading_name]], on="SIS Login ID")

    
canvas_data.to_csv('outputs/result.csv', index=False)