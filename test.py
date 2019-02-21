import random
season = []
all = []
for j in range(4):
    for i in range(3):
        n = random.randint(0, 1000)
        season.append(n)
    all.append(season)
print(season)
print(all)
