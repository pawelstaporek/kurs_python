import pandas as pd

df = pd.read_csv("log.csv", delimiter=';', header=None)

print(df.head())

df.to_excel("log.xlsx", index=False, header=False)