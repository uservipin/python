import  pandas as pd

df= pd.read_csv("data.csv")

#print(df)
#print(df.to_string()


# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows
# containg NULL values from the original DataFrame.

new_df= df.dropna()
# print(new_df)


# Replace Empty Values

# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

fill_new_data = df.fillna(120,inplace=True)

print(fill_new_data)
# Replace Only For a Specified Columns
#df['calories'].fillna(100, inplace=True)

# Replace Using Mean, Median, or Mode
x= df['calories'].mean()

#Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

df['calories'].fillna(x,inplace=True)