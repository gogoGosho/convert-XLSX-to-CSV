import os, glob, shutil
import pandas as pd


current = os.getcwd()

for file in glob.glob("*.xlsx"):
    base = os.path.splitext(file)[0]
    df = pd.read_excel(file)
    df.to_csv(base + ".csv", index=False)
for csvFile in glob.glob("*.csv"):
    shutil.move(csvFile, "./converted")
    # shutil.copy(csvFile, "./converted") #if you want to replace files use this, the line one top will
    # give and error if a file with that name already exists
