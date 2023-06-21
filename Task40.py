import pandas as pnd
df = pnd.read_csv('sample_data/california_housing_train.csv')
df[df['population']<501]['median_house_value'].mean()