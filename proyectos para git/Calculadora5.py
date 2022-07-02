#--------------------------INGRESO--------------------------------------
cantidad=int(input("ingrese la cantidad de corazones: "))

#-------CANTIDAD DE MEDALLAS REQUERIDAS PARA EL INTERCAMBIO-------------
CorazonDeArbol=3000
InsLymIniciadoT4=400
InsLymExpertoT5=2250
InsLymMaestroT6=3000
InsLymGranMaestroT7=7500
InsLymDeAncianoT8=15000
jabatoSalvaje=3000
jabatoSalvajeElite=50000

CorazonDeArbolPrecio=46400
InsLymIniciadoT4Precio=7995
InsLymExpertoT5Precio=47175
InsLymMaestroT6Precio=49980
InsLymGranMaestroT7Precio=149998
InsLymDeAncianoT8Precio=249988
jabatoSalvajePrecio=30470
jabatoSalvajeElitePrecio=839994

#-----------------CANTIDAD DE OBJETOS QUE OBTENGO-----------------------

cantObjCorazon=cantidad//CorazonDeArbol
cantObjT4=cantidad//InsLymIniciadoT4
cantObjT5=cantidad//InsLymExpertoT5
cantObjT6=cantidad//InsLymMaestroT6
cantObjT7=cantidad//InsLymGranMaestroT7
cantObjT8=cantidad//InsLymDeAncianoT8
cantObjSalvaje=cantidad//jabatoSalvaje
cantObjElite=cantidad//jabatoSalvajeElite
#--------------------PRECIO FINAL CANTIDAD/CALIDAD----------------------

totalCorazonDeArbol=cantObjCorazon*CorazonDeArbolPrecio
totalT4=cantObjT4*InsLymIniciadoT4Precio
totalT5=cantObjT5*InsLymExpertoT5Precio
totalT6=cantObjT6*InsLymMaestroT6Precio
totalT7=cantObjT7*InsLymGranMaestroT7Precio
totalT8=cantObjT8*InsLymDeAncianoT8Precio
totalSalvaje=cantObjSalvaje*jabatoSalvajePrecio
totalElite=cantObjElite*jabatoSalvajeElitePrecio
#-----------------------------------------------------------------------

print("\nCantidad de corazón de árbol:", cantObjCorazon,
    "\nGanancia obtenida:", totalCorazonDeArbol,
    "\n---------------------------------------"
    "\nCantidad de insignias T4:", cantObjT4,
    "\nGanancia obtenida:", totalT4,
    "\n---------------------------------------"
    "\nCantidad de insignias T5:", cantObjT5,
    "\nGanancia obtenida:", totalT5,
    "\n---------------------------------------"
    "\nCantidad de insignias T6:", cantObjT6,
    "\nGanancia obtenida:", totalT6,
    "\n---------------------------------------"
    "\nCantidad de insignias T7", cantObjT7,
    "\nGanancia obtenida:", totalT7,
    "\n---------------------------------------"
    "\nCantidad de insignias t8:", cantObjT8,
    "\nGanancia obtenida:", totalT8,
    "\n---------------------------------------"
    "\nCantidad de Jabatos Salvajes:", cantObjSalvaje,
    "\nGanancia obtenida:", totalSalvaje,
    "\n---------------------------------------"
    "\nCantidad de Jabatos Elite:", cantObjElite,
    "\nGanancia Obtenida:", totalElite,
    "\n---------------------------------------")

