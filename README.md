# Canvas-LMS-Web-Scraper
I made these to facilitate grade input from Zybooks, Gradescope, as well as Google Sheets!
I used this to grade for 3 sections of CS010C at UCR, but they can truly be used for anything! :) Feel free to use these as a template if you are grading, or trying to input data from one .csv to another .csv file, by mapping a specific id. 

### Setup and Installation
1. First, check if you have [Python](https://www.python.org/downloads/) installed on your computer
2. Once you have Python or Python3, you will need some packages.
   
Go into the Terminal or Command Prompt and type the following
```
pip install pandas
pip install math
```
OR if it did not work, and you are using Python3, try these commands
```
pip3 install pandas
pip3 install math
```

## How to use mainzybook.py (Zybook to Canvas)
This takes in a csv file from zybooks -- you can use the reporting feature on Zybooks to download a report of the class as a .csv file. You also need to "Export Entire Gradebook" for sections on Canvas, and it will download a .csv file for the canvas section. 
It maps an SISLoginID on Canvas to the netid preceding the @ delimiter on the School Email column to find the student.

All you need to do:
1. Change the filepath of the Canvas .csv file(canvas_csv_file)
2. Change the filepath of the Zybooks .csv file(zybooks_csv_file)
3. Change the point total as needed(point_total)
4. Change the assignment name to the specific column from the Canvas .csv file you want to input into--
5. Then run it!
6. Your results will generate a file called canvasdata.csv
7. To put it back into Canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!

## Using attendance.py (Google Sheets to Canvas)
To export the Google Sheet properly, click File-> Download-> Comma Separated Values(.csv)
Then export your Canvas file as described in mainzybook.py's usage.

Now:
1. Change the filepath of the Canvas .csv file(canvas_csv_file)
2. Change the filepath of the Google Sheets .csv file (sheets_csv_file)
3. Change the assignment name to the specific column from the Canvas .csv file you want to input into--
4. Then run it!
5. Your results will generate a file called demodata.csv
6. To put it back into Canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!

## Using ceilmidterm.py (Canvas to Canvas)
All you need to do:

1. Change the filepath of the Canvas .csv file(canvas_csv_file)
2. Change the canvas_target_col value to the assignment name's column in Canvas
3. Run it!
4. Your results will generate a file called canvasdata.csv
5. To put it back into Canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!

## Using gradescope.py (Gradescope to Canvas)
After using this for a couple assignments I realized that I didn't need it because Gradescope has a button that can publish grades to Canvas, which is super cool!

Regardless, if you end up using this...first export both the Canvas gradebook as well as a Gradescope file as .csv

Then: 
1. Change the filepath of the Canvas .csv file(canvas_csv_file)
2. Change the filepath of the Gradescope .csv file(gradescope_csv_file)
3. Change the assignment column name from Canvas which is your destination to map to
4. Now run it, and you will generate a labquality.csv file
5. To put it back into Canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!
