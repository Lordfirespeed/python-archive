import re

matcher = re.compile(r"\d+")
test = matcher.findall("#1271 @ 292,532: 21x20")
print(test)

p = re.compile(r'\d+')
m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

# with open("2018/2018day3input.txt") as inputfile:
# inputdata = [matcher.findall(line.strip()) for line in inputfile.readlines()]
