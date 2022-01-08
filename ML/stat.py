players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

import math

mean = int(sum(players)/len(players))

d = []
for i in players:
    f = abs(i - mean)
    f = f**2
    d.append(f)


varience = int(sum(d)/len(players))
sd = int(math.sqrt(varience))

players_diff = []
for i in players:
    if (i >= mean - sd) & (i <= mean + sd):
        players_diff.append(i)

print(len(players_diff))