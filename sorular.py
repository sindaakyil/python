website ="http://wwww.sindaakyill.com"
course ="python kursu:baştan sona python kursu"
#soru 1 ) 'course' karakter dizisinde kaç karakter bulunmaktadır.


# result = len(course)
# print(result)
# lenght = len(website)

#soru 2)'web site'içinden wwww karakterlerini alın

# result = website[7 :10]
# print(result)

#soru3) website içinden com karakterini alın.

# result =website [ lenght-3: lenght]   
# print(result)

#soru4) 'course ' içinden  ilk 15 ve son 15 karakterlerini alın
# lenght = len(course)
# result = course [ 0 :15 ]
# result =course [lenght -15 : lenght]
# print(result)

# soru5)course ifadesindeki karakterleri tersten yazınız
#  course ='python kursu:baştan sona python kursu'
#  result = course [::-1]
#   print(result)

# name = 'şinda'
# surname = 'akyıl'
# age = 25
# job = 'mühendis'
# print(f"benim adım'{name} {surname} yasım {age} mesleğim {job}")

# soru 6) ' hello world 'karakter dizisinin baş ve sondaki boşluk karakterlerini silin
 
# result = "        hello world ".strip()
# print(result)

# soru 7 )wwww.sindaakyil.com içindeki sindaakyil haricinndeki tüm bilgiyi silin

#  result = "http://wwww.sindaakyil.com" .strip('http://')
#  print(result)
#soru8) 'course' karakter dizisinin tüm karakterlerini büyük karf yapın
# course = course.upper()
# print(course)
# soru 9) website içerisinde kaç tane a harfi var bulalım

result = website.count('a')
print(result)