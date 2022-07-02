#Este código sirve para apagar el ordenador en un tiempo determinado por "temp" // importa la librería os y time
#!!!LEER!! EL VALOR DE TEMP DEBE ESTAR EN SEGUNDOS 60 seg = 1 min (por si quieren pasarlo a minutos u horas)

import os
import time
temp=int(input("Ingrese el tiempo para apagar el ordenador: ")) #en segundos
time.sleep(temp)
os.system("shutdown /s")