import pandas as pd
import seaborn as sns

sns.set(color_codes=True)
df = pd.read_csv("D:/Учеба/mtcars.csv");
df.shape
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

df = df.drop_duplicates()
print(df.head(5))
