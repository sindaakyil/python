x = 5
hak = 5
devam = 'e'
result = 5 < x < 10 

#and
result = (x > 5 )and (x < 10 ) # eğer her iki ifadennin doğru olduğu durumda true döndürür
result = (hak>0) and (devam == 'e')
print(result)
# or
result = (x > 0) or (x % 2 == 0)  #or işleminde ise tek bir değerin true olması durumunda bile true döndurur
print(result)
#not 

result = not(x > 0) #not operatörü ile tam tersini alabiliriz
print(result)

#x, 5-10 arasında olan bir çift sayı mı?
result = (((x>5) or (x<10)) and (x % 2 == 0))
print(result)


#1.Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
sayi = int(input('sayi : '))
result = ((sayi > 0 ) and (sayi < 100))
print(result)

#2.Girilen bir sayının pozitif çift sayı olduğunu kontrol ediniz
a = int(input('sayi : '))
result = ((a>0) and (a % 2 == 0))
print(result)

#3.Email ve parola bilgileri ile giriş kontrolu sağlayınız
parola = 123
mail = 'sinda@gmail.com'

email = input('email: ')
password = int(input('parola: '))

result = (( email == mail ) and (password == parola))
print(result)

#4.Girilen 3 sayısı büyüklük olarak karşılaştırınız

b = int(input('1.sayi: '))
c= int(input('2.sayi: '))
d = int(input('3.sayi: '))
result= (b>c) and (c>d)
print(result)
result= (c>b) and (c>d)
print(result)
result= (d>b) and (d>c)
print(result)
#5.kullanıcıdan 2 vize (%60) ve final (½40) notunu alıp ortalama hesaplayınız.
#  a)ortalama 50  olsa bile final notu en az 50 olmalıdır
#  b) finalden 70 alındığında ortalamannın önemi olmasın

vize1 = float(input('1.vize: '))
vize2 = float(input('2.vize: '))
final = float(input('final: '))

ortalama =  ((((vize1 + vize2)/2)*0.6) + ((final)*0.4))

print(ortalama)
result = ((ortalama >= 50) and (final > 50))
print(f" ortalama {ortalama} geçme durumu: {result} ")
result = ((ortalama >= 50) or (final>69))
print(f" ortalama {ortalama} geçme durumu: {result} ")


#6. kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
#    formül:(kilo/boy uzunluğunun karesi )
#    aşağıdaki tabloya göre kişi hangi gruba girmektedir

#    0-18.4   => zayıf
#    18.5-24.9=>normal
#    25.0-29.9=>fazla kiolu
#    30.0-34.9=>şişman (obez)

boy = float(input('boy: '))
kilo = float(input('kilo: '))

vki= (kilo)/((boy)**2)
zayif=(vki>0) and(vki<18.4 )
normal=(vki>18.4) and(vki<24.9 )
kilolu=(vki>25.0) and(vki<29.9 )
obez=(vki>30.4) and(vki<34.9 )

print(f" vucut kitle indeksi {vki} {zayif} zayıf")
print(f" vucut kitle indeksi {vki} {normal} normal")
print(f" vucut kitle indeksi {vki} {kilolu} kilolu")
print(f" vucut kitle indeksi {vki} {obez} obez")
