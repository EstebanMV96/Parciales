#PARCIAL 1

##Esteban Moya Vargas-13207005

###Antes de realizar la implementación de los servicios web, realicé lo siguiente:

1.) Cree el ambiente en el usuario filesystem_user:

	mkdir envs


	cd envs


	virtualenv flask_env

2.)Active el ambiente desde el directorio raiz de filesystem_user:


	. envs/flask_env/bin/activate
	

3.) Instale Flask:

	pip install Flask 

4.)Abrí el puerto requerido para implementar el servicio, yo eligí usar el 8080:

![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/iptables.PNG)
	
5.)Reinicie el servicio:
	
	
	service iptables restart

###Implementacion de los servicios web:

Comandos.py
```Python
#Comando a usar para los contratos
from subprocess import Popen, PIPE

def lsArchivos():
	archivos = Popen(["ls","/home/filesystem_user/Parciales/parcial1"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,archivos)

def deleteFiles(nomArchivo):
	vip=["comandos.py","comandos.pyc","files.py"]
	if nomArchivo not in vip:
		kill=Popen(["rm","-f","/home/filesystem_user/Parciales/parcial1/"+nomArchivo], stdout=PIPE, stderr=PIPE)
		kill.wait()
		return True



def darArchivosRecientes():
	archivos = Popen(["find","-mtime","-1"], stdout=PIPE, stderr=PIPE)
	archivos1 = Popen(["grep","./"],stdin=archivos.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,archivos1)	
    	

def crearArchivo(nombre,contenido):
	nuevoArchivo= Popen(["touch",nombre], stdout=PIPE, stderr=PIPE)
	nuevoArchivo.wait()
	file=open(nombre,"w")
	file.write(contenido)
	file.close()
	if nombre in lsArchivos():
		return True


```

Files.py

```Python
from flask import Flask, abort, request
import json, time
from comandos import lsArchivos, deleteFiles,darArchivosRecientes, crearArchivo
app = Flask(__name__)

@app.route('/files',methods=['GET'])
def darArchivos():
  list = {}
  list["files"] = lsArchivos()
  return json.dumps(list), 200

@app.route('/files',methods=['DELETE'])
def eliminarArchivos():
	
	for i in lsArchivos():
		deleteFiles(i)
			
	return "Todos los archivos no VIP fueron borrados",200

@app.route('/files/recently_created',methods=['GET'])
def recently():
  list = {}
  list["Archivos creados hace menos de un dia"] = darArchivosRecientes()
  return json.dumps(list),200
  
@app.route('/files',methods=['POST'])
def newArchivo():
  content = request.get_json(silent=True)
  nombreA = content['filename']
  contenido= content['content']
  if crearArchivo(nombreA,contenido):
  	return "Archivo creado",201
  
@app.route('/files/recently_created',methods=['POST'])
def recently3():
 
  return "No implementado",404

@app.route('/files/recently_created',methods=['PUT'])
def recently1():
 
  return "No implementado",404

@app.route('/files/recently_created',methods=['DELETE'])
def recently2():
 
  return "No implementado",404

@app.route('/files',methods=['PUT'])
def recently5():
 
  return "No implementado",404

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080,debug='True')

```

###Capturas de Pantalla de la solución

####/files Peticion GET

![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_get.png)

####/files Peticion POST

![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_post.PNG)
![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_post_2.PNG)

####/files Peticion DELETE
![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_deleted.PNG)
![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_deteled2.PNG)

####/files/recently_created Peticion GET
![Log](https://github.com/EstebanMV96/Parciales/blob/master/Imagenes/files_recently_created_get.PNG)


##URL=https://github.com/EstebanMV96/Parciales
