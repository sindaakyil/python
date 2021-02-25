# Girilen 2 sayıdan hangisl büyüktür

a = int(input('a: '))
b = int(input('b: '))
if (a>b):
    print(f'en büyük sayı {a}')
else :
    print(f"en büyük sayı {b}")
# Kullannıcıdan 2 vize (%60)ve final (%40)notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazsın

vize1= int(input('vize1: '))
vize2 =int(input('vize2: '))
final =int(input('final: '))
ortalama = (((((vize1+vize2)/2)*60)/100) +((final*40)/100))
if (ortalama>=50):
    print(f'ortalamanız {ortalama} geçtiniz')
else : 
    print(f'ortalamanız {ortalama} kaldınız')


# Girilen bir sayını tek mi çift mi olduğunı yazdırın
sayi= int(input('1.sayi: '))
if (sayi % 2 == 0) :
   print(f" sayi çift")
else :
    print (" sayı tek" )
# Girilen bir sayının negatif pozitif durumunu yazdırın 
sayi= int(input('sayi: '))
if (sayi >= 0) :
    print("pozitif")
else :
    print("negatif")

# Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
# (email: email@sadikturan.com parola:abc123)

email ='email@sadikturan.com'
pasword ='abc123'

girilenEmail = input('email: ')
girilenPasword = input('parola: ')

if ((email==girilenEmail.lower().strip()) and (pasword == girilenPasword.lower())) : #lower girlen büyük harf varsa küçük harfe çevirir
    print(" kullanıcı mail doğru ")
else :
    print(" kullanıcı mail yanlış")

# strip ise girlen boşlukları siler

