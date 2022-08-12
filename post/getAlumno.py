from connect import getConnect


def get_alumno():
    try:
        conection = getConnect()

        with conection.cursor() as cursor:
            cursor.execute('SELECT * FROM api_alumno WHERE "Legajo" = ' + "'R1275'")

        # display the PostgreSQL database server version
            alumno = cursor.fetchall()
            print(alumno)
    
        conection.commit()
    
    except Exception as ex:
        raise Exception(ex)

    finally:
        if conection is not None:
            conection.close()
            print('Database connection closed.')

if __name__ == '__main__':
    get_alumno()
    