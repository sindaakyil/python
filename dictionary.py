sehirler = ['kocaeli','istanbul']
plakalar = [41,34]
print(plakalar[sehirler.index('istanbul')])
plakalar = {'kocaeli': 41, 'istanbul' : 34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])


plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'
print(plakalar)



users = {
'sadikturan':{
'age' 36 ,
'email':'sadikturn@gmail.com',
'adress':'kocaeli',
'phone': 224224342
},
'cinarturan': 
{
'age' 2 ,
'email':'çınarturn@gmail.com',
'adress':'kocaeli',
'phone': 224224342
}

}
print(users['cinarturan']['age'])