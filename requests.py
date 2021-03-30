import json
print(json.__file__)
import reguests #bu modül sayesinde HTTP ruguest, yapabiliriz
result=reguests.get("https://www.mynet.com")
result=rjson.loads(result.text)
for i in result:
    print(i["title"])

print(result[0][title])
print(type(result))