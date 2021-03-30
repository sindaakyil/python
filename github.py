import reguests 
import json
class Github:
    def __init__(self):
        self.api_url='http://api.github.com'
    def getUser(self,username):
        response = requests.get(self.api_url+'/users'+username)
        return response.json()
github =Github




while True:
    secim=input('1-find user\n2-Get Repositories\n3-Create Repository\n4- Exit\nSeçim:')
    if secim =='4':
        break
    elif secim =='1':
        username= input ('username: ')
        result = github.getUser(username)
        print(f"name:{result[name]} public repos: {result['public_repos']} followers : {result['follawers']}")
    elif secim =='2':
        pass
    elif secim=='3':
        pass
    else:
        print:('yanlış secim')