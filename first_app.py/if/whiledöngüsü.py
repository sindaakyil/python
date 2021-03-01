name ='' #False
while not name.strip() : #bir isim girilmediği sürece sürekli döngüyü döndürür.
    name = input('lütfen isminizi giriniz')
print(f' marhaba ,{name}')

sayilar = [1,3,5,7,9,12,19,21]
#sayilar listesini while döngüsü ile yazdırın

i = 0
while i < (len(sayilar)):
    print(sayilar[i])
    i+=1
#başlangıç ve bitiş değeri kullanıcı tarafından belirlenen sayıların arasındaki tüm tek sayıları yazan kod
 
baslangic = int(input('baslangıc değerini giriniz: '))
sonSayi = int(input('son  sayıyı  giriniz: '))
i = baslangic
while i< sonSayi :
    i+=1
    if (i%2==1):
        print(i)
# 1 ve 100 arasındaki sayıları azalarak yazdırın
b= 5
while b > 0:
    print(b)
    b-=1
#kullanıcıdan aldığımız sayıları listeleyen kod
numbers=[]
kacSayi = int(input('kaç sayi gireceksiniz: '))
i = 0
while i<kacSayi :
    sayi =int(input('sayi giriniz'))
    numbers.append(sayi) # append gilrilen sayıları numbers listesine eklmek için kullanılır
    i+=1
numbers.sort() #sayiların aritmetik olarak küçükten büyğe doğru sıralanmasını sağlar
print(numbers)
#kullanıcıdan alacağımız sınırsız ürün bilgisni ürünler listesine  
#ürün sayısını kullanıcıya sorun 
#dictionary listesinin yapısı (name,price şeklinde olsu)
#ürün ekleme işlemi bittiğinde while ile ekrana yazdırın
urunler =[]
i=0
adet = int(input('kaç ürün  gireceksiniz: '))

while i<adet :
  name = input('ürün adı  giriniz:')
  price =int(input('fiyatı giriniz'))
  urunler.append({
       'name ': name,
       'price' : price
   })
i+=1
for urun in urunler:
 print(f'ürün adı{urun["name"]} ürün fiyati{urun["price"]}')




for item in range(10,100,10):#range başlagıç bitiş ve artış değerine göre sayıları sıralar
  print(item)
print(list(range(10,100,10))) #list ise range aralığındaki sayıların listelenmesini sağlar
#enumerate 
index = 0
greeting = 'hello there'
for letter in greeting:
     print(f'index{index} letter {letter}')
     index+= 1
     #index i eğer önceden tanımlamak istemiyorsak 
greeting = 'hello there'
for index, letter in enumerate(greeting):
     print(f'index{index} letter {letter}')
#zip ile iki listeyi birleştirp aynı index numaralı olanları birleştirir

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))

for item in (zip(list1,list2)):
    print(item)
for a,b in zip(list1,list2):
    print(a,b)



for x in range(10):
    print(x)
numbers = [x for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0 ]
print(numbers)
 
mylist = 'hello'
list =[]
for letter in mylist:
     list.append(letter)
print(list)
 #aynı işlemi daha kısa bir şekilde yazabiliriz
mylist = [ letter for letter in mylist]
print(list)
years = [1995,1963,1991]
ages= [2019-year for year in years]
print(ages)
numbers = [x if x%2==0 else 'tek' for x in range(10) ]
print(numbers)

result=[]
for x in range(3):
 for y in range(3):
  result.append((x,y))
print(result)

#daha basit haliyle yapacak olursak 
numbers= [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
