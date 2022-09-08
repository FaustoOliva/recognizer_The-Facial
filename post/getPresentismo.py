from .connectar import getConnect


def modificar_presentismo(estado, bloque, tiempo,legajo):
    e = "'" + estado + "'"
    b = "'" + bloque + "'"
    t = "'" + tiempo + "'"
    l = "'" + legajo + "'"
    print(e, b, t, l)

    hd = 'select * from api_presencia where api_cxmxpxa where api_presencia."IdCMPA" = api_cxmxpxa."IdCMPA" and "LegajoAlumno" = ' + \
        l + ' and api_cxmxpxa."BloqueDia" = ' + b

    XD = 'update api_presencia set "Estado" = ' + e + ' ,"Tiempo" = ' + t + \
        ' from api_cxmxpxa where api_presencia."IdCMPA" = api_cxmxpxa."IdCMPA" and "LegajoAlumno" = ' + \
        l + ' and api_cxmxpxa."BloqueDia" = ' + b

    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            existe = cursor.execute(hd)
            print(existe)
            if(existe):
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
