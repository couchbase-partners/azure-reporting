# azure-reporting
These are scripts to crunch Azure reports.  

## Usage
To run the usage script, you'll first need to download the Azure usage reports from [here](https://cloudpartner.azure.com/#insights/ordersandusage) as CSVs and put them in the usage directory.  After that you can run:

    python usage.py

## Payout
To run the payout scipt, download a CSV for "Inception to Date" [here](https://cloudpartner.azure.com/#insights/payout), rename it to payout.csv and put it in this directory.  After that you can run:

    python payout.py
