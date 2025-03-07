def getkey(s):
    return s.split("-")[1]


def sort_keys(path, infile, outfile):
    with open(path+''+infile, 'r') as f:
        inputlines = [line.strip() for line in f.readlines() if "-" in line]

    outputlines = sorted(inputlines, key=lambda s: s.split("-")[1])
    with open(path + "" + outfile, 'w') as o:
        for line in outputlines:
            o.write(line + "\n")


#sort_keys("C:\\Users\\Daniel\\Desktop", "sample.txt", "results.txt")
