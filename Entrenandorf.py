import cv2
import os
import numpy as np

dataPath = 'C:/Users/46195270/Desktop/Proyecto5to/Recognizera/Data' #Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath) # List de los nombres de las carpetas de inscripciones (nombres personas)
print('Lista de personas: ', peopleList)


labels = []
facesData = []
label = 0
# Muy importante para ponerle una etiqueta las inscripciones para la maquina sepa a quien esta reconociendo (0 => Pedro 1 => Diego)
#Arraws paralelos jaja

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir #Directorio de las inscripciones
    print('Leyendo las imágenes')

    for fileName in os.listdir(personPath):
        #print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0)) #Arraw con las inscripciones (Leer imagenes)
        #image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label += 1 #Cambia la etiqueta cuando cambia de carpeta inscripciones

#print('labels= ',labels)
#print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0)) #Imrpimir cant etiquetas 0
#print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1)) #Imprimir cant etiquetas 1
#print('Número de etiquetas 2: ',np.count_nonzero(np.array(labels)==2)) #Imprimir cant etiquetas 1
#print('Número de etiquetas 3: ',np.count_nonzero(np.array(labels)==3)) #Imprimir cant etiquetas 1
#print('Número de etiquetas 4: ',np.count_nonzero(np.array(labels)==4)) #Imprimir cant etiquetas 1
#print('Número de etiquetas 5: ',np.count_nonzero(np.array(labels)==5)) #Imprimir cant etiquetas 1

# Métodos para entrenar el reconocedor
face_recognizer = cv2.face.EigenFaceRecognizer_create() #Metodo 1
#face_recognizer = cv2.face.FisherFaceRecognizer_create() #Metodo 2
#face_recognizer = cv2.face.LBPHFaceRecognizer_create() #Metodo3

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels)) #Entrena el modelo con la array de las inscripciones

# Almacenando el modelo obtenido
face_recognizer.write('modeloEigenFace') #1
#face_recognizer.write('modeloFisherFace.xml') #2
#face_recognizer.write('modeloLBPHFace.xml') #3
print("Modelo almacenado...") #Aprox 1min

if os.path.exists(dataPath):
    os.rmdir(dataPath)
    print("Data borrada.")
else:
    print("No se encontró la data.")