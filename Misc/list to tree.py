current = [['A1'], ['B1', 'A1'], ['B2', 'A1'], ['C1', 'B2', 'A1'], ['D2', 'C1', 'B2', 'A1'], ['D1', 'C1', 'B2', 'A1'], ['A2']]
tree = {}

for item in current:
    currentdict = tree
    for key in item[::-1]:
        if key not in currentdict.keys():
            currentdict[key] = {}
        currentdict = currentdict[key]

expected = {
  'A1': {
    'B1': {},
    'B2': {
      'C1': {
        'D1': {},
        'D2': {}
      },
    },
  },
  'A2': {}
}

print(tree == expected)  # True
