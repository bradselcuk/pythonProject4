opelObj = {
    'marka': 'Opel',
    'model': "Corsa",
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
sonuc = len(opelObj)


# print(sonuc)

# opelObj['renk'] = 'kirmizi' #ekle
# opelObj.pop("renk") # sil

# del opelObj["marka"] # sil
# del opelObj
# opelObj.clear() # icini sil

# op = opelObj # copy esitle
# print(op)


# op = opelObj.copy() # copy
# op['Marka'] = 'Mazda'
#
# print(op)
print(opelObj)
