import re
import time
import os
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

COLOR = Fore.MAGENTA

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def parse_lrc(path):
    patron = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)")
    lineas = []

    with open(path, "r", encoding="utf-8") as f:
        for linea in f:
            match = patron.match(linea.strip())
            if match:
                minutos = int(match.group(1))
                segundos = float(match.group(2))
                texto = match.group(3).strip()
                tiempo = minutos * 60 + segundos
                lineas.append((tiempo, texto))

    return lineas

def convertir_a_estilo(texto):
    arte = pyfiglet.figlet_format(texto, font="slant")

    reemplazos = {
        "#": "/",
        "|": "|",
        "_": "_",
        "/": "/",
        "\\": "\\",
        "(": "/",
        ")": "\\",
    }

    nuevo = ""
    for c in arte:
        if c == " " or c == "\n":
            nuevo += c
        elif c in reemplazos:
            nuevo += reemplazos[c]
        else:
            nuevo += "_"

    return nuevo

def mostrar_linea(texto_actual, texto_siguiente=""):
    limpiar()

    arte = convertir_a_estilo(texto_actual)
    print(COLOR + arte + Style.RESET_ALL)

    if texto_siguiente:
        print("\n" + Fore.WHITE + Style.DIM + "      ")
        print(Fore.YELLOW + texto_siguiente + Style.RESET_ALL)

def reproducir_lrc(path):
    lineas = parse_lrc(path)
    inicio = time.time()

    for i, (tiempo, texto) in enumerate(lineas):
        espera = tiempo - (time.time() - inicio)

        if espera > 0:
            time.sleep(espera)

        siguientes = [l[1] for l in lineas[i+1:i+3] if l[1]]
        mostrar_linea(texto, " / ".join(siguientes))


reproducir_lrc("cancion.lrc")