#Comando a usar para los contratos
from subprocess import Popen, PIPE

def lsArchivos():
	archivos = Popen(["ls","/home/filesystem_user/parciales/parcial1"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,archivos)

def deleteFiles(nomArchivo):
	vip=["comandos.py","comandos.pyc","files.py"]
	if nomArchivo not in vip:
		kill=Popen(["rm","-f","/home/filesystem_user/parciales/parcial1/"+nomArchivo], stdout=PIPE, stderr=PIPE)
		kill.wait()
		return True



def darArchivosRecientes():
	archivos = Popen(["find","-mtime","-1"], stdout=PIPE, stderr=PIPE)
	archivos1 = Popen(["grep","./"],stdin=archivos.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,archivos1)	
    	

def crearArchivo(nombre,contenido):
	nuevoArchivo= Popen(["touch",nombre], stdout=PIPE, stderr=PIPE)
	asignarContenido= Popen(['echo',contenido,'>>',"/home/filesystem_user/parciales/parcial1/"+nombre],shell=True, stdout=PIPE, stderr=PIPE)
	asignarContenido.wait()
	if nombre in lsArchivos():
		return True
