print("BIENVENIDO A LA RECETA DE PASTELES DE GANSO")
cantidad=float(input("¿cuantos pasteles de ganso quiere? "))

#cantidades necesarias
col=6
harina=12
carneG=24
lecheC=6
precioPastelDeGanso=1483
#-------precios de los productos
precioCol=406
precioHarina=294
precioCarneG=324
precioLecheC=135

#---CALCULO DE LA CANTIDAD DE PRODUCTOS NECESARIOS----
col=col*cantidad
harina=harina*cantidad
carneG=carneG*cantidad
lecheC=lecheC*cantidad
#-----------------CALCULO DE PRECIO DE CANTIDAD DE PRODUCTOS----
precioTotalCol=col*precioCol
precioTotalHarina=harina*precioHarina
precioTotalCarneG=carneG*precioCarneG
precioTotalLecheC=lecheC*precioLecheC
precioTotalPastelGanso=precioPastelDeGanso*cantidad
gastoTotal=precioTotalCol+precioTotalHarina+precioTotalCarneG+precioTotalLecheC
#-----------------------------------------------------------------------------
print("para fabricar",  cantidad, "Pastel/es de ganso, se necesita:\nCol:",col,
"\nHarina:",harina,"\nCarne de ganso:", carneG,"\nLeche de cabra:", lecheC,"\n")
print("el precio de dicha cantidad de Col es:",precioTotalCol,
    "\nel precio de dicha cantidad de Harina es:", precioTotalHarina,
    "\nel precio de dicha cantidad de Carne de Ganso es:", precioTotalCarneG,
    "\nel precio de dicha cantidad de Leche de Cabra es:", precioTotalLecheC,
    "\nEl precio en mercado del Pastel de Ganzo por unidad es de:", precioPastelDeGanso,"\n",
    "\nLa suma total es:", gastoTotal,"K",
    "\nEn el precio en mercado de la cantidad deseada es de:", precioTotalPastelGanso,"K")

if precioTotalPastelGanso<=gastoTotal:
    print("\nComprar el Pastel de Ganzo en mercado es más eficiente")
else:
    print("\nEs más económico comprar los ingredientes")
