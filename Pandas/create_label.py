import  pandas as pd

listA = [10,30,40,49]

# with the help of index, provide index for items.
series = pd.Series(listA,index=['a','b','c','d'])
print(series)


# When label created you can access an item by referring to the label.
print(series["a"])

