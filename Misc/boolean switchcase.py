answer = input('Age: ')
age = {
    True: "You are elegible for a license.",
    False: "You are too young for a license."
    }
print(age[int(answer) >= 17])
