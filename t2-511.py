# 5
from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing(as_frame=True)
# print(data)

# 6
# Add column median value of the house (target) and print data + target
data = pd.concat([data.data.head(), data.target.head()], axis=1)
print("---6---")
print(data)

# 7
print("---7---")
print(data.info())

# 8
print("---8---")
print(data.isna().sum())

# 9
print("---9---")
print(data.loc[(data['HouseAge'] > 50) & (data['Population'] > 2500)])

# 10
print("---10---")
print(data['MedHouseVal'].max())
print(data['MedHouseVal'].min())

# 11
print("---11---")
print(data.apply(print))
