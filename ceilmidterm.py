import math
import pandas as pd
import csv

canvas_csv_file = 'section2zybooks/2023-06-20T2232_Grades-CS_010C_002_23S.csv' #edit with Canvas csv filename
canvas_data = pd.read_csv(canvas_csv_file)

def grade_calc(rawScore):
    return math.ceil(rawScore)

for canvas_row in canvas_data.itertuples():
    rounded_num = 0 
    canvas_target_column = 'Midterm (541965)' #edit with column name of assignment in Canvas
           
    if (canvas_data.loc[canvas_row[0]][canvas_target_column]) != 'Manual Posting':
        if not (pd.isnull(canvas_data.loc[canvas_row[0]][canvas_target_column])):
            rounded_num = grade_calc(float(canvas_data.loc[canvas_row[0]][canvas_target_column]))
            print(rounded_num)
            canvas_data.loc[canvas_row[0], [canvas_target_column]] = [rounded_num]
        
canvas_data.to_csv('canvasdata.csv', index=False)