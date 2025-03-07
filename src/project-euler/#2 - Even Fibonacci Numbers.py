numbers = [1, 2]
while numbers[-1] < 4_000_000:
    numbers.append(numbers[-1] + numbers[-2])
result = sum([number for number in numbers if number % 2 == 0])
print(result)
