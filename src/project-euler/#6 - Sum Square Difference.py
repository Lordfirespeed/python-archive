numberrange = list(range(1, 100+1))
sumofsquares = sum([number**2 for number in numberrange])
squareofsum = sum(numberrange)**2
difference = max([sumofsquares, squareofsum]) - min([sumofsquares, squareofsum])
print(difference)
