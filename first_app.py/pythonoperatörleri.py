x,y,z =2,5,10
numbers = 1,5,7,10,6
#kullanıcıdan aldığınız 2 sayısının çarpımı ile x,y,z toplamının farkı nedir?

sayi1 = int(input("sayi1 : "))
sayi2 = int(input("sayi2 : "))

carpim = sayi1 * sayi2
toplam = x + y + z
sonuc = carpim - toplam
print(sonuc)
 
#y'nin x'e kalansız bölümünü hesaplayınız

result= y //x
print(result)
#(x,y,z) toplamının mod 3'ü nedir?
result = (x + y + z) %3
print(result)
#  y'nin x.kuvvetini hesaplayınız
result =y**x
print(result)
#  x,*y,z =numbers işlemine göre z nin küpü kaçtır
x,*y,z = numbers
result = z**3
print(result)

#  x,*y,z = numbers işlemine göre y nin değerleri toplamı kaçtır
x,*y,z= numbers
result=(y[0]+y[1]+y[2])
print(result)