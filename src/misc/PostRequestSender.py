from urllib import request, parse

address = "http://192.168.1.12:8089"

# dataRaw = [("v1", v1), ("y1", y1), ("v2", v2), ("y2", y2)]
dataRaw = [("ab", ["abc", "def", "ghj"]), ("db", [123, 456, 789])]
dataEncoded = bytes(parse.urlencode(dataRaw), "utf-8")

newRequest = request.Request(address, data=dataEncoded)
resp = request.urlopen(newRequest).read().decode("utf-8")
