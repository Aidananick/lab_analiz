import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation

sns.set(color_codes=True)
sns.set(color_codes=True)

df = pd.read_csv("D:/Учеба/mtcars.csv");
df = df.rename(columns={"model": "Model", "mpg": "MPG", })

print(df.head(5));