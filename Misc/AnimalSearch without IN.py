List = ['Cow', 'Dog', 'Horse', 'Goat', 'Cat']
Length = len(List)
Search = input('Enter animal name: ').title()
Value = False
for i in range(Length):
    if List[i] == Search:
        Value = True
        break
if Value:
    print("'" + Search + "' was found in the list.")
else:
    print("'" + Search + "' was not found in the list.")
