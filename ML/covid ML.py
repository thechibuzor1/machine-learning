import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("desktop\ML\ca-covid.csv")

df.drop('state', axis = 1,inplace=True)#deleting the state column

df['date'] = pd.to_datetime(df['date'],format="%d.%m.%y") 
df['month'] = df['date'].dt.month

df.set_index('date', inplace=True)

df[df['month'] == 12]['cases'].plot()
plt.savefig('plot1.png')
plt.show()

(df.groupby('month')['cases'].sum()).plot(kind = 'bar')
plt.savefig('plot2.png')
plt.show()