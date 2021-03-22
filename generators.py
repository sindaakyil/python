def coube():
    result=[]
    for i in range(1,5,1):
        result.append(i**3)
    return result
print(coube())
#generators kullanmamızın nedeni eğer oluşturduğumuz bir değeri bir liste içinde saklamak gerekmıyorsak sadece o an ulaşmak istiyorsak daha sonra o elemana ulaşmamız gerekmiyorsa kullanılır.
def cube():
    for i in range(5):
        yield i**3
generator = cube()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
def cube():
    for i in range(5):
        yield i**3
iterator= cube()
for i in iterator:
    print(i)
def cube():
    for i in range(5):
        yield i**3

for i in cube():
    print(i)