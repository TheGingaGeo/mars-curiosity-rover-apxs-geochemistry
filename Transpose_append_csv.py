#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:43:51 2021

@author: josh
"""


"""
This code takes a directory of csv files, transposes them and then concatenates them underneath each other.
Input: csv files
Output: transposed and concatenated csv file
"""

import pandas as pd
import os
from glob import glob

directory = '/Users/josh/Downloads/Mars-Curiosity_APXS/Data/'   # Root directory containing files and subdirectories with csvs
file_extension = "*.csv"   # File extension of your files for concatenating
all_csv_files = [file
                 for directory, subdir, files in os.walk(directory)
                 for file in glob(os.path.join(directory, file_extension))]   # Finds all csv files in directory and creates a list to be looped through

li = []   # Create an empty list to add the processed csv files to for concatenating

for filename in all_csv_files:   # For loop through each element (csv file) in the list of csvs in all_csv_files
    df = pd.read_csv(filename, index_col=None, header=0)   # Read in each csv file
    df_tr = df.transpose()   # Transposed each csv file
    df_tr['Filename'] = os.path.basename(filename)   # Add a new column called Filename to the transposed csv and populate it with the name of the file
    df_tr['Sol'] = os.path.basename(filename[-24:-20])   # Add a new column called Sol to the transposed csv and populated with with the Sol number which is contained within the filename itself at index -24 to -20
    li.append(df_tr)   # Append this file to the list for concatenating when the loop is finished

transposed_files = pd.concat(li, axis=0, ignore_index=True)   # Concatenate each 
transposed_files.to_csv("/Users/josh/Downloads/Mars-Curiosity_APXS/all_csv_transposed.csv", index=False)   # Write new appended file to csv
print(transposed_files.head(15))   # Print the first 15 rows of the head of the new appended file to check is they tranposed and concatenated properly
print()
print(all_csv_files)   # Print the list of the transposed and appended csv files for reference