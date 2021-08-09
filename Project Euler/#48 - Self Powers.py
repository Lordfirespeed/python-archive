target = 1000
num = 0
for i in range(1, target+1):
    num += i ** i
print("Result: %s" % str(num)[-10:])
