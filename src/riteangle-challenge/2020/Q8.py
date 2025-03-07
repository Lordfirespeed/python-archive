from string import ascii_uppercase as lettertiles
import itertools

success = 0
total = 0

for selected_tiles in itertools.product(lettertiles, repeat=3):
    if len(set(selected_tiles)) == len(selected_tiles):
        print(selected_tiles)
        if selected_tiles[2] > selected_tiles[1] > selected_tiles[0]:
            print("SUCCESS")
            success += 1
        else:
            print("FAIL")
        total += 1

print(success/total)
