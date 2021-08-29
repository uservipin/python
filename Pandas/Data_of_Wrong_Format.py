import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])


# convert all cells in the 'Date' column into dates.
# andas has a to_datetime() method for this
print(df.to_string())

# we can remove the row by using the dropna() method

df.dropna(subset=['Date'], inplace = True)
