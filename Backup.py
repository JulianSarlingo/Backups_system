from genericpath import exists
import shutil
import time
import datetime
import os
import pyttsx3
from notifypy import Notify
from email.mime import audio

# # #  Preparacion  # # #

engine = pyttsx3.init()
engine.setProperty("rate", 160)

notif = Notify()

# # #  Preparacion  # # #


# # #  Funcion alerta  # # #


def alerta(titulo, escucha):
    notif.title = titulo
    # engine.say(escucha)
    notif.message = escucha
    notif.send()
    # engine.runAndWait()

def decir(escucha):
    engine.say(escucha)
    engine.runAndWait()


# # #  Funcion alerta  # # #


os.system("cls")

segundos = 10/3*60
# segundos = 10

nombrePartida = ""
rutaOrigen = "C:/Users/Julian/curseforge/minecraft/Instances/1.12 IC2 BuildC/saves/"
# Reemplazar por la ruta de la carpeta a respaldar

contenido = os.listdir(rutaOrigen)
print(contenido)
engine.say("introduzca por consola el numero de la partida que quiere guardar")
engine.runAndWait()
n = int(input('Introduzca el numero de la partida que quiere salvar\nSiendo "1" la primera que ve, "2" la segunda, etc\n\n'))
n -= 1
nombrePartida = contenido[n]
print("\n" + nombrePartida + "\n")

rutaDestino = "C:/Users/Julian/Desktop/Backups worlds/backups/" + nombrePartida + "/Backup"
# Reemplazar por la ruta destino, incluyendo el sufijo del nombre que tendra la carpeta
# En el ejemplo, la ultima carpeta 'Backup' sera el nombre de la carpeta con terminacion '1', '2' y '3' mas adelante

def hora():
    ahora = datetime.datetime.now()
    ahora = ahora.strftime('%Y/%m/%d %H:%M:%S')
    print(ahora)

inicio = f"""Inicializando...
Cada Backup se realiza cada {segundos} segundos"""

print(inicio)

def iniciando(mens):
    notif.title = "Inicializando...\n"
    engine.say(mens)
    notif.message = f"Cada Backup se realiza cada {segundos} segundos"
    notif.send()
    engine.runAndWait()
iniciando(inicio)

while True:
    for i in range(1,4):
        time.sleep(segundos)
        hora()
        existe = os.path.exists(rutaDestino + str(i))
        print(existe)
        escucha = "Copia de seguridad Realizada en backup"
        if existe == True:
            siExiste = "'Backup" + str(i) + "'" + " Existe\n"
            print(siExiste)
            shutil.rmtree(rutaDestino + str(i))
            alerta(siExiste, escucha + str(i))
        else:
            noExiste = "'Backup" + str(i) + "'" + " NO Existe\n"
            print(noExiste)
            alerta(noExiste, escucha + str(i))
        shutil.copytree(rutaOrigen + "/" + nombrePartida, rutaDestino + str(i) + "/" + nombrePartida)

        decir(escucha + str(i))
       
