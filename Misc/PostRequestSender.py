from urllib import request, parse

address = "http://AE4A533373474DA6831EC406052E4FE02.asuscomm.com:8080"

# dataRaw = [("v1", v1), ("y1", y1), ("v2", v2), ("y2", y2)]
dataRaw = [("ab", ["abc", "def", "ghj"]), ("db", [123, 456, 789])]
dataEncoded = bytes(parse.urlencode(dataRaw), "utf-8")

newRequest = request.Request(address, data=dataEncoded)
resp = request.urlopen(newRequest).read().decode("utf-8")
