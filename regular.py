import re#genel olarak arama sonucunda bir sonuç döndrür 
result=dir(re)

#re module
str="python kursu:pytnon programlama rehberi"
#re.findall()
result=re.findall("python",str) #str içinde arama yaparak python kelimesini arar
result=len(result)#kaçtane python kelimesi var onu bulur
#re.split()
result=re.split(" ",str)#str içindeki kelimeleri boşluk karakterinden bölerek listeler
#re.sub:()
result=re.sub(" " ,"-",str)#str deki boşluk karakterlerin hepsini - işareti ile değiştir
#re.search()
result=re.search("python",str)#python kelimesini bulup konumunu gösterir
result=result.start()#bhangi karakterden başladığını gösteriri
result=result.end() #bhangi karakterden başladığını gösteriri
result=result.group()
result=result.string #arama işlemini hangi stringde yaptığımızı gösterir



#regular expression
"""
[]-köşeli parantezler arasına yazılan bütün karakterler aranır
[abc]=> a      :1 match
        ac     :2 match
        python :no matches
[a-e]=>[abcde]
[1-5]=>[12345]
[0-39]=>[01239]
[âbc]=>abc dışındaki karakterler
[^0-9]=>rakam olmayan karakterler
"""
result=re.findall("[abc]",str)
result=re.findall("[sat]",str)
result=re.findall("[a-e]",str)# ilgili string içindeki adan e ye kadar lan bütün karakterleri bulur
"""
. - her hangi bir karakteri belirtir
   ..=>a     :no match
       ab    :1 match
       abc   :1 match
       abcd  :2 marches

"""
result=re.findall("...",str)#string grupları 3 lü gruplara ayırarak bize geri döndürür
result=re.findall("py..on",str)
"""
 ^-belirtilen karakterle başlıyor mu*
 â=>a:    1 match
    abc:  1 match
    bac:  no match
"""
result=re.findall("^p",str)
"""
§- belirtilen karakterle bitiyor mu?
a§=>a    :1 match
    lamba:1 match
    python:no match
"""
result=re.findall("t§",str)
"""
* - bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder
 ma*n= mn   :1 match
       man  :1 match
       maaan:1 match
       main:no match()
"""
result=re.findall("sa*t",str)

"""
+ - bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder
 ma+n= mn   :1 match
       man  :1 match
       maaan:1 match
       main:no match(a'nın arkasına n gelmiyor)
"""
result=re.findall("sa+t",str)
"""
? - bir karakterin sıfır ya da 1 kez  olmasını kontrol eder
 ma?n= mn   :1 match
       man  :1 match
       maaan:1 match
       main:no match(a'nın arkasına n gelmiyor)
"""
result=re.findall("sa?t",str)

"""
   {}- karakter sayısını kontrol eder.
   al{2}=> a karakterinin arkasını l karakteri 2 kez tekrarlanmalı
   al{2,3}=>a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlanmalı
   [0-9]{2,4}=>en az 2 en çok 4 basamaklı sayılar
"""
result=re.findall("a{2}",str)
result=re.findall("[0-9]{2}",str)

"""
| - alternatif seçeneklerden birinin gerçekleşmesi gerekir
a|b=> a yada b
 cde=>  nno match
 ade=> 1 match
 acdbea=>3 match
"""












print(result)