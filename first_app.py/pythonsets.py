fruits = {'orange','apple','banana'}
print(fruits)

for x in fruits :
    print(x)
fruits.add('cherry') #listeye ekler
fruits.update(['mango','grape','apple'])# listeye belirlenen elemanları ekler
fruits.remove('mango') #listeden mangoyu siler
fruits.discard('apple') # listeden apple siler
fruits.clear #bütün listeyi siler
print(fruits)
myList = [1,2,3,4,4,5,5]
print(set(myList)) #tekrarlayan terimleri siler
print(myList)#listedeki bütün terimleri ekler


#value &referance types
# value types --- string number

x=5
y=25
x=y
y=10
print(x,y)

# referance types_list
a= ["apple","banana"]
b= ["apple","banana"]
a=b
b[0]="grape"
print(a,b)