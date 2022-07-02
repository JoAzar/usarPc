def calculo(valorDePiel, cantidadPieles):
    res=valorDePiel*cantidadPieles
    return res

def precioTotal(valor1, valor2):
    suma=valor1+valor2
    return suma

#-------------------------PP----------------------------------------------------
precioPielT2=29
precioPielT3=50
precioPielT4=72
precioPielT5=408


pregunta=int(input("¿Cuántos tipos de pieles tiene? "))
if pregunta==1:
    pregunta2=int(input("¿De que tier son las pieles? "))
    if pregunta2==2:
        cantPielesT2=float(input("Ingrese la cantidad de pieles T2 que tiene "))
        res2=calculo(precioPielT2, cantPielesT2)
        print("El precio de:" ,cantPielesT2, "pieles T2, es de:" ,res2)

    if pregunta2==3:
        cantPielesT3=float(input("Ingrese la cantidad de pieles T3 que tiene "))
        res3=calculo(precioPielT3, cantPielesT3)
        print("El precio de:" ,cantPielesT3, "pieles T3, es de:" ,res3)

    if pregunta2==4:
        cantPielesT4=float(input("Ingrese la cantidad de pieles T4 que tiene "))
        res4=calculo(precioPielT4, cantPielesT4)
        print("El precio de:" ,cantPielesT4, "pieles T4, es de:" ,res4)

    if pregunta2==5:
        cantPielesT5=int(input("Ingrese la cantidad de pieles T5 que tiene "))
        res5=calculo(precioPielT5, cantPielesT5)
        print("El precio de:" ,cantPielesT5, "pieles T5, es de:" ,res5)

if pregunta==2:
    pregunta2=int(input("¿De que tier son las pieles? "))
    pregunta3=int(input("¿De que tier son las pieles? "))
    if pregunta2>pregunta3:
        aux=pregunta2
        pregunta2=pregunta3
        pregunta3=aux
    if pregunta2==2 and pregunta3==3:
        cantPielesT2=float(input("Ingrese la cantidad de pieles T2 que tiene "))
        cantPielesT3=float(input("Ingrese la cantidad de pieles T3 que tiene "))
        res2=calculo(precioPielT2, cantPielesT2)
        res3=calculo(precioPielT3, cantPielesT3)
        total=precioTotal(res2,res3)
        print("El precio de:" ,cantPielesT2, "pieles T2, es de:" ,res2,
            "\nEl precio de:" ,cantPielesT3, "pieles T3, es de:" ,res3,
            "\nEn total se obtiene:", total)

    if pregunta2==2 and pregunta3==4:
        cantPielesT2=float(input("Ingrese la cantidad de pieles T2 que tiene "))
        cantPielesT4=float(input("Ingrese la cantidad de pieles T4 que tiene "))
        res2=calculo(precioPielT2, cantPielesT2)
        res4=calculo(precioPielT4, cantPielesT4)
        total=precioTotal(res2,res4)
        print("El precio de:" ,cantPielesT2, "pieles T2, es de:" ,res2,
            "\nEl precio de:" ,cantPielesT4, "pieles T4, es de:" ,res4,
            "\nEn total se obtiene:", total)

    if pregunta2==3 and pregunta3==4:
        cantPielesT3=float(input("Ingrese la cantidad de pieles T3 que tiene "))
        cantPielesT4=float(input("Ingrese la cantidad de pieles T4 que tiene "))
        res3=calculo(precioPielT3, cantPielesT3)
        res4=calculo(precioPielT4, cantPielesT4)
        total=precioTotal(res3,res4)
        print("El precio de:" ,cantPielesT3, "pieles T3, es de:" ,res3,
            "\nEl precio de:" ,cantPielesT4, "pieles T4, es de:" ,res4,
            "\nEn total se obtiene:", total)

    if pregunta2==2 and pregunta3==5:
        cantPielesT2=float(input("Ingrese la cantidad de pieles T2 que tiene "))
        cantPielesT5=float(input("Ingrese la cantidad de pieles T5 que tiene "))
        res2=calculo(precioPielT2, cantPielesT2)
        res5=calculo(precioPielT5, cantPielesT5)
        total=precioTotal(res2,res5)
        print("El precio de:" ,cantPielesT2, "pieles T2, es de:" ,res2,
            "\nEl precio de:" ,cantPielesT5, "pieles T5, es de:" ,res5,
            "\nEn total se obtiene:", total)

    if pregunta2==3 and pregunta3==5:
        cantPielesT2=float(input("Ingrese la cantidad de pieles T3 que tiene "))
        cantPielesT2=float(input("Ingrese la cantidad de pieles T5 que tiene "))
        res3=calculo(precioPielT3, cantPielesT3)
        res5=calculo(precioPielT5, cantPielesT5)
        total=precioTotal(res3,res5)
        print("El precio de:" ,cantPielesT3, "pieles T3, es de:" ,res3,
            "\nEl precio de:" ,cantPielesT5, "pieles T5, es de:" ,res5,
            "\nEn total se obtiene:", total)

    if pregunta2==4 and pregunta3==5:
        cantPielesT4=float(input("Ingrese la cantidad de pieles T4 que tiene "))
        cantPielesT5=float(input("Ingrese la cantidad de pieles T5 que tiene "))
        res4=calculo(precioPielT4, cantPielesT4)
        res5=calculo(precioPielT5, cantPielesT5)
        total=precioTotal(res4,res5)
        print("El precio de:" ,cantPielesT4, "pieles T4, es de:" ,res4,
            "\nEl precio de:" ,cantPielesT5, "pieles T5, es de:" ,res5,
            "\nEn total se obtiene:", total)





