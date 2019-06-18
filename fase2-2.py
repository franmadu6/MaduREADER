import requests

listausers=[]

print("Listado de las listas de un usuario")
user=str(input("¿Que usuario buscas?: "))    

u = requests.get('http://openlibrary.org/people/%s/lists.json' % user) 

if u.status_code == 200:
    datos=u.json()
    
    for i in datos["entries"]:
        print('Nombre: ', i.get("name"))
        
        print("Libros:", i.get("seed_count",[]))
        
        print("Recuento de ediciones: ", i.get("edition_count",[]))
            
        print('URL:', i.get("url"))

        print('FULL URL: ', i.get("full_url"))
        
        print('Ultima actualización: ', i.get("last_update"))

        print("-------------------------\n")
