import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
print(df[pd.isnull(df['Rating'])].head(2))