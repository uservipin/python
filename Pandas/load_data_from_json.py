import  pandas as pd

df = pd.read_json('data.json')


# print(d

# show complete data
print(df.to_string())

# if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())

# Get a quick overview by printing the first 10 rows of the DataFrame:

print(df.head(10))


# get data from end of data frame


print(df.tail())