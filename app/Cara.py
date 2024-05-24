#uso del algoritmo de Viola-Jones
import cv2

# Cargar el clasificador preentrenado para caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen donde se detectarán las caras
image = cv2.imread('img/imagen1.png')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=6, minSize=(20, 20))

# Dibujar rectángulos alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()