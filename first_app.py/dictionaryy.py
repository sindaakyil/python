# ögrenciler = {
#     '120' : {
#         'ad': 'ali',
#         'soyad': 'yılmaz',
#         'telefon':'5676465767'
#     },
#     '125':{
#         'ad': 'can',
#         'soyad': 'yılmaz',
#         'telefon':'3564566646'
#     },
#     '128':{
#         'ad': 'volkan',
#         'soyad': 'yılmaz',
#         'telefon':'dgdhdfhg'
#     },
# }

# 1)bilgileri verilen öğrencileri kullanıcıdan aldığınız bigilerle dictionary içinde saklayınız.
# 2)öğrenci numarasını kullanıcıdann alıp ilgili öğrenci bilgisini gösteriniz


ogrenciler ={}
number = input("ögrenci no: ")
name = input("ögrenci adı :")
surname = input("ögrenci soyadı: ")
phone = input("ögrenci telefon: ")

# ogrenciler[number]= {
#     'ad': name,
#     'soyad': surname
# }


ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
}),

ogrenciler ={}
number = input("ögrenci no: ")
name = input("ögrenci adı :")
surname = input("ögrenci soyadı: ")
phone = input("ögrenci telefon: ")

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
}),
ogrenciler ={}
number = input("ögrenci no: ")
name = input("ögrenci adı :")
surname = input("ögrenci soyadı: ")
phone = input("ögrenci telefon: ")

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
})
print(ogrenciler)

ogrNo = input('ögrenci no : ')
ogrenci = ogrenciler[number]
print(f"arafığınız {ogrNo} nolu ögrencinin adı {ögrenci['ad']} ve telefonu ise {ögrenci['tel']}")
