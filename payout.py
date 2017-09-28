import csv
from dateutil.parser import parse

def run():
    process_file()

def process_file():
    with open('payout.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            process_row(row)

def process_row(row):
    pass

run()
