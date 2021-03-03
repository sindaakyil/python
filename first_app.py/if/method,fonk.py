#fonksiyon oluşturma:
def sayHello(): # def fonksiyon oluşturmak için anahtar kelime daha sonra fonksiyon ismi belirtiyoruz ve parantez açıp kapıyoruz
     print('hello')
sayHello()
def sayHello(name='user'): # fonksiyona dışardan bir parametre gondermek istediğimizde parantez içine parametre değişkeni tanımlarız
     print('hello'+name) 
sayHello('Çınar')
sayHello('Ada')
sayHello() #parametre belirtilmediğinde '' de belirttiğimiz parametre döner user g,b,

def sayHello(name='user'): # fonksiyona dışardan bir parametre gondermek istediğimizde parantez içine parametre değişkeni tanımlarız
    return ('hello'+name) 
msg = sayHello('Çınar')
print(msg)
def total(num1,num2):
  return num1 + num2
result = total(10,20)
print(result)


def yasHesapla(dogumyili):
    return 2019-dogumyili
agecinar = yasHesapla(1992)
ageAsa = yasHesapla(2000)
print(agecinar, ageAsa)

def change(n):
  n[0]='istanbul'
sehirler= ['ankara','izmir']
n = sehirler[:] #slicing
change(sehirler[:]) #kopya bir liste oluşur orjinal listeninn içeriği değişmez
print(sehirler)
print(n)

def add(a,b,c=0):#eğer parametreleri bazen 2 ve bazen 3 olarak kullanıcaksak 3 parametreyi sıfıra eşitleyebiliriz
   return sum((a,b))
print(add(10,20))

def add(*params): #sonsuz parametrlelerce  işlem yapabiliriz
    print(params) #parametreleri liste olarak yazdırır
    return sum((params))
print(add(10,20,56,78,3,2,2,34,34,3))

def add(*params): #sonsuz parametrlelerce  işlem yapabiliriz
   sum = 0
   for n in params:
       sum = sum + n
   return sum
print(add(10,20,56,78,3,2,2,34,34,3))

def displayUser(**args):
    print(type(args))
    for key,value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name ='çinar',age=2,city='')
displayUser(name ='ada',age=29,city='diyarbakır',phone='2324342')
displayUser(name ='eary',age=30,city='izmit',phone='2324342',email='kykdj.@gmail')
#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
def yazdir(kelime,adet):
    print(kelime * adet)
yazdir('merhaba',10)
#kendine gönderilen sınırsız sayidaki parametreyi bir listeye ekleyen kod

def  listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste
result = listeyeCevir(10,20,30,'merhaba')
print(result)


#girilen iki sayı arasındaki tüm asal sayıları bulunuz

def asalSyilar(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if sayi%i==0:
                   break
            else:
                print(sayi)
sayi1 =int(input('1.sayi giriniz'))
sayi2 =int(input('2.sayi  giriniz'))
asalSyilar(sayi1,sayi2)

#kendisine gönderilern bir sayının tam bölenlerini liste şeklinde geriye gönderen kodu yazınız


def tamblen(sayilar):
    list=[]
    for i in range(2,sayilar):
        if (sayilar%i==0):
         list.append(i)
    return list
sayilar =int(input('sayi  giriniz'))
print(tamblen(20))
          
            

