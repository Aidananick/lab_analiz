import pandas as pd
import numpy as np
import seaborn as sns  # visualisation
import matplotlib.pyplot as plt  # visualisation

sns.set(color_codes=True)
df = pd.read_csv("D:/Учеба/mtcars.csv");
df.model.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number")
plt.ylabel('Models')
plt.xlabel('model');

plt.figure(figsize=(10, 5))
c = df.corr()
sns.heatmap(c, cmap="BrBG", annot=True)
print(c)

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['model'], df['gear'])
ax.set_xlabel('model')
ax.set_ylabel('gear')
plt.show()