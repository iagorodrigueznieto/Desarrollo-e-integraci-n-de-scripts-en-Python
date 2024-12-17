# Desarrollo e integracion de Scripts en Python

## Iniciar MongoDB con Docker

![alttext](https://cdn-icons-png.flaticon.com/256/919/919853.png)

Si no tienes docker, [descargalo e instálalo.](https://www.docker.com/products/docker-desktop/)

A continuacion abre una terminal (o consola de comandos) y ejecuta el siguiente comando para levantar un contenedor de MongoDB:

`docker run -d --name mongo -p 27017:27017 mongo:latest`

Si quieres verificar que el conteneder está corriendo:
 
`docker ps`


 ## Ejecución de scripts de python

Para la ejecución de los scripts es necesario tener instalado python, y algún gestor de paquetes como por ejemplo conda. 
Puedes descargar conda [aquí](https://docs.anaconda.com/miniconda/install/#quick-command-line-install).

Ya habiendo instalado conda, podremos crear un entorno a partir del exportado presente en el repositorio a través de este comando ejecutado en la terminal. 

`conda env create -f requirements.yaml`

Se creará un entorno ya con librerías necesarias para ejecutar los scripts del repositorio. 


### Primer Script

El primer script presente en el repositorio se encarga de conectarse a una [api]("http://api.citybik.es/v2/networks/bicicorunha") y almacenar los datos extraídos de la anterior api para 



