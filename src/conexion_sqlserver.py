import pyodbc
import requests
import json
from pprint import pprint

try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-BC112OPN\SQLEXPRESS;DATABASE=MarvelAPI;Trusted_Connection=yes')
    print("Conexion exitosa")
except Exception as ex:
    print(ex)



#---------------------Metodos para la insercion a la base de datos------------------#
def insertCharacters(nameC, descriptionC, comics_availableC,idImagenC):
    cursor = connection.cursor()
    query = f"INSERT INTO marvel_characters(nombre, descripcion, comics_available,idImg) values ('{nameC}', '{descriptionC}', '{comics_availableC}','{idImagenC}')"
    cursor.execute(query)
    cursor.close()


def insertThumbnail(descriptionT):
    cursor = connection.cursor()
    query = f"INSERT INTO thumbnail(descripcion) values ({descriptionT}) "
    cursor.execute(query)
    cursor.close()

def insertStories(descSt):
    cursor = connection.cursor()
    query = f"INSERT INTO stories(descripcion) values ({descSt}) "
    cursor.execute(query)
    cursor.close()
#---------------------Metodos para la insercion a la base de datos------------------#



#---------------------Llamado y consumo del API de Marvel------------------#
ts=1
private_key="58f0fe9954dacd060e14365755f7d041158eb6d0"
public_key="5f9273485ee671e7b57e232b05cbe581"

hashed = "979e7a0a4be770d3c5dfb3a78bf17771"

url = f"https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hashed}"

#---------------------Llamado y consumo del API de Marvel------------------#

#---------------------Creo un objeto lista para verificar que si haga el llamado correcto------------------#
lista = []


#---------------------Llamado y consumo del API de Marvel a traves del get------------------#
response = requests.get(url)


#---------------------Verifico qque el llamado sea el correcto para continuar------------------#
if response.status_code==200:
    response_json = json.loads(response.text)
#---------------------Recorro los datos que traigo a traves del get y extraigo solo los que seleccioné------------------#
    for i in response_json["data"]["results"]:
        id = i["id"]
        nombre = i["name"]
        descripcion = i["description"]
        comics_disponibles = i["comics"]["available"]
        series_disponibles = i["series"]["available"]
        image = i["thumbnail"]["extension"]
        stories = i["stories"]["available"]
#---------------------Hago la insersión de los datos a la base de datos a traves de los metodos previamente creados------------------#
        insertStories(stories)
        insertThumbnail(image)
        insertCharacters(nombre, descripcion, comics_disponibles, 1)

        #---------------------Agrego algunos datos a la lista para probar que si esta funcionando el llamado------------------#
        arr = {"nombre":nombre,"descripcion":descripcion,"comics_disponibles":comics_disponibles,"series_disponibles":series_disponibles, "imagen":image}
        #---------------------Inserto en la lista------------------#
        lista.append(arr)
        #---------------------Imprimo la lista para ver el llamado------------------#
# #print(lista)
