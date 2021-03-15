numbers = [1, 10, 10,12, 5, 6, 7, 54]
letters = ['a', 'b', 'c',]
val = min(numbers)
val = max(numbers)
val= min(letters)
val= max(letters)
val = numbers [3 :6]
numbers[4]= 40

numbers.append(49) # append listeye eleman eklemeye yarar
numbers.append(59)
numbers.insert(3, 75) #insert istediğimiz konuma eleman eklemeye yarar 3. indeksten önce 75 sayısınnı ekler
numbers.pop() #pop en son elemanı silmeye yarar 
numbers.remove(40) #remove silmek istediğiniz karakteri silmek için kullanılır
numbers.sort() #aritmetik olarak  küçükten büyüğe doğru sıralama yapar
numbers.reverse() #aritmetik olarak büyükten küçüğe doğru sıralar
letters.sort() # alfabetik olarak sıralar
letters.reverse() # alfabetik olarak tersten sıralar


print(len(numbers)) #eleman sayılarını öğrenmek için len kullanılır
print(len(letters))#eleman sayılarını öğrenmek için len kullanılır

print(numbers.count(10)) #numbers içinde kaç adet 10 var ona bakar
print(letters.count('a')) #numbers içinde kaç adet "a "var ona bakar
numbers.clear() #numbers listesini siler
print(letters)
print(numbers)
print(val)

names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

#cenk ismini listenin sonuna ekleyiniz

names.append('Cenk')
# sena değerini listenin başına ekleyiniz
names.insert(0 ,'sena')
# deniz ismini listeden siliniz
#names.remove('Deniz')
# deniz isminin indexi nedir,
index = names.index('Deniz')
print(index)
# ali listenin bir elemanı mıdır?
result ='Ali' in names
print(result)
print(names.count('Ali'))
# liste elemanlarını ters çevirin
#names.reserve()
# liste elemanlarını alfabetik olarak sıralayınnız
names.sort()
# years listesini rakamsal büyüklüğe göre sıralayınnız
years.sort()
# str ="chevroler,dacia"karakter dizisini listeye çeviriniz
# str = ['chevrolet', 'dacia']
# result = str.split
# years dizininim en büyük ve en küçük elemanı nedir
val = max(years)
val = min(years)
# years dizisinde kaç tane 1998 değeri vardır
result =years.count(1998)
# years dizisinin tüm elemanlarını siliniz
years.clear()
# kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız

markalar =[]
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)
print(names)
print(str)
print(years)
print(val)
print(result)