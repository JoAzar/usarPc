    #PROGRAMA PARA ALBION ONLINE

#Esta funcion calcula un valor (aprox) del dinero que podremos conseguir farmeando arboles T1

def farmArbolT1(tiempo, respuesta):
    precioPorMin=2.764
    precioTotal=tiempo*precioPorMin
    if respuesta.lower()=="no":
        return round(precioTotal,2)
    else:
        precioTotal=precioTotal+(precioTotal*50)/100
        return round(precioTotal,2)

ingreso=0
while ingreso<=0:
    ingreso=int(input("Ingrese el tiempo en minutos que farmeara arboles T1 "))
    respuesta=input("¿Tiene premium? ")
print("la ganancia de farmear arboles T1 durante", ingreso,
"minutos, será: ", farmArbolT1(ingreso, respuesta),"k\n")


