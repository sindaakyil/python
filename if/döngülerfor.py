numbers = [ 1,2,3,4,5,6]
for a in numbers :
    print('Hello')
names = ['çınar','sadık','sena']

for name in names :
    print(f'my name is {name}')
name = 'sadik turan'
for n in name :
    print(n) #eğer print (name) yazarsak harf sayısı kadar sadik turan yazar print(n ) string ifadenin her bir karakteri tek tek yazdırılır
tuple = ((1,2),(3,4),(5,6))
for t in tuple : # t yerine a,b dersek her gelen a ya ilk eleman b ye ikinci eleman dek gelir
    print(t)
d= {'k1':1, 'k2':2 , 'k3':3}
for key, value in d.items():
    print(key,value)