unitword = {0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
            }

teenword = {"": "ten",
            "one": "eleven",
            "two": "twelve",
            "three": "thirteen",
            "four": "fourteen",
            "five": "fifteen",
            "six": "sixteen",
            "seven": "seventeen",
            "eight": "eighteen",
            "nine": "nineteen"
            }

tensword = {0: "",
            1: "ten",
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
            }


def words(integer):
    outputstring = ""
    for valuecolumn, number in enumerate(str(integer)[::-1]):
        number = int(number)
        if valuecolumn == 0:
            outputstring = unitword[number] + outputstring
        elif valuecolumn == 1:
            if number == 1:
                outputstring = teenword[outputstring]
            else:
                outputstring = tensword[number] + outputstring
        elif valuecolumn == 2:
            if number != 0:
                outputstring = unitword[number] + "hundredand" + outputstring
        elif valuecolumn == 3:
            outputstring = unitword[number] + "thousand" + outputstring
    if outputstring[-3:] == "and" and outputstring != "onethousand":
        outputstring = outputstring[:-3]
    elif outputstring == "":
        outputstring = "zero"
    return outputstring


numberwords = []
for index in range(1, 1001):
    numberwords.append(words(index))

lengthwords = [len(word) for word in numberwords]
print("Result: " + str(sum(lengthwords)))
