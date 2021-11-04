# convert-XLSX-to-CSV
this is how to convert multiple xlsx files to csv in python using pandas <br /> 
From the automate the boring stuff with python, I wanted to try and use pandas.<br /> 
This takes all the xlsx files from the current directory and places them into a new directory(folder) called converted.<br /> 
Keeping shutil.move and trying to run the program a second time will give an error saying that the file already exists.<br /> 
if you wanna replace the files without an error, uncomment the shutil.copy line and comment the shutil.move line :)
