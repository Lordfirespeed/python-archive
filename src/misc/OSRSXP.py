totalxp = 0
for level in range(1, int(input("Level: "))):
    totalxp = (level + (300 * ((2 * level) / 7))) / 4
    print(totalxp)
