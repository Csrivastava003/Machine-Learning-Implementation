import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

df = pd.read_csv('tips.csv')
print(df.head())
print(np.mean(df['total_bill']))
sns.boxplot(df["total_bill"])
plt.show()

