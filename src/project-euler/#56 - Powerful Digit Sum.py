target = 100

maxsum = 0
for a in range(1, target+1):
    for b in range(1, target+1):
        val = a ** b
        digitsum = sum([int(c) for c in str(val)])
        maxsum = digitsum if digitsum > maxsum else maxsum

print("Largest digital sum for value a^b where a and b are natural values lesser than %s: %s" % (target, maxsum))
