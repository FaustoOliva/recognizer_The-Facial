import cv2
import os
from dotenv import load_dotenv

load_dotenv()

dataPath = os.getenv('LEGAJOS_PATH')#Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)



face_recognizer = cv2.face.EigenFaceRecognizer_create()  #1
#face_recognizer = cv2.face.FisherFaceRecognizer_create() #2
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()   #3

# Leyendo el modelo
face_recognizer.read('modeloEigenFace')  #1
#face_recognizer.read('modeloFisherFace.xml') #2
#face_recognizer.read('modeloLBPHFace.xml')   #3

try:
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Captura video streaming. 0 => camara default
    #cap = cv2.VideoCapture('Video.mp4')
except:
    print('Falló conexion de camara.')

# Lee los modelos de prueba


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro) #Precide una etiqueta y la confianza asociada

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA) #Rectangulo, etiqueta y confianza
        
        # Metodo EigenFaces
        if result[1] < 6300: # Fijarnos en el valor de la confianza para determinar rostros entrenadps / desconocidos
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
        # Metodo FisherFace
        if result[1] < 500:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        # Metodo LBPHFace
        if result[1] < 70:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        legajo = '{}'.format(imagePaths[result[0]])
        break

cap.release()
cv2.destroyAllWindows()

#Muy importante en estudiar los valores de confianza de cada metodo. 
#Saber que la precision de la confianza depende de la cantidad de 
# videos, cambios de entorno, etc con lo que este entrenado el modelo