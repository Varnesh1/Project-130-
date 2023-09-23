import csv, pandas as pd

df = pd.read_csv('final.csv')
print(df.shape)



df = df.drop('Luminosity', axis = 1)
df.to_csv('final2.csv')
