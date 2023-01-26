import requests

ProductIDs = [
    5538831958,
    5538831962,
]


def getProductInfo(ID):
    request = requests.get("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(ID))
    return request.json()


def getImageAssetID(ID, tries):
    product = getProductInfo(ID)

    def checkID(cID):
        cproduct = getProductInfo(cID)
        if cproduct["Name"] == product["Name"] and cproduct["AssetTypeId"] == 1 and cproduct["Creator"]["Id"] == product["Creator"]["Id"]:
            return cID
        elif cID >= (ID - tries):
            return checkID(cID - 1)
        else:
            return "NOT FOUND"

    return checkID(ID - 1)


outstr = "module.atlases = {\n"
for index, prodID in enumerate(ProductIDs):
    outstr = outstr + "\t[" + str(index+1) + "] = \"rbxassetid://" + str(getImageAssetID(prodID, 50)) + "\",\n"
outstr = outstr + "}"
print(outstr)

