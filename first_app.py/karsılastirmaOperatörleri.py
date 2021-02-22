# Girilen 2 sayıdan hangisl büyüktür

a = int(input('a: '))
b = int(input('b: '))
result = (a > b)
print(f'1.sayi: {a} 2.sayi : {b} dan büyüktür : {result}')

# Kullannıcıdan 2 vize (%60)ve final (%40)notunu alıp ortalama hesaplayınız
vize1= int(input('vize1: '))
vize2 =int(input('vize2: '))
final =int(input('final: '))
result = (((((vize1+vize2)/2)*60)/100) +((final*40)/100))
ortalama = (result>50)
print(f" ortalama: {ortalama} geçti ve dersten geçme durumunuz : {ortalama >=50 }")
print(result)



# Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazsın


# Girilen bir sayını tek mi çift mi olduğunı yazdırın
sayi= int(input('1.sayi: '))
tekcift = sayi % 2 == 0
print(f" sayi çift mi :{tekcift}")
# Girilen bir sayının negatif pozitif durumunu yazdırın 
sayi= int(input('1.sayi: '))
pozneg = sayi >= 0
print(f" sayi pozitif mi  : {pozneg} ")
# Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
# (email: email@sadikturan.com parola:abc123)

email ='email@sadikturan.com'
pasword ='abc123'

girilenEmail = input('email: ')
girilenPasword = input('parola: ')

isMail = (email==girilenEmail)
isPasword = (pasword == girilenPasword)

print(f' girilen mail doğru mu {isMail} girilen parola doğru mu : {isPasword}')