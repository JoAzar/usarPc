#GUERRA NAVAL
import random
randomPosX=random.randint(0,50)
randomPosY=random.randint(0,50)
barcoEnemigo=[randomPosX, randomPosY]
#print(barcoEnemigo) #con esto se puede saber la posición del barco enemigo
cont=0
barcoDestruido=False

posicionBarcoX=int(input("Comandante, ingrese la posición X del barco de guerra Ballena III -> "))
posicionBarcoY=int(input("Comandante, ingrese la posición Y del barco de guerra Ballena III -> "))
if posicionBarcoX<=50 and posicionBarcoX>=0 and posicionBarcoY<=50 and posicionBarcoY>=0:
    comandante2=[posicionBarcoX, posicionBarcoY]
else:
    print("¡Comandante, las posiciones están fuera del area de combate! ")
PrimerDisparo=int(input("¡¡¡Señor!!! ¿¿Posición para disparar señor?? -> "))
SegundoDisparo=int(input("¡¡¡Señor!!! ¿¿Posición para el segundo disparo señor?? -> "))
if PrimerDisparo>=0 and PrimerDisparo<=50 and SegundoDisparo>=0 and SegundoDisparo<=50:
    if barcoEnemigo[0]==PrimerDisparo and barcoEnemigo[1]==PrimerDisparo or barcoEnemigo[0]==SegundoDisparo and barcoEnemigo[1]==SegundoDisparo or barcoEnemigo[0]==SegundoDisparo and barcoEnemigo[1]==PrimerDisparo or barcoEnemigo[0]==PrimerDisparo and barcoEnemigo[1]==SegundoDisparo:
        print("¡¡Inteligencia aerea informa que hemos hundido el barco enemigo!!!\n")
        barcoDestruido=True
    else:
        print("\n¡¡Hemos vuelto a darle al agua SEÑOR!! Inteligencia informa que la posición del enemigo es:", barcoEnemigo[0:2])
else:
    print("\n¡¡Hemos vuelto a darle al agua SEÑOR!! Inteligencia informa que la posición del enemigo es:", barcoEnemigo[0:2])

if barcoDestruido==False:
    disparoEnemigo=random.randint(0,50)
    segundoDisparoEnemigo=random.randint(0,50)
    if disparoEnemigo==posicionBarcoX and disparoEnemigo==posicionBarcoY or segundoDisparoEnemigo==posicionBarcoX and segundoDisparoEnemigo==posicionBarcoY or disparoEnemigo==posicionBarcoX and segundoDisparoEnemigo==posicionBarcoY or segundoDisparoEnemigo==posicionBarcoX and disparoEnemigo==posicionBarcoY:
        print("¡¡ALERTA!! ¡¡El barco enemigo nos ha dado!!\n")
    else:
        print("Por suerte nuestro enemigo ha fallado los disparos\n")

print("LA GUERRA HA TERMINADO, VOLVAMOS A CASA...")
