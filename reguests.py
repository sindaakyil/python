import reguests
import json
api_url_="https://api.exchangeratesapi.io/latest?base=USD "
bozulan_doviz=input("bozulan döviz turu")
alınan=doviz=input("alınan döviz türü")
miktar=int(input(f"ne kadar{bozulan_doviz}bozgurmak istiuorsunuz"))
result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)
print("1 {0}={1} {2}". format(bozulan_doviz,result["rates"]))