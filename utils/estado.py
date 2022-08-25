from tiempo import time_BA, bloque

valoresTemprano = ['07:30:00', '09:05:00', '10:40:00', '12:55:00', '14:30:00', '16:00:00', '17:30:00']
valoresTarde = ['08:00:00', '09:35:00', '11:10:00', '13:25:00', '14:55:00', '16:25:00']
valoresAusente = ['08:25:00', '10:00:00', '11:35:00', '13:50:00', '15:20:00', '16:50:00']

bloq = int(bloque[2]) 

if(time_BA < valoresTarde[bloq - 1] and time_BA > valoresTemprano[bloq -1]):  
    pta = 'Presente'
elif(time_BA >= valoresTarde[bloq - 1] and time_BA < valoresAusente[bloq - 1]):
    pta = 'Tarde'
elif(time_BA >= valoresAusente[bloq - 1] and time_BA < valoresTemprano[bloq]):
    pta = 'Ausente'

