animals = ['dog', 'cow', 'cat', 'horse', 'goat']
search = input('Enter animal name: ').lower()
if search in animals:
    print('True')
else:
    print('False')
