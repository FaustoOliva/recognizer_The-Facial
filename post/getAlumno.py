from connectar import getConnect
from utils.tiempo import bloque, time_BA
from ReconocimientoFacial import legajo
from utils.estado import pta
from ..ReconocimientoFacial import legajo

def get_alumno(legajo):
    l = "'" + legajo + "'"

    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            cursor.execute('SELECT * FROM api_alumno WHERE "Legajo" = ' + l)

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


def modificar_presentismo(estado, tiempo, bloque):
    e = "'" + estado + "'"
    b = "'" + bloque + "'"
    t = "'" + tiempo + "'"
    l = "" + legajo + "'"

    XD = 'update api_presencia set "Estado" = ' + e + ' ,"Tiempo" = ' + t + \
        ' from api_cxmxpxa where api_presencia."IdCMPA" = api_cxmxpxa."IdCMPA" and "LegajoAlumno" = ' + \
        l + ' and api_cxmxpxa."BloqueDia" = ' + b

    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            cursor.execute(XD)
            print(cursor.rowcount, "Presentimso actualizado")

        # display the PostgreSQL database server version

        conection.commit()

    except Exception as ex:
        raise Exception(ex)

    finally:
        if conection is not None:
            conection.close()
            print('Database connection closed.')
