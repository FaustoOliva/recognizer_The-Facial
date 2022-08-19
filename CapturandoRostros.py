import cv2
import os
import imutils
from post.getAlumno import get_alumno

while True:
    print("¿Legajo del alumno? Aclaracion, pongalo entre comillas simples")
    legajo = input()

    alumno = get_alumno(legajo)
   
    if alumno: 
        print(alumno)
        break
    else:
        print('No existe el legajo ingresado')


personName = legajo
characters = "'"

personName = ''.join( x for x in personName if x not in characters)
print(personName)
dataPath = 'C:/Users/devandroid/Desktop/recognizer_The-Facial/Data'#Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)


legajoPath = 'C:/Users/devandroid/Desktop/recognizer_The-Facial/Legajos'#Cambia a la ruta donde hayas almacenado Data
legajoPath = legajoPath + '/' + personName 


if not os.path.exists(legajoPath):
    print('Carpeta creada: ',legajoPath)
    os.makedirs(legajoPath)

#Lineas 5 - 11
#Se crea y posiciona en la carpeta en donde se guardaran las inscripciones del video/stream que se realize 
try:
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Captura video streaming. 0 => camara default
    #cap = cv2.VideoCapture('Video.mp4')
except:
    print('Falló conexion de camara.')

    
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)
#24 - 30
#Lee los frames y redimensiona el tamaño del video


    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC) #150,150 => tamaño de los cortes
        cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
        count += 1
    cv2.imshow('frame',frame)
#35 - 41
#Muestra un rectangulo en el streming y fija el tamaño de las inscripciones
   

    k =  cv2.waitKey(1)
    if k == 27 or count >= 50:
        break
#46-48
#Hace 300 inscripciones (aprox 30seg)y se rompe cuando llega a esa cantidad de imagenes o cuando se presiona 'Esc' (27)
cap.release()
cv2.destroyAllWindows()

#Variables
#26 (640) 38 (150,150) 47 (300)

#Ejecutar Python 'py nombreArchivo.py'