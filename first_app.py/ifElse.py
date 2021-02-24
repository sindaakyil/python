userName = 'sinda'
password= 123

name = input('kullanıcı adı: ')
parola =int(input('parola: '))

if (name == userName):
  if (parola == password):
     print('hoş geldiniz')
  else:
     print('parola yanlış')
else:
     print('kullanıcı adı yanlış')       




num = int(input('sayi: '))
if num > 0:
    print('sayı pozitiftir')
elif num < 0:
    print('sayi negatiftir')
else : 
    print('sayı sıfırdır')


# kullanıcıdan isim, yaş ve eğitim bilimlerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır
isim = input('adınızı giriniz: ')
yas = int(input('yaşınızı giriniz: '))
egitim = input('eğitim bilgilerinizi giriniz: ') 
if ((egitim == 'lise') or (egitim == 'üniversite ') and ( yas  >= 18 )):
   print('ehliyet alabilirsiniz')
else :
    print('ehliyet alamazsınız')
# bir öğrencinin 2 yazılı bir sözlü nnotunu alıp hesaplalan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız
# 0-24 = 0
# 25-44 = 1
# 45-54 =2
# 55-69= 3
# 70 -84= 4
# 85-100 = 5

yazili1 = float(input('1.yazılı notu: '))
yazili2 = float(input('2.yazılı notu: '))
sözlü = float(input('sözlü notu: '))
ortalama = (((yazili1)+(yazili2)+(sözlü))/3)

# sifir = ((ortalama > 0 ) and (ortalama <24))
# bir = ((ortalama > 25 ) and (ortalama <44))
# iki = ((ortalama > 45 ) and (ortalama <54))
# üc = ((ortalama > 55 ) and (ortalama <69))
# dört = ((ortalama > 70 ) and (ortalama <84))
# bes = ((ortalama > 84 ) and (ortalama <100))

if ((ortalama > 0 ) and (ortalama <24)):
   print(f"ortlamanız {ortalama} notunuz:{sifir}")
elif ((ortalama > 25 ) and (ortalama <44)):
   print(f"ortlamanız {ortalama} notunuz: bir ")
elif ((ortalama > 45 ) and (ortalama <54)):
    print(f"ortlamanız {ortalama} notunuz: iki ")
elif ((ortalama > 55 ) and (ortalama <69)):
    print(f"ortlamanız {ortalama} notunuz: üç ")
elif ((ortalama > 70 ) and (ortalama <84)):
    print(f"ortlamanız {ortalama} notunuz: dört ")
elif ((ortalama > 84 ) and (ortalama <100)):
    print(f"ortlamanız {ortalama} notunuz: beş ")
else :
    print('yanlış bilgi girdiniz' )

    

# Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşaıdaki bilglerlere göre hesaplayınız
# 1.bakım = 1. yıl
# 2.bakım = 2. yıl
# 3.bakım = 3. yıl
import datetime
tarih = int(input('aracınnızı hangi tarihte aldınız(2019/08/08)'))
tarih= tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[3]))
simdi=datetime.datetime.now()
print(simdi - tarih)
fark = simdi - trafigeCikis
print(fark)
days = fark.days
if days > 0 and days < 365 :
    print('1. bakım yılı ')
elif days>365 and days<365*2:
    print('2. bakım yılı ')
elif days>365*2 and days<365*3:
    print('3. bakım yılı ')
else:
    print('hatalı giriş')
