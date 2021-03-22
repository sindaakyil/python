
#iteration elemanlar üzerinde tek tek dolaşmamızı sağlar for'a benzetebiliriz


liste = [1,2,3,4,5,6]
for i in liste:
    print(i)
print(dir(liste))
liste = [1,2,3,4,5,6]
iterator = iter(liste)
print(next(iterator))#tek tek liste üzerindeki elemanları yazar
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = iter(liste)
while true:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:
        break
    #list gibi bir classı kendimiz yapmak için iteration kullanırız
class MyNumbers:
    def__init__(self,start,stop)
       self.start = start 
       self.stop = stop
    def__iter__(self):
        return self
    def__next__(self):
        if self.start <= self.stop:
            x=self.start
            sef.start+=1
            return x
        else:
            raise StopIteration
list=MyNumbers(10,20)
myiter =iter(list)
print(next(myiter))
for x in list:
    print(x)



