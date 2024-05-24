"""
Este script utiliza Dlib junto con OpenCV para cargar una imagen, 
detectar rostros, y luego ubicar y marcar 68 puntos faciales 
distintos que representan varias regiones clave del rostro,
 como los bordes de los ojos, la nariz, la boca y la mandíbula.
"""

import dlib
import cv2

# Cargar el detector de rostros de Dlib
detector = dlib.get_frontal_face_detector()

# Cargar el predictor de puntos faciales preentrenado
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Cargar una imagen usando OpenCV
image = cv2.imread("img/imagen2.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
faces = detector(gray)

# Loop sobre cada rostro detectado
for face in faces:
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    # Dibujar un rectángulo alrededor del rostro
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Usar el predictor para encontrar los puntos faciales
    landmarks = predictor(gray, face)

    # Dibujar los puntos faciales en la imagen
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 4, (255, 0, 0), -1)


# Mostrar la imagen con los rostros detectados
cv2.imwrite("img/imagen1_rostros.png", image)
