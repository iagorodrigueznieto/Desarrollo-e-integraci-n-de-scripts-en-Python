# Desarrollo e integracion de Scripts en Python

## Iniciar MongoDB con Docker

![alttext](https://cdn-icons-png.flaticon.com/256/919/919853.png)
Si no tienes docker, [descargalo e instálalo.](https://www.docker.com/products/docker-desktop/)

A continuacion abre una terminal (o consola de comandos) y ejecuta el siguiente comando para levantar un contenedor de MongoDB:
`docker run -d --name mongo -p 27017:27017 mongo:latest`

Si quieres verificar que el conteneder está corriendo: 
`docker ps`



