from .connectar import getConnect


def get_alumno(legajo):
  
    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            cursor.execute('SELECT * FROM api_alumno WHERE "Legajo" = ' + legajo)

        # display the PostgreSQL database server version
            alumno = cursor.fetchall()
            print(alumno)
    
        conection.commit()
        return alumno
    except Exception as ex:
        raise Exception(ex)

    finally:
        if conection is not None:
            conection.close()
            print('Database connection closed.')

if __name__ == '__main__':
    get_alumno()
    