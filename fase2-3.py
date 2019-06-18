import requests

listado=[]

print("Obtener libros de una lista")
user=str(input("¿Que usuario buscas?: "))  
libro=str(input("¿Que lista busca?: "))

u = requests.get('http://openlibrary.org/people/%s/lists/%s/seeds.json' % (user,libro)) 
#ejemplo OL97L
if u.status_code == 200:
    datos=u.json()
        
    for i in datos["entries"]:
        print('Titulo: ', i.get("title"))
        
        print('FULL URL: ', i.get("full_url")) 
        
        print('Ultima actualización: ', i.get("last_update"))
        
        print('FotoLibro: ', i.get("picture"))
        
        print("-------------------------\n")
