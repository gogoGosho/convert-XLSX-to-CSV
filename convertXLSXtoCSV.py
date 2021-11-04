import os, glob, shutil
import pandas as pd
from pathlib import Path

current = os.getcwd()
dest = Path("./converted")
supaa = os.path.join(current, "./converted")

for file in glob.glob("*.xlsx"):
    base = os.path.splitext(file)[0]
    df = pd.read_excel(file)
    df.to_csv(base + ".csv", index=False)
for csvFile in glob.glob("*.csv"):
    shutil.move(csvFile, "./converted")
