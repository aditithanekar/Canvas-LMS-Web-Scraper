# Canvas-LMS-Web-Scraper
I made these to facilitate grade input from Zybooks, Gradescope, as well as Google Sheets!
I used this to grade for 3 sections of CS010C at UCR. :)

### How to use mainzybook.py 
This takes in a csv file from zybooks -- you can use the reporting feature on Zybooks to download a report of the class as a .csv file. You also need to "Export Entire Gradebook" for sections on Canvas, and it will download a .csv file for the canvas section. 
It maps an SISLoginID on Canvas to the netid preceding the @ delimiter on the School Email column to find the student.

All you need to do:
1. Change the filepath of the Canvas .csv file
2. Change the filepath of the Zybooks .csv file
3. Change the point total as needed
4. Change the assignment name to the specific column from the Canvas .csv file you want to input into--
5. Then run it!
6. Your results will generate a file called canvasdata.csv
7. To put it back into canvas, you can click "Import" in the gradebook, and then upload the canvasdata.csv file you created, and it should fill in all the grades you just mapped in!

### Using attendance.py

### Using ceilmidterm.py
### Using gradescope.py
