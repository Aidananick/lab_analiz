import pandas as pd
import seaborn as sns

sns.set(color_codes=True)
df = pd.read_csv("D:/Учеба/mtcars.csv");
print(df.isnull().sum())
df = df.dropna()    # Dropping the missing values.
df.count()
print(df.isnull().sum())