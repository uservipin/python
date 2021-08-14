import pandas as pd

df = pd.read_csv('data.csv')

#In our example, it is most likely a typo, and the value should be
# "45" instead of "450", and we could just insert "45" in row 7:

#Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45


#To replace wrong data for larger data sets you can create some rules,
# e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


# Removing Rows

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

# Delete rows where "Duration" is higher than 120:

#---------------------

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)


#Removing Duplicates
# Returns True for every row that is a duplicate, othwerwise False:

print(df.duplicated())


# To remove duplicates, use the drop_duplicates() method

# Remember: The (inplace = True) will make sure that the method does NOT return a new
# DataFrame, but it will remove all duplicates from the original DataFrame.

df.drop_duplicates(inplace = True)
