cantidad=int(input("¿cuántos pasteles T7 quiere? "))

#------------Cantidad Necesaria---------------
pardoDeMaiz=18
harina=36
carneDeCerdo=72
lecheDeOveja=18
#---------------------------------------------
totalMaiz=pardoDeMaiz*cantidad
totalHarina=harina*cantidad
totalCarne=carneDeCerdo*cantidad
totalLeche=lecheDeOveja*cantidad

#--------------Devolucion 15%-----------------
devMaiz=(totalMaiz*15)//100
devHarina=(totalHarina*15)//100
devCarne=(totalCarne*15)//100
devLeche=(totalLeche*15)//100

print("\nSe dan ingredientes sobrantes:",
    "\nMaiz:", devMaiz,
    "\nHarina:", devHarina,
    "\nCarne:", devCarne,
    "\nLeche:", devLeche)
#---------------------------------------------


#-----------------------------------------------
print("\nPara hacer", cantidad, "pasteles T7 se necesita:",
    "\nMaiz:", totalMaiz,
    "\nHarina:", totalHarina,
    "\nCarne de cerdo:", totalCarne,
    "\nLeche de oveja:", totalLeche)

#-----------Costos de ingredientes------------
maizCosto=357
harinaCosto=293
carneCosto=340
lecheCosto=266
#--------------------------------Costos totales-----------------------------------------
totalCostoMaiz=maizCosto*totalMaiz
totalCostoHarina=harinaCosto*totalHarina
totalCostoCarne=carneCosto*totalCarne
totalCostoLeche=lecheCosto*totalLeche
costoTotalIngredientes=totalCostoHarina+totalCostoCarne+totalCostoLeche+totalCostoMaiz
#---------------------------------------------------------------------------------------

print("\nEl costo total de los maices es:", totalCostoMaiz,
    "\nEl costo total de las harinas es:", totalCostoHarina,
    "\nEl costo total de la carne es:", totalCostoCarne,
    "\nEl costo total de la leche es:", totalCostoLeche,
    "\nCosto total de todos los productos es:", costoTotalIngredientes)
#---------------------------------------------------------------------------------------

