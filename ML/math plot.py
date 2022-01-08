import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("desktop/titanic.csv")
plt.scatter(df['Fare'],df['Pclass'], c= df['Survived'])
plt.show()