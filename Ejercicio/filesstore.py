
#RECUERDA! Se tiene que descargar el archivo .JSON (Este se descarga desde firebase) y agregar en variable de entorno 
# y se nombra a la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
# posibles errores, recuerda buscar tu archivo desde carpeta y que aparezca el .json

#Mandamos a llamar a firestore de la nube de google
from google.cloud import firestore
from firebase_admin import credentials
import firebase_admin
import os

#Creamos variable de entorno y la mandamos a llamar con os
cred = credentials.Certificate(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
default_app = firebase_admin.initialize_app(cred)

#Llamada al cliente firestore
db = firestore.Client()

# Note: Use of CollectionRef stream() is prefered to get()
query = db.collection(u'comercios_dev').stream()

#Realizamos una consulta básica
for i in query:
 print(f'{i.id} => {i.to_dict()}')

#NOTA: Cuando se tengan diferentes llaves .json, es importante cambiar a la indicada, no se pueden vincular todas juntas 
# Solo una por una

