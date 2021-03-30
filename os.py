import os #isletim sistemi ile ilgili bilgi sunar vve işletim sistemi ile alakalı  bilgi talebinde bulunmak için  yada klasörler hakkında bilgi klasör oluşturma adını değişme yada dosyalarla ilgili işlemleri path sınıfı üzerinden yapabiliriz
import datetime
result = dir(os)
result = os.name #hangi işletim sistemini kullandığımızı belirtir
#dizin değiştirme
os.chdir('c:\\') #şu andaki c dizini altında olduğumuzu belirtir
os.chdir('..//..')#bir üst dizinde olduğumuzu gösterir 
#klasör oluşturma
os.mkdir("newdirectory")#  aynı dizin üzerinnden klasör oluşturur
os.makedirs("newdirectors/yeniklasör")
os.rename("newdirectory"."yeni klasör")#newdirectory klasörün adını değiştirip yeni klasör yapar
os.rmdir("newdirevtoru") #klasör silme
os.removedirs("yeniklasör/yenikalsör")#alt dizin klasör silme
#listeleme
result= os.listdir()
result= os.listdir('c:\\')
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)
#etkin dizin öğrenme
result.os.getcwd()#ilgili dosya hakkında bilgi verir bu bilgi hangi klasör altında bulunduğunu gösterir
result=os.stat("_datetime.py")
result=result.st_size/1024
result.datetime.datetime.fromtimestamp(result.st_ctime)#oluşturulma tarihi
result.datetime.datetime.fromtimestamp(result.st_atime)#son erişilme tarihi
result.datetime.datetime.fromtimestamp(result.st_mtime)#değiştirilme tarihi
os.system("notpad.exe")
#path dosya uzanntisi değiştirme dosya adı değiştirme resim apload etme
result=os.path.abspath("_os.pay")#dosyanın konumunu verir
result=os.path.dirname("c:/python/advenced-modules/_os.py")#tam konumu verilen bir dosyanın dizin ismini verir
result=os.path.dirname(os.path.anspath("os.py"))#tam konumu bilinmeyen bir dosyayı dosya isminden dizin ismine ulaşmak
result=os.path.exists("_os.py")#böyle bir dosya olup olmadığunu sorgular bize true ve folse değerini döndürür
result==os.path.isdir("c:/python/advenced-modules")#ulaştığımız alan klasör mü dosyamı onu sorgular
result==os.path.isfile("c:/python/advenced-modules/_os.py")#ulaştığımız oalan bir dosya mı onu sorgular
result= os.path.join("c:\\","deneme")#resmi bir konuma gönderme
result.os.path.split("c:\\deneme")
result=os.path.splitext("_os.py")#uzantisiyla ismini ayırmaya yarar
print(result)
