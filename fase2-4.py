import requests

print("Creación de lista")
user=str(input("Usuario: "))  


json_project="""
{
    "name": "Lista de prueba",
    "description": "Studies of architectural practice, mainly English works",
    "tags": ["Architecture", "18th Century", "Drawings", "Buildings"],
    "seeds": [
        "/books/OL1M",
        "/subjects/gothic_architecture"
    ]
}
"""

headers = {'Content-Type': 'application/json'}
u = requests.post('http://openlibrary.org/people/%s/lists' % user , data=json_project,headers=headers) 

if u.status_code == 201:
    print ("ok")
else:
    print ("Error: "+str(u.status_code)+"\n"+u.text)