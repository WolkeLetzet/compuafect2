# Set Up

1. Build Imagen

Para construir la imagen apartir de **DockerFile** se debe ingresar el siguiente comando en la carpeta del proyecto.
Se construira una imagen con el nombre de face-recog-python

```
docker build -t face-recog-python .
```

2. Crear Volumen

Crear el volumen para el contenedor y guardar los datos

```
docker volume create face_recog_vol
```

3. Iniciar Contenedor

Para iniciar un contendor a partir de la imagen creada y usar el puerto 8888

```
docker run --rm -p 8888:8888 -v face_recog_vol:/app/img face-recog-python
```
