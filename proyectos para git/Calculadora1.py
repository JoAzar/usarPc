bueyPeso=2462
pesoObjeto=float(input("el peso del objeto"))
pesoAdmisible=bueyPeso/pesoObjeto

precioLym=int(input("ingrese precio Lym:" ))
precioMartlock=int(input("ingrese precio Martlock: "))
precioFortSterling=int(input("ingrese precio Fort:" ))
precioBridgeWatch=int(input("ingrese precio Bridge:" ))
precioThetFord=int(input("ingrese precio ThetFord:" ))


resultado1=precioLym*pesoAdmisible
resultado2=precioMartlock*pesoAdmisible
resultado3=precioFortSterling*pesoAdmisible
resultado4=precioBridgeWatch*pesoAdmisible
resultado5=precioThetFord*pesoAdmisible

print("\nlos precios son:\nLym",resultado1,
    "\nMarlock" ,resultado2,
    "\nFortSterling",resultado3,
    "\nBridgeWatch",resultado4,
    "\nThetFord" ,resultado5,
    "\nCantidad de objetos por peso de buey", pesoAdmisible)




