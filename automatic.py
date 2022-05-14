import subprocess
nombre = input("Que nombre tendra la pagina?/ What name will the proyect have?")
dirName= "../"+nombre
html = "type nul > "+nombre+".html"
css = "type nul > "+nombre+".css"
js = "type nul > "+nombre+".js"
htmlFormat='''^<!DOCTYPE html^>|^<html^>|^<head^>|	^<meta charset="utf-8"^>|	^<meta http-equiv="X-UA-Compatible" content="IE=edge"^>|	^<meta name="viewport" content="width=device-width, initial-scale=1"^>|	^<title^>'''+nombre+'''^</title^>|	^<link rel="stylesheet" href="'''+nombre+".css"+'''"^>|	^<script src="'''+nombre+".js"+'''" type="text/javascript" async defer^>^</script^>|^</head^>|^<body^>◙|^</body^>|^</html^>'''
lineas = htmlFormat.split("|")
subprocess.run(["md",nombre],shell=True,cwd='..')#crea la carpeta
subprocess.run(["cd",nombre],shell=True,cwd='..')#entra a la carpeta
subprocess.run(html,shell=True,cwd=dirName)#crea un archivo html
subprocess.run(css,shell=True,cwd=dirName)#crea un archivo css
subprocess.run(js,shell=True,cwd=dirName)#crea un archivo js
for linea in lineas:
	echo = 'echo '+linea+' >> '+nombre+'.html'
	subprocess.run(echo,shell=True,cwd=dirName)#le da formato al html