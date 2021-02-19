# 1)"bmv ,mercedes,opel, mazda" elemannlarına sahip bir liste oluşturunuz.

liste =['bmv', 'mercedes', 'opel','mazda']
#2)liste kaç elemanlıdır.
result=(len(liste))
#3)mazda değerini toyota ile değiştirin
liste[-1] = 'toyota'
result = liste

#listenin ilk ve son elemanı nnedir?
result =liste[0]
result =liste[3]
#6)mercedes listenin bir elemanımıdır?
result = 'mercedes' in liste
#listenin -2 indeksindeki değer nedir
result = liste[-2]
#listenin ilk 3 elemanını alın
result= liste[0 : 3]
#listenın son 2 elemanının yerie 'toyota" ve "renault" olarak değiştirin
liste[-2]= 'toyota'
liste[-1]= 'renault'
#print(liste)
#listenin üzerine "audi"ve "nissan " değerlerini ekleyiniz
result = liste + ['audi' ,'nissan']
#listenin son elemanını silin
del liste[-1]
result = liste
#liste elemanlanlarını tersten yazdırınız
result = liste [ ::-1]
#12)aşağıdaki verileri bir liste içinde saklayınız
# studentA: yiğit bilgi 2010,(70,60,90)
#studentB:  sena turan 1999,(80,80,70)
#studentC:  ahmet turann 1998,(80,70,90)

studentA =['yiğit','bilgi',2010,[70,60,90]]
studentB =['sena','turan',1999,[70,60,90]]
studentC =['ahmet','turan',1998,[70,60,90]]
#3) liste elemanlarını ekrana yazınız
result=studentA[0]
print(result)





# print(liste)