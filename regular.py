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
result=result.end()#bhangi karakterden başladığını gösteriri
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
result=re.findall("[a-e]",str)



print(result)