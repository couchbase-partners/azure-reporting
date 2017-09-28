import os
import csv

def run():
    filenames=get_filenames()
    for filename in filenames:
        #[hourly, byol, legacy] =
        x=process_file(filename)
        print(str(x))

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

def process_file(filename):
    hourly=0
    byol=0
    legacy=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'VM Image' in row['OfferType']:
                date = ['UsageStartDate']
                if 'silver_support' in row['ServicePlanName'] or 'hourly_pricing' in row['ServicePlanName']:
                    hourly+=float(row['Usage'])
                elif 'byol' in row['ServicePlanName']:
                    byol+=float(row['Usage'])
                else:
                    legacy+=float(row['Usage'])

    return [hourly, byol, legacy]

run()
