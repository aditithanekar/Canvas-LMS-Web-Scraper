# Canvas-LMS-Web-Scraper
I made these to facilitate grade input from Zybooks, Gradescope, as well as Google Sheets!

I used this to grade for 3 sections of CS010C at UCR, but they can truly be used for anything! :) Feel free to use these as a template if you are grading, or trying to input data from one .csv to another .csv file, by mapping a specific id. 

The script now uses regex, which specifically looks for the reading and challenges columns, so all you have to do it change 2 lines of code :)

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

## How to use winterparticipation.py (Zybook to Canvas)
This takes in a .csv file from Zybooks -- you can use the reporting feature on Zybooks to download a report of the class as a .csv file. You also need to "Export Entire Gradebook" for sections on Canvas, and it will download a .csv file for the canvas section. 
It maps an SISLoginID on Canvas to the netid preceding the @ delimiter on the School Email column to find the student.

All you need to do:
1. Change the filepath of the Canvas .csv file(canvas_csv_file)
2. Change the filepath of the Zybooks .csv file(zybooks_csv_file)
3. Then run it!
4. Your results will generate a file called canvasdata.csv
5. To put it back into Canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!

* Pro Tip: If you want to write multiple Zybooks exports to the same Canvas just set the canvas_csv_file input filepath to be the previous output export canvasdata.csv. So it can overwrite the file you've already written to, and edit a new column. 

```
canvas_csv_file = 'canvasdata.csv' 
```

# Questions?
Feel free to reach out to Aditi Thanekar  :) 
athan014@ucr.edu


