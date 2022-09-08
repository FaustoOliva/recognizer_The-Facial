from .connectar import getConnect

def get_alumno(legajo):
    l = "'" + legajo + "'"

    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            cursor.execute('SELECT * FROM api_alumno WHERE "Legajo" = ' + l)

        # display the PostgreSQL database server version
            alumno = cursor.fetchall()

        conection.commit()
        return alumno
    except Exception as ex:
        raise Exception(ex)

    finally:
        if conection is not None:
            conection.close()
            print('Database connection closed.')


