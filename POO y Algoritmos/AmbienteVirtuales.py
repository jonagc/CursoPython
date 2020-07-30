"""
Permite aislar el ambiente para poder instalar diversas de paquetes.
A partir de python 3 se incluye en la libreria estandar en el modulo venv.
Ningun ingeniero profesional de python trabaja sin ellos.

PIP:

Permite descargar paquetes para utilizar en nuestro programa.
Permite compartir nuestro paquetes con terceros.
Permite especificar la version del paquete  que necesitamos.´

Se ejecuta en consola windows:
1.- crear directorio con mkdir
2.- instalar virtualenv: py -m pip install virtualenv                   
3.- crear ambiente virtual: py -m venv nombre_espacio_virtual
4.- activar espacio virtual: nombre_espacio_virtual\Scripts\activate.bat
5.- Instalar libreria: pip install nombre_libreria (ejemplo bokeh)

nota: puede usarse py o python. Estos comandos con para CMD

Para linux:
1.- crear directorio con mkdir                  
3.- crear ambiente virtual: python3.7 -m venv nombre_espacio_virtual
4.- activar espacio virtual: source nombre_espacio_virtual\bin\activate
5.- Instalar libreria: pip install nombre_libreria (ejemplo bokeh)

indica las librerias instaladas: pip freeze 
salir ambiente virtual: deactivate

libreria flask = servidor 

pip install flask

"""


