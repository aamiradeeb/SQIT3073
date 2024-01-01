import pandas as pd

url = "https://raw.githubusercontent.com/dosm-malaysia/data-open/main/datasets/prices/prices_district_selected.csv"
dataframe = pd.read_csv(url)
# To view the first few rows of the DataFrame
print(dataframe)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my