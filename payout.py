import csv
from dateutil.parser import parse

revenue={}

def run():
    process_file()
    print_revenue()

def process_file():
    with open('payout.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            update_revenue(row)

def update_revenue(row):
    date = row['Order Purchase Date']
    if date:
        date = date.split(' ')[0]
        date = parse(date)
        date = str(date.month) + '/1/' + str(date.year)
    else:
        date = '1/1/1'

    if not date in revenue:
        revenue[date]={}
        revenue[date]['revenue']=0
        revenue[date]['legacyrevenue']=0

    if 'Hourly Pricing' in row['SKU']:
        revenue[date]['revenue']+=float(row['Payout Amount (PC)'])
    else:
        revenue[date]['legacyrevenue']+=float(row['Payout Amount (PC)'])

def print_revenue():
    print('Month, Revenue, Legacy Revenue, Total Revenue')
    for date in revenue:
        total = revenue[date]['revenue']+revenue[date]['legacyrevenue']
        print(date + ', ' + str(revenue[date]['revenue']) + ', ' + str(revenue[date]['legacyrevenue']) + ', ' + str(total))

run()
