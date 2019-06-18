import requests

listalibros=[]

search=str(input("¿Que libro estas buscando? "))    

payload = {'q' : search}
b = requests.get('http://openlibrary.org/search.json?', params=payload) 

if b.status_code == 200:
    datos=b.json()
    
    for i in datos["docs"]:
        print('Titulo:', i.get("title"))
        
#        print(type(i.get("isbn")))
        print("--- ISBN :")
        for isbn in i.get("isbn",[]):
            print(isbn)

        
#        print(type(i.get("author_name")))
        print("--- Autores:")
        for author in i.get("author_name",[]):
            print(author)
        print("-------------------------\n")

    

    