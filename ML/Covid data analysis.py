import pandas as pd
df = pd.read_csv("desktop\ML\ca-covid.csv")

df.drop('state', axis = 1,inplace=True)#deleteting the state column
df.set_index('date', inplace= True)

df['ratio'] = df['deaths']/df['cases']

max_ratio = df[df['ratio'] == df['ratio'].max()]
print(max_ratio)