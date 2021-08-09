import hashlib
import itertools
from string import ascii_lowercase


def getmd5(string):
    md5 = hashlib.md5()
    md5.update(string.encode())
    return md5.hexdigest()


def crack(hashed):
    global alphabet
    length = 4
    while True:
        print("Cracking: %s, Current Length: %s" % (hashed[:5] + "...", length))
        for chars in itertools.product(alphabet, repeat=length):
            string = "".join(chars)
            if getmd5(string) == hashed:
                return string
        length += 1


# hashes = ["8f330787c0b4bb8a4dfdd31f3e1792b3",
#           "d18c2ed3165af2b07508454f2e5b95cd",
#           "35f92ef81ef726905a4edc54cf99d8cc",
#           "ebe62bac6f23ac1a1d8586009a51622b",
#           "574c9b34b3c8e6bb64b039d726ef09fd",
#           "cb082b6b18c868dac92bc30f93d4cb76",
#           "e2d3d81e126518ce460fbddd5abe5dbd",
#           "d4af6a342e73f3d46f0500981e284798",
#           "48754180065bb5962b62d48f09d65dc9",
#           "07e7fd52bc55c9cc55792883930f7a73",
#           "93922650c136c721b2553afb4439d4c8",
#           "f85f4590f012d12a6434fc76c1436965"]  # -> triplesix.co.uk/brute.php


hashstring = "7919e1a4942acbe4e94a02e0a493a90a6e3dbca453faa02b92335560400b9b8b705848c45df6936e84c14a9c371a3d6a794f57e5a5ee0151ace7c549520c2c26f9f27b4f1a09f28c34da00a8fa8a9089120f0362ec7400898ffb8ca15b983a9675667901c4a09f9c99aa9b85b27e774d61b4a84f46431bb087325d32fbcfd8f81546c7b445ed2eeae82c95df971e95a20388e7e249233f2f0f489344c29b4ae0db25ca5745148a1b9516d3e7bc14cbfd6d2f8280093cfb9155b01ca29a96be56bad4bd45486c5d6f8473a3e184dfc9939b699bea024d0fba27429b49edbab9b9b7bd5432a4c31307f6d10a345b0caba2db25ca5745148a1b9516d3e7bc14cbfdd690af28155c7c3b1f8228c11eb5f90d70e48aecb69d8ae215f627d1c3cf9324"
hashes = [hashstring[i:i+32] for i in range(0, len(hashstring), 32)]
# znkvg yycux joykt romnz ktskt zigvo zgrki gvozg rsznk oxkvr gikic ozngu tkznk lotgr kxkvr gikic ozngz nxkk
hmm = "znkvg yycux joykt romnz ktskt zigvo zgrki gvozg rsznk oxkvr gikic ozngu tkznk lotgr kxkvr gikic ozngz nxkk".split(" ")
"the password is 'Enl1ghtenM3nt' capital e capital m the i replace with a one the final e replace with a three"

alphabet = ascii_lowercase + "1234567890"

output = []

for index, hashed in enumerate(hashes):
    output.append(crack(hashed))
    print("Found value of hash #%s: %s" % (index+1, output[-1]))

