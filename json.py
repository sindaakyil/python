import json



#json cihazlar arasında ortak veri taşıma objesi
#dictinary
person ={"name":"ali","languages":["python","c#"]}
result=person["name"]
result=person["languages"]
result=person["languages"][0]
#json olarak kullanmak için string ifadeye çevirip daha sonra dctionary yapısına çevirmemmiz gerekiyor
person ='{"name":"ali","languages":["python","c#"]}'
#JSON string to Dict
result = json.loads(person_string)#dictionary çevirmiş oluruz
result=result["name"]
result=result["languages"]

with open("person.json") as f:#dosyanın içindeki bilgileri okur ve bilgisayara yazdırır
    data=json.load(f)
    print(data)
with open("person.json") as f:#dosyanın içindeki bilgileri okur ve bilgisayara yazdırır
    data=json.load(f)
    print(data["name"])# dosyanın içinde bulunan ismi getirir
    print(data["languages"])

person_dict= {
    "name":"ali",
    "languages":["python","c#"]
}

result = json.dumps(person_dict)#dictionary yi json modülüne çevirir

with open("person.json","w") as f: #dosyayı yazma modunda aç 
    json.dump(person_dict,f)

person_dict=json.loads(person_string)
result= json.dumps(person_dict,indent=4,sort_keys=true)
print:(person_dict)
print(result)



print(result)