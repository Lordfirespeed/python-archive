startnumber = int(input("Enter number: "))
number = startnumber
binary = []
binnum = 1
while binnum <= number:
    binnum *= 2
binnum /= 2

while binnum >= 1:
    if number // binnum == 1:
        binary.append("1")
        number -= binnum
    else:
        binary.append("0")
    
    binnum /= 2

print(str(startnumber) + " is ...")
print(''.join(binary))
print("... in binary.")
