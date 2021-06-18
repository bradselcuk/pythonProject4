urunler = {
           '1': {'ad': 'ford', 'fiyat': '5000'},
           '2': {'ad': 'toyota', 'fiyat': '2000'},
           '3': {'ad': 'Nissan', 'fiyat': '2500'}
           }


# id = input('id:  ')
# ad = input('ad:  ')
# fiyat = input('fiyat:  ')
#
# urunler[id] = {
#     "ad":ad,
#     "fiyat":fiyat
# }
# id = input('id:  ')
# ad = input('ad:  ')
# fiyat = input('fiyat:  ')
#
# urunler[id] = {
#     "ad":ad,
#     "fiyat":fiyat
# }
# id = input('id:  ')
# ad = input('ad:  ')
# fiyat = input('fiyat:  ')
#
# urunler[id] = {
#     "ad":ad,
#     "fiyat":fiyat
# }

id = input ('aradiginiz ID')
urun = urunler[id]

print(f'id: {id}, urun adi: {urun["ad"]},urun fiyati: {urun["fiyat"]}')
# print(urunler)

