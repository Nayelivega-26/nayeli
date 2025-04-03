import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


imagen = cv2.imread('ruta_a_tu_imagen.jpg')

gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Rostros detectados', imagen)


cv2.waitKey(0)
cv2.destroyAllWindows()
