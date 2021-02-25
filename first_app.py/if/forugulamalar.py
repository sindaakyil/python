#sayilar = [ 1,3,5,7,9,12,21]

#1)sayilar listesindeki hangi sayılar 3'ün katıdır ?
# sayilar = [ 1,3,5,7,9,12,21]
# for a in sayilar :
#  if ( a%3==0 ):
#     print(a)
#2)sayilar listesinde sayıların toplamı kaçtır?
toplam = 0
sayilar = [1,3,5,7,9,12,19,21]
for b in sayilar :
 toplam+= b 
print(toplam)
#1)sayılar listesindeki tek sayıların karesini alınız.
kare = 0
sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar :
   if (sayi%2==1):
    kare=sayi*sayi
    print(kare)
#şehirler = ['kocaeli','istanbul','ankara','izmir','rize']
#şehirlerin hangirleri en fazla 5 karakterlidir?
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
for sehir in sehirler :
    if (len(sehir)<=5):
        print(sehir)
urunler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s6','price':'7000'},
]

# ürünlerin fiyat ytoplamı nedir?
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print(toplam)

#ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?

for urun in urunler :
 fiyat = int(urun["price"])
 if (fiyat<=5000):
     print(urun)


