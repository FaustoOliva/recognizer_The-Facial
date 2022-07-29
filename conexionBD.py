import pyodbc
from tiempo import bloque, time_BA
from ReconocimientoFacial import legajo
from estado import pta

server = 'A-BTA-525'
bd = 'TheFacialDataBase'
usuario = 'facial'
contrasena = 'facial'

bloque = 'VI3'

print(legajo)
print(bloque)

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='
                              + bd+';UID='+usuario+';PWD='+contrasena)

    print('conexion exitosa')

except:
    print('error al intentar conectar a la base de datos')

cursor = conexion.cursor()

cursor = conexion.cursor()
query = "update Presencia set Estado = ?, Tiempo = ? from Presencia inner join CxMxPxA on Presencia.IdCMPA = CxMxPxA.IdCMPA where LegajoAlumno = ? and CxMxPxA.BloqueDia = ?"
query2 = "INSERT INTO Alumno (Legajo, IdCurso) VALUES (?, ?)"
val = (pta, time_BA, legajo, bloque)

alumno = cursor.execute(query, val).rowcount

print(alumno)
conexion.commit()
cursor.close()
conexion.close()
