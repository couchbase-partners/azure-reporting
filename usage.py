import os
import csv
from dateutil.parser import parse

usage={}

def run():
    filenames=get_filenames()
    for filename in filenames:
        process_file(filename)
    print_usage()

def get_filenames():
    filenames=[]
    for file in os.listdir("./usage"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./usage", file))
    return filenames

def process_file(filename):
    hourly=0
    byol=0
    legacy=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            process_row(row)

def process_row(row):
    if 'VM Image' in row['OfferType']:
        date = parse(row['UsageStartDate'])
        date = str(date.month) + '/1/' + str(date.year)

        if not date in usage:
            usage[date]={}
            usage[date]['hourly']=0
            usage[date]['byol']=0
            usage[date]['legacy']=0

        if 'silver_support' in row['ServicePlanName'] or 'hourly_pricing' in row['ServicePlanName']:
            usage[date]['hourly']+=float(row['Usage'])
        elif 'byol' in row['ServicePlanName']:
            usage[date]['byol']+=float(row['Usage'])
        else:
            usage[date]['legacy']+=float(row['Usage'])

def print_usage():
    print('Date, Hourly Pricing Usage, BYOL Usage, Legacy Usage, Total Usage')
    for date in usage:
        total = usage[date]['hourly']+usage[date]['byol']+usage[date]['legacy']
        print(date + ', ' + str(usage[date]['hourly']) + ', ' + str(usage[date]['byol']) + ', ' + str(usage[date]['legacy']) + ', ' + str(total))

run()
