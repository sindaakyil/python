import datetime # dersek datetime ait olan bütün classlara ulaşmış oluruz
result = dir(datetime)
print(result)
from datetime import datetime# tek bir classa  ulaşmış oluruz
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
result=dir(datetime.datetime)
result=dir(datetime.time)
result=dir(datetime.date)
print(result)
from datetime import datetime
simdi=datetime.now()
result=datetime.now()
result=datetime.now().day
result=simdi.minute
result=simdi.hour
result=datetime.strftime(simdi,'%Y')#bize ilgili yılı yazar,
result=datetime.strftime(simdi,'%X')#bize saat bilgisini verir
result=datetime.strftime(simdi,'%d')#bize günn bilgisini verir
result=datetime.strftime(simdi,'%A')#bize gün bilgisini string olarak verir
result=datetime.strftime(simdi,'%B')#bize aybilgisini string olarak verir
result=datetime.strftime(simdi,'%Y %B %A')#bize ilgili ygün ve ay bilgisini string olarak verir 
print(result)
t='21 nisan 2019'
gun,ay , yil=t.split()
print(gun)
print(ay)
print(yil)
t='15 April 2019 hour 10:12:56'
dt=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)
birthday = datetime(1993,5,9)
print(birthday)
result=datetime.timestamp(birthday) #saniye bilgisini verir
result=datetime.fromtimestamp(result)#saniye bilgisini tarihe çevirir

result=datetime.fromtimestamp(0)#1970 tarihini getirir bilgisyarların miladı olarak 1970 yılı baz alınmıştır.
result = simdi- birthday # timedelta yapıo yanı iki tarih arasında gün farkını bize verir
result= result.days
print(result)
print(simdi)
result=simdi+timedelta(days = 10)
result=simdi+timedelta(days= 260)



print(result)