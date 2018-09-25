import pandas as pd
import numpy as np



years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

rename_dictionary = {
    'Doctype': 'document', 'EmployerAddressLine1': 'employer_address',
    'EmployerAddressLine2': 'employer_address', 'EmployerName': 'employer',
    'EntityAddressLine1': 'address', 'EntityAddressLine2': 'address', 'EntityCity': 'city',
    'EntityName': 'entity', 'EntityState': 'state', 'EntityZip': 'zip',
    'FilerName': 'filer'
}

transactions = pd.read_csv('philly_transactions2007.csv')

for year in years:
    print(f'Reading {year} data')
    year_transactions = pd.read_csv(f'philly_transactions{year}.csv', low_memory=False)
    print(f'{year_transactions.shape[0]} observations being added with {year_transactions.shape[1]} columns. ')
    transactions = transactions.append(year_transactions, ignore_index=True, sort=True)

transactions.rename(rename_dictionary, axis=1, inplace=True)
transactions.rename(str.lower, axis='columns', inplace=True)

transactions['amended'].replace({'Y': True, 'yes': True, 'N': False, 'no': False}, inplace=True)
transactions['amended'] = transactions['amended'].astype(bool)
transactions['date'] = pd.to_datetime(transactions['date'], errors='coerce')
transactions['subdate'] = pd.to_datetime(transactions['subdate'], errors='coerce')

transactions.drop(['unnamed: 0'], axis=1, inplace=True)
print(transactions.info())

print(transactions[['subdate','year']].dropna())
