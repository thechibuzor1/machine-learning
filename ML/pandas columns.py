import pandas as pd
df = pd.read_csv("desktop\ML\ca-covid.csv")

df.drop('state', axis = 1,inplace=True)#deleteting the state column

df['Month'] = pd.to_datetime(df['date'],format="%d.%m.%y").dt.month_name()

df.set_index('date', inplace= True)

print(df)