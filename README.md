# Data Analysis for Hospitals
## Description
You're currently working with the data for local hospitals. You have several files with information about patients
from different districts. sometimes, the data is split into many datasets or may contain empty or invalid values.
The first step is to preprocess the data before the analysis: merge the files into one, delete empty or incorrect
rows, fill the missing values, and so on.  
You will deal, with datasets that contain information about patients from three hospitals: a general, a prenatal, and
a sports one.

## Objectives
1. Read 3 CSV files containing the datasets from the user input.
2. Merge the data frames into one after having changed some column names.
3. Delete all the empty rows, replace NaN values in the gender column of the prenatal hospital with f and replace
the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros.
4. Start a comprehensive study of data finding de main characteristics of data and considering data distributions:
    * which hospital has the highest number of patients?
    * what share of the patients in the general hospital suffers from stomach-related issues?
    * what share of the patients in the sports hospital suffers from dislocation-related issues?
    * what is the difference in the median ages of the patients in the general and sports hospitals?
   * What is the most common diagnosis among the sports patients?
