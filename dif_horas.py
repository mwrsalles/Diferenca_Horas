def dif_horas(hora1,hora2): 

    if len(hora1) == 4 or len(hora1) == 3:
        if hora1[2:3:] == ":":
            horas_1 = hora1[:2:1]
            minutos_1 = hora1[3::1]
        else:
            horas_1 = hora1[:1:1]
            minutos_1 = hora1[2::1]
    elif len(hora1) == 5:
        horas_1 = hora1[:2:1]
        minutos_1 = hora1[3::1]
    if len(hora2) == 4 or len(hora2) == 3:
        if hora2[2:3:] == ":":
            horas_2 = hora2[:2:1]
            minutos_2 = hora2[3::1]
        else:
            horas_2 = hora2[:1:1]
            minutos_2 = hora2[2::1]
    elif len(hora2) == 5:
        horas_2 = hora2[:2:1]
        minutos_2 = hora2[3::1]
        
#calculando as horas
    if int(horas_1) == int(horas_2):
        total_horas = 0
    elif int(horas_1) > int(horas_2):
        if int(minutos_2) >= int(minutos_1):
            auxiliar_horas = 24 - int(horas_1)
            total_horas = int(horas_2) + auxiliar_horas
        elif int(minutos_1) > int(minutos_2):
            auxiliar_horas = 23 - int(horas_1)
            total_horas = int(horas_2) + auxiliar_horas
    elif int(horas_2) > int(horas_1):
        total_horas = int(horas_2) - int(horas_1)
        if int(minutos_2) < int(minutos_1):
            total_horas = int(horas_2) - int(horas_1) -1
    if int(minutos_2) > int(minutos_1):
        total_minutos = int(minutos_2) - int(minutos_1)
    elif int(minutos_1) == int(minutos_2):
        total_minutos = 0
    elif int(minutos_1) > int(minutos_2):
        auxiliar_minutos = 60 - int(minutos_1)
        total_minutos = auxiliar_minutos + int(minutos_2)
    if total_minutos == 60:
        total_horas += 1
    elif total_minutos > 60:
        horas_mais = total_minutos//60
        total_horas = total_horas + horas_mais
        total_minutos = total_minutos - ((horas_mais)*60) 
        
    h = str(total_horas)
    if len(str(total_minutos)) == 2:
        m = str(total_minutos)
    if len(str(total_minutos)) == 1:
        m = "0"+str(total_minutos)
    dif_horas = h+":"+m
        
#minutos
    dif_minutos = total_horas*60 + total_minutos
    
#segundos
    dif_segundos = dif_minutos*60
    
    return dif_horas+":"+str(dif_minutos)+":"+str(dif_segundos)
