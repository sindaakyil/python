import os #isletim sistemi ile ilgili bilgi sunar vve işletim sistemi ile alakalı  bilgi talebinde bulunmak için  yada klasörler hakkında bilgi klasör oluşturma adını değişme yada dosyalarla ilgili işlemleri path sınıfı üzerinden yapabiliriz
result = dir(os)
result = os.name #hangi işletim sistemini kullandığımızı belirtir
#dizin değiştirme
os.chdir('c:\\') #şu andaki c dizini altında olduğumuzu belirtir
os.chdir('..//..')#bir üst dizinde olduğumuzu gösterir 
#klasör oluşturma
os.mkdir("newdirectory")#  aynı dizin üzerinnden klasör oluşturur
os.makedirs("newdirectors/yeniklasör")
#etkin dizin öğrenme
result.os.getcwd()#ilgili dosya hakkında bilgi verir bu bilgi hangi klasör altında bulunduğunu gösterir

#listeleme
result= os.listdir()
result= os.listdir('c:\\')
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)
print(result)
