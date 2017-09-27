import os
import csv

def run():
    filenames=get_filenames()
    print(filenames)

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

run()
