opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}
# sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj:
#     print(x)
#
# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():
#     print(x)

# for x,y in opelObj.items():
#     print(x+":",y)

sonuc = "marka" in opelObj
print(sonuc)

# print(opelObj)
