#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# upload data
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# change columns name
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# merge data and delete unwanted column
data = pd.concat([general, prenatal, sports], ignore_index=True)
del data['Unnamed: 0']

# delete completely missing rows
data.dropna(subset=['hospital'], inplace=True)

# put corrected label for gender
data.gender[(data.gender == 'female') | (data.gender == 'woman') | (data.gender.isna())] = 'f'
data.gender[(data.gender == 'male') | (data.gender == 'man')] = 'm'

# Replace all others NaN values with zero
data.fillna(value=0, inplace=True)
# print(data.head(20))

# Which hospital has the highest number of patients?
print(f"The answer to the 1st question is {data.hospital.value_counts().idxmax()}")
data.groupby('hospital').agg({'hospital': 'count'}).plot(kind='bar')
plt.hist(data['hospital'], histtype='bar')
plt.show()

# What is the most common diagnosis among the sports patients?
print(f"The answer to the 2nd question is {data[data.hospital=='sports'].diagnosis.value_counts().idxmax()}")
# print(f"The answer to the 2nd question is {data.diagnosis.value_counts().max()/1000}")
data.groupby('diagnosis').agg({'diagnosis': 'count'}).plot(kind='pie', y='diagnosis')
plt.pie(data.diagnosis.value_counts())
plt.show()
# print(f"The answer to the 2nd question is {round(data[(data.hospital == 'general') & (data.diagnosis == 'stomach')].shape[0]/data[(data.hospital == 'general')].shape[0], 3)}")

# print(f"The answer to the 3rd question is {round(data[(data.hospital == 'sports') & (data.diagnosis == 'dislocation')].shape[0]/data[(data.hospital == 'sports')].shape[0], 3)}")

# data[(data.hospital == 'general') | (data.hospital == 'sports')].groupby('hospital').agg({'age': 'median'}).diff
# print("The answer to the 4th question is 19.0")

# Build a violin plot of growth distribution by hospitals.
plt.violinplot([data[data.hospital == 'general']['height'], data[data.hospital == 'prenatal']['height'], data[data.hospital == 'sports']['height']])
plt.show()
print(f"The answer to the 3rd question is: It's because the sport dataset has athlete people who are certainly bigger than normal people.")
