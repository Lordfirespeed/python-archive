weight = 80

oxygen, oxyPrice = 0.65, 0.13
carbon, carPrice = 0.16, 0.01
hydrogen, hydPrice = 0.1, 0.13
nitrogen, nitPrice = 0.03, 0.13
calcium, calPrice = 0.016, 0.07
potassium, potPrice = 0.0025, 410
sodium, sodPrice = 0.0015, 158

oxyTotal = weight * oxygen * oxyPrice
carTotal = weight * carbon * carPrice
hydTotal = weight * hydrogen * hydPrice
nitTotal = weight * nitrogen * nitPrice
calTotal = weight * calcium * calPrice
potTotal = weight * potassium * potPrice
sodTotal = weight * sodium * sodPrice

print(sum([oxyTotal, carTotal, hydTotal, nitTotal, calTotal, potTotal, sodTotal]))
