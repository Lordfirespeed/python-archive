lyrics = ["And a partridge in a pear tree",
          "Two turtle doves,",
          "Three french hens,",
          "Four calling birds,",
          "Five gold rings,",
          "Six geese a-laying,",
          "Seven swans a-swimming,",
          "Eight maids a-milking,",
          "Nine ladies dancing,",
          "Ten lords a-leaping,",
          "Eleven pipers piping,",
          "Twelve drummers drumming,"]

days = ["first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"]

chorus = "\nOn the %s day of Christmas,\nMy True Love gave to me:"

for i in range(12):
    print(chorus % days[i])
    [print(line) for line in lyrics[:i+1][::-1]] if i != 0 else print("A partridge in a pear tree")
