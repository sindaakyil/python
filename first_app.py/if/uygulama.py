'''
1-100arasınnda rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalısın
**random modülü için"python random" şeklinde arama yapın
**100 üzerinden puanlama yapın her soru 20 puanlama
**hak bilgisini kullanıcıdann alın ve her soru belirtilen can sayısı üzerinden hesaplansın
'''
import random
a =random.randint(1,100)
print(a)
numbers=[]
kacSayi = int(input('kaç sayi gireceksiniz: '))
puan=100
i=0
b=(100/kacSayi)
while i<kacSayi :
    i+=1
    sayi =int(input('sayi giriniz'))
    if (sayi == a):
        print(f'tebrikler bildiniz{puan}')
        numbers.append(sayi) # append gilrilen sayıları numbers listesine eklmek için kullanılır
        break
    else:
     print('sayıyı bilemediniz')
    puan-=b
print(numbers)


import random
sayi = random.randint(1,10)
hak=5
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin = int(input('tahmin:'))
    sayac
    if tahmin < sayi:
        print('yukarı')
    elif tahmin>sayi:
        print('aşağı')
    else:
       print(f'tebrikler {sayac} bildiniz puanınız :{(100 - (20) *(sayac-1))}')
       break
    if hak==0:
        print(f'hakkınız bitti tutulan sayi {sayi}')


   
  
    
