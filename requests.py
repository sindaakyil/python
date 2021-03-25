import json
print(json.__file__)
import reguests #bu modül sayesinde HTTP ruguest, yapabiliriz
result=reguests.get("https://www.mynet.com")
print(result)