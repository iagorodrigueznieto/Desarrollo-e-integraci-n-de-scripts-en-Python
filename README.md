# Desarrollo e integracion de Scripts en Python

  

## :wrench:Iniciar MongoDB con Docker

  

![alttext](https://cdn-icons-png.flaticon.com/256/919/919853.png)

  

Si no tienes Docker, [descárgalo e instálalo.](https://www.docker.com/products/docker-desktop/)

  

A continuación abre una terminal (o consola de comandos) y ejecuta el siguiente comando para levantar un contenedor de MongoDB:

  

    docker run -d --name mongo -p 27017:27017 mongo:latest

  

Si quieres verificar que el contenedor está corriendo:

    docker ps

  
  

## :rocket:Ejecución de scripts de Python

  

Para la ejecución de los scripts es necesario tener instalado Python, y algún gestor de paquetes como por ejemplo conda.

Puedes descargar conda [aquí](https://docs.anaconda.com/miniconda/install/#quick-command-line-install).

  

Ya habiendo instalado conda, podremos crear un entorno a partir del exportado presente en el repositorio a través de este comando ejecutado en la terminal.

  

    conda env create -f requirements.yaml

  

Se creará un entorno ya con librerías necesarias para ejecutar los scripts del repositorio.

  
  


### Primer Script

  

El primer script presente en el repositorio se encarga de conectarse a una [api]("http://api.citybik.es/v2/networks/bicicorunha") y almacenar los datos extraídos en una base de datos mongo.

Para ejecutar el script en la terminal:

    python script1.py
Para verificar que los datos están insertados correctamente en la terminal escribe. 

    docker exec -it nombre_tu_contenedor mongosh
    use city
    db.bikes.find()

