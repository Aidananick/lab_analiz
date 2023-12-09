import pandas as pd
import seaborn as sns

sns.set(color_codes=True)
df = pd.read_csv("D:/Учеба/mtcars.csv");

df = df.drop(['gear', 'carb', 'vs'], axis=1)
print(df.head(5));