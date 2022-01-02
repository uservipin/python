import os
import glob
import pandas as pd
os.chdir("D:\Time_Line\Test_VAB_in_Excel_Merge_files")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


#This document is reference from  please have a look for more reference
#  https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py
