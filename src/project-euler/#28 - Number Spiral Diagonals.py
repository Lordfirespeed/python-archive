spiralsize = 1001
seqlength = (spiralsize // 2) + 1  # length of diagonals from centre given spiral size

topright = [(2*n + 1)**2 for n in range(seqlength)]  # sequence (2n+1)^2 OR 4n^2 + 4n + 1
botright = [(4*(n**2) - 2*n + 1) for n in range(seqlength)]  # sequence 4n^2 - 2n + 1
botleft = [(4*(n**2) + 1) for n in range(seqlength)]  # sequence 4n^2 + 1
topleft = [(4*(n**2) + 2*n + 1) for n in range(seqlength)]  # sequence 4n^2 + 2n +1

resultingnums = set(topright + botright + botleft + topleft)
print("Result: %s" % sum(resultingnums))
