#!/usr/bin/python
import psycopg2
from config import config
from tiempo import bloque, time_BA
from ReconocimientoFacial import legajo
from estado import pta

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
        cur = conn.cursor()
        query = "update Presencia set Estado = ?, Tiempo = ? from Presencia inner join CxMxPxA on Presencia.IdCMPA = CxMxPxA.IdCMPA where LegajoAlumno = ? and CxMxPxA.BloqueDia = ?"
        query2 = "INSERT INTO Alumno (Legajo, IdCurso) VALUES (?, ?)"
        query3 = 'select * from Alumno where legajo = ?'
        val = (pta, time_BA, legajo, bloque)
        val3 = (legajo)

        updates = cur.execute(query, val).rowcount

        print('Devuelve la cantidad de update que hubo ', updates)
        conn.commit()
        cur.close()

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
