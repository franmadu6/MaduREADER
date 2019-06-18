from flask import Flask
from flask import render_template,request,abort

import requests
import json
import os

app = Flask(__name__, template_folder="templates")

#---------pg de inicio
@app.route('/',methods=["GET"])
def inicio():
    return render_template("base.html",error= None)

#----------pg libros
@app.route('/libros',methods=["GET","POST"])
def oblibros():
    
    return render_template('free.html',error= None)

@app.route('/free2',methods=["GET","POST"])
def oblibros2():
    search=request.form.get("libro")
    print (search)
    
    payload = {'q' : search}
    b = requests.get('http://openlibrary.org/search.json?', params=payload) 

    if b.status_code == 200:
        datos=b.json()
    
        listatit=[]
        listaisbn=[]
        listaaut=[]
        listapub=[]
        listaleng=[]
        listaenlc=[]
    
        for i in datos["docs"]:
            listatit.append(i.get("title"))
        
            listaisbn.append(i.get("isbn","Desconocido"))
    
            listaaut.append(i.get("author_name","Desconocido"))
        
            listapub.append(i.get("publisher","Desconocido"))
            
            listaleng.append(i.get("language","Desconocido"))
        
            listaenlc.append(i.get("key","Desconocido"))
        
        return render_template('free2.html',title=listatit,isbn=listaisbn,author=listaaut,pub=listapub,leng=listaleng,key=listaenlc)
    else:
        abort(404)
        
    
#-----------pg usuarios
@app.route('/usuario',methods=["GET","POST"])
def obusuario():
        
    return render_template('usuario.html',error= None)

@app.route('/usuario2',methods=["GET","POST"])

def obusuario2():
    usuario=request.form.get("usuario")
    print (usuario)
    
    b = requests.get('http://openlibrary.org/people/%s/lists.json' % usuario) 

    if b.status_code == 200:
        entradas=b.json()
    
        listaname=[]
        listaseed=[]
        listarecuent=[]
        listaurl=[]
        listafullurl=[]
        listalastupdate=[]
    
        for i in entradas["entries"]:
            listaname.append(i.get("name"))
        
            listaseed.append(i.get("seed_count","Desconocido"))
    
            listarecuent.append(i.get("edition_count","Desconocido"))
        
            lurl=i.get("url","Desconocido")
            lurl=lurl.split("/")
            listaurl.append(lurl)
            
            listafullurl.append(i.get("full_url","Desconocido"))
            
            listalastupdate.append(i.get("last_update","Desconocido"))
            

        return render_template('usuario2.html',name=listaname,seed_count=listaseed,edition_count=listarecuent,url=listaurl,full_url=listafullurl,last_update=listalastupdate)
    else:
        return render_template('error.html')

#-----------pg listas
#@app.route('/listas',methods=["GET","POST"])
#def oblistas():
        
#    return render_template('listas.html',error= None)

@app.route('/listas/<usuario>/<libro>',methods=["GET","POST"])
def oblistas2(usuario,libro):
#    usuario=request.form.get("usuario")
#    libro=request.form.get("libro")

    
    b = requests.get('http://openlibrary.org/people/%s/lists/%s/seeds.json' % (usuario,libro)) 

    if b.status_code == 200:
        entradas=b.json()
    
        listatitl=[]
        listafullurl=[]
        listalast=[]
        listapic=[]
    
        for i in entradas["entries"]:
            listatitl.append(i.get("title"))
        
            listafullurl.append(i.get("full_url","Desconocido"))
        
            listalast.append(i.get("last_update","Desconocido"))
            
            url=i.get("picture",{})
            url=url.get("url","")
            
            print(url)
            if url!=None:
                url=url[2:]
            listapic.append(url)
            
#.split("'")[3][2:]
        
        return render_template('listas2.html',title=listatitl,full_url=listafullurl,last_update=listalast,picture= listapic,usuario=usuario,libro=libro)
    else:
        return render_template('error.html')

#-----------pg  lista mr
@app.route('/listamr',methods=["GET","POST"])
def oblistasmr():
        
    return render_template('listasmr.html',error= None)
#-----------listamr/tema
#OL135747L cuentos
#OL135750L novelas
#OL135749L terror
#OL136133L poesía
@app.route('/temas',methods=["GET","POST"])
def listatemas():
    mr = request.form.get("temas")
    b = requests.get('http://openlibrary.org/people/franmadu/lists/%s/seeds.json' % mr) 

    if b.status_code == 200:
        datos=b.json()
    
        listatitl=[]
        listaseed=[]
        listarecuent=[]
        listaurl=[]
        listafullurl=[]
        listalastupdate=[]
    
        for i in datos["entries"]:
            listatitl.append(i.get("title"))
        
            listaseed.append(i.get("seed_count","Desconocido"))
    
            listarecuent.append(i.get("edition_count","Desconocido"))
        
            listaurl.append(i.get("url","Desconocido"))
            
            listafullurl.append(i.get("full_url","Desconocido"))
            
            listalastupdate.append(i.get("last_update","Desconocido"))

        return render_template('listatemas.html',title=listatitl,seed_count=listaseed,edition_count=listarecuent,url=listaurl,full_url=listafullurl,last_update=listalastupdate)
    else:
        return render_template('error.html')
    
#-----------pg  google
@app.route('/google',methods=["GET","POST"]) 

def obgoogle():
        
    return render_template('google.html',error= None)

#-----------pg buscador google
@app.route('/google2',methods=["GET","POST"])
def obgoogle2():
    search=request.form.get("googlelibros")
   
    payload = {'q' : search}
    b = requests.get('https://www.googleapis.com/books/v1/volumes?', params=payload) 

    if b.status_code == 200:
        datos=b.json()
    
        listatit=[]
        listaautor=[]
        listapublished=[]
        listapublishedDate=[]
        listapdf=[]
        listadef=[]
        listaleng=[]
        listaimg=[]
    
        for i in datos["items"]:
            listatit.append(i["volumeInfo"].get("title"))
            
            
            listaautor.append(i["volumeInfo"].get("authors","Desconocido"))
        
            listapublished.append(i["volumeInfo"].get("publisher","Desconocido"))
    
            listapublishedDate.append(i["volumeInfo"].get("publishedDate","Desconocido"))
        
            listapdf.append(i["accessInfo"].get("webReaderLink","Desconocido"))
            
            listadef.append(i["volumeInfo"].get("description","Desconocido"))
        
            listaleng.append(i["volumeInfo"].get("language","Desconocido"))
            
            listaimg.append(i["volumeInfo"]["imageLinks"].get("smallThumbnail","Desconocido"))
        
        return render_template('google2.html',title=listatit,autor=listaautor,published=listapublished,date=listapublishedDate,pdf=listapdf,defin=listadef,leng=listaleng,img=listaimg)
    else:
        return render_template('error.html')

#activar estas lineas para que vaya en heroku.
if __name__ == '__main__':
    port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)

#activar esta linea para que vaya en la termial.
#app.run(debug=True)
