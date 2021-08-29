import pandas as pd

dataSet ={
    'bike': ['yahama','honda','suzuki'],
    'speed': [120,150,180]
}

bike_data= pd.DataFrame(dataSet)
print(bike_data)

# locate row  use loc.

# get sinngle record
print(bike_data.loc[1])

# get multiple record
#note use 2 dimensional array

print(bike_data.loc[[0,1,2]])


# indexing data frame

dataSet_1 ={
    'bike': ['yahama','honda','suzuki'],
    'speed': [120,150,180]
}

bike_data_1= pd.DataFrame(dataSet_1, index=['alpha','beta','theta'])

print(bike_data_1)

# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)