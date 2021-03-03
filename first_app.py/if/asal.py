#girilen bir sayının asal olup olmadığını bulun
sayi=int(input('sayıyı giriniz'))

for a in range(2,sayi,1):
   
    if sayi%a==0:
        print(f'sayi asal değil sayıya bölündü :{a}')
        break
    else:
        print('asal sayi')

sayi=int(input('sayıyı giriniz'))
fak=1
a=1
for a in range(2,(sayi+1)):
    a+1
    fak*=a
print(fak)
        
    