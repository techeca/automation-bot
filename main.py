import time

import cv2
import numpy as np
import pyautogui
import pytesseract

import os
import threading
from tkinter import ttk, Tk, Button, Label, Listbox, Scrollbar, Toplevel, Canvas
import pathlib
import pygubu
import re
import math
import ast
import pyperclip

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"

ruta_imagen_chrome = './treasureHunt/chrome.png'
ruta_imagen_dofus = './treasureHunt/dofus.png'
ruta_imagen_puerta = './treasureHunt/puerta.png'
ruta_imagen_moverse = './treasureHunt/mover.png'
ruta_imagen_tesoro = './treasureHunt/tesoro.png'
ruta_imagen_200 = './treasureHunt/nivel200.png'
ruta_imagen_180 = './treasureHunt/nivel180.png'
ruta_imagen_160 = './treasureHunt/nivel160.png'
ruta_imagen_140 = './treasureHunt/nivel140.png'
ruta_imagen_120 = './treasureHunt/nivel120.png'
ruta_imagen_salir = './treasureHunt/salir.png'
ruta_imagen_salir_puerta = './treasureHunt/salir_puerta.png'
ruta_imagen_captura = './treasureHunt/captura.png'
ruta_imagen_recortada = './treasureHunt/captura_recorte.png'
ruta_imagen_flecha_abajo1 = './treasureHunt/flecha_abajo1.png'
ruta_imagen_flecha_abajo2 = './treasureHunt/flecha_abajo2.png'
ruta_imagen_flecha_arriba1 = './treasureHunt/flecha_arriba1.png'
ruta_imagen_flecha_arriba2 = './treasureHunt/flecha_arriba2.png'
ruta_imagen_flecha_izquierda1 = './treasureHunt/flecha_izquierda1.png'
ruta_imagen_flecha_izquierda2 = './treasureHunt/flecha_izquierda2.png'
ruta_imagen_flecha_derecha1 = './treasureHunt/flecha_derecha1.png'
ruta_imagen_flecha_derecha2 = './treasureHunt/flecha_derecha2.png'
ruta_imagen_llegado_destino = './treasureHunt/llegado_destino.png'
ruta_imagen_banderita = './treasureHunt/banderita.png'
ruta_imagen_perforatroz = './treasureHunt/perforatroz.png'
ruta_imagen_X_navegador = './treasureHunt/XenNavegador.png'
ruta_imagen_Y_navegador = './treasureHunt/YenNavegador.png'
ruta_imagen_reload_navegador = './treasureHunt/reloadNavegador.png'
ruta_imagen_hint_box = './treasureHunt/hintbox.png'
ruta_imagen_chat_box = './treasureHunt/chatbox.png'
ruta_imagen_interrogacion = './treasureHunt/interrogacion.png'
ruta_imagen_etapa_finalizada = './treasureHunt/etapa_finalizada.png'
ruta_imagen_monstruo = './treasureHunt/monstruo.png'
ruta_imagen_lucha = './treasureHunt/lucha.png'
ruta_imagen_merkasako = './treasureHunt/merkasako.png'
ruta_imagen_zaap_merka = './treasureHunt/zaap_merka.png'
ruta_imagen_teleport_btn = './treasureHunt/teleport_btn.png'
ruta_imagen_buscar_zaap = './treasureHunt/buscar_zaap.png'
ruta_imagen_cerrar_bat = './treasureHunt/end_battle.png'
ruta_imagen_entreda_cofre = './treasureHunt/puerta.png'
ruta_imagen_mover2 = './treasureHunt/mover2.png'
ruta_imagen_minBusqueda = './treasureHunt/minimizar_busqueda.png'
ruta_imagen_maxBusqueda = './treasureHunt/maximizar_busqueda.png'
ruta_imagen_navegador1 = './treasureHunt/nav1.png'
ruta_imagen_navegador2 = './treasureHunt/nav2.png'
ruta_imagen_validar = './treasureHunt/validar.png'
limite_intentos = 200000000000000000000
intentos_realizados = 0

### Game data (eliminar?)
game_coords = None
etapa_actual = None
salida_actual = None
pistas_actual = None
comienzo_perfo_actual = None
inBattle = False

coordenadas_zaap = [
    (-5, -23, "Llanura de los puerkazos"),
    (-46, 18, "Pueblo costero"),
    (15, -58, "Dunas de los Huesos"),
    (10, 22, "Ribera del golfo sufokeno"),
    (-20, -20, "Caminos Rocosos"),
    (-78, -41, "Burgo"),
    (-2, 0, "Pueblo de Amakna"),
    (1, -32, "Tainela"),
    (-1, 24, "Llanura de los escarahojas"),
    (7, -4, "Puerto de Madrestam"),
    (-5, -8, "Montana de los crujidores"),
    (-13, -28, "Sierra de cania"),
    (-1, 13, "Linde del Bosque Malefico"),
    (-3, -42, "Lago de Cania"),
    (-15, 25, "Tierras Desacralizadas"),
    (20, -29, "Pueblo de Pandala"),
    (35, 12, "Playa Tortuga"),
    (39, -82, "Arboleda Nevada"),
    (-31, -56, "Corazon Inmaculado"),
    (-46, 18, "Pueblo costero"),
    (-25, 12, "Camino de las caravanas"),
    (-26, 37, "Coraza"),
    (-16, 1, "Pueblo de los ganaderos"),
    (-27, -36, "Campos de cania")
]

# Calcular la distancia Euclidiana
def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Encontrar la coordenada más cercana
def coordenada_mas_cercana(x, y, coordenadas):
    coordenada_mas_cercana = None
    distancia_minima = float('inf')
    nombre_mas_cercano = None

    for coord in coordenadas:
        coord_x, coord_y, nombre = coord
        distancia = calcular_distancia(x, y, coord_x, coord_y)
        print(f"Calculando distancia de ({x}, {y}) a ({coord_x}, {coord_y}): {distancia:.2f} - {nombre}")
        
        if distancia < distancia_minima:
            distancia_minima = distancia
            coordenada_mas_cercana = (coord_x, coord_y)
            nombre_mas_cercano = nombre

    print(f"La coordenada más cercana es: {coordenada_mas_cercana} - {nombre_mas_cercano} con una distancia de {distancia_minima:.2f}")
    return coordenada_mas_cercana, nombre_mas_cercano

def buscar_y_clickear_chrome(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(0.5)
    else:
        buscar_y_clickear_chrome(ruta_imagen_chrome)

def buscar_y_clickear_dofus(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        buscar_y_clickear_dofus(ruta_imagen_dofus)

def buscar_y_clickear_monstruo(ruta_imagen):
    global intentos_realizados
    global inBattle
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    imagen_referencia2 = cv2.imread(ruta_imagen_cerrar_bat)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    altura2, ancho2, _ = imagen_referencia2.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    resultado2 = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(resultado2)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza or max_val2 >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        
        # Haz clic en el centro de la imagen encontrada
        if(max_val >= umbral_confianza):
            centro_x = max_loc[0] + ancho // 2
            centro_y = max_loc[1] + altura // 2
            pyautogui.tripleClick(centro_x, centro_y)
        if(max_val2 >= umbral_confianza):
            inBattle = False
            btX = max_loc2[0] + ancho2 // 2
            btY = max_loc2[1] + altura2 // 2
            pyautogui.click(btX, btY)
        time.sleep(1)
    else:
        buscar_y_clickear_monstruo(ruta_imagen_monstruo)

def moverse():
    pyautogui.tripleClick(1619, 646)
    time.sleep(5)

def buscar_y_clickear_puerta(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2

        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(4)
    else:
        buscar_y_clickear_puerta(ruta_imagen_puerta)

def buscar_y_clickear_moverse(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2

        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(4)
    else:
        buscar_y_clickear_moverse(ruta_imagen_moverse)

def buscar_y_clickear_tesoro(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2

        # Haz clic en el centro de la imagen encontrada
        pyautogui.tripleClick(centro_x, centro_y)
        time.sleep(0.5)
    else:
        buscar_y_clickear_tesoro(ruta_imagen_moverse)



def buscar_y_clickear_salir(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(4)
    else:
        buscar_y_clickear_salir(ruta_imagen_salir)

def buscar_y_clickear_salir_puerta(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2

        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(4)
    else:
        buscar_y_clickear_salir_puerta(ruta_imagen_salir_puerta)

def verificacion_pistas():
    recorte_verificacion_pistas(ruta_imagen_captura)
    time.sleep(1)
    cantidad_pistas(ruta_imagen_recortada)
    cantidad = cantidad_pistas(ruta_imagen_recortada)
    print(cantidad)
    # Realizar acciones según la cantidad de símbolos "?"
    if cantidad == 0:
        print("Cero '?'")
        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')
    if cantidad == 1:
        print("Uno '?'")
        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista2")
        recorte_segundapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_2pista()
        recorte_segundapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')
    elif cantidad == 2:
        print("Dos '?'")
        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista2")
        recorte_segundapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_2pista()
        recorte_segundapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista3")
        recorte_tercerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_3pista()
        recorte_tercerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')
    elif cantidad == 3:
        print("Tres '?'")

        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista2")
        recorte_segundapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_2pista()
        recorte_segundapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista3")
        recorte_tercerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_3pista()
        recorte_tercerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista4")
        recorte_cuartapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_4pista()
        recorte_cuartapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')
    elif cantidad == 4:
        print("Cuatro '?'")
        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista2")
        recorte_segundapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_2pista()
        recorte_segundapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista3")
        recorte_tercerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_3pista()
        recorte_tercerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista4")
        recorte_cuartapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_4pista()
        recorte_cuartapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        print("Pista5")
        recorte_quintapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_5pista()
        recorte_quintapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')
    elif cantidad == 5:
        print("Cinco '?'")
        print("Pista1")
        recorte(ruta_imagen_captura)
        cordenadas()
        recorte_primerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas()
        print(texto_hasta_coma)
        recorte_primerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista2")
        recorte_segundapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_2pista()
        recorte_segundapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista3")
        recorte_tercerapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_3pista()
        recorte_tercerapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista4")
        recorte_cuartapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_4pista()
        recorte_cuartapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista5")
        recorte_quintapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_5pista()
        recorte_quintapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)

        print("Pista6")
        recorte_sextapista_flecha(ruta_imagen_captura)
        texto_hasta_coma = comparacion_flechas_6pista()
        recorte_sextapista(ruta_imagen_captura)
        OCR(ruta_imagen_recortada)
        pista(texto_hasta_coma)
        etapa_finalizada('etapa_finalizada.png')



def comenzar_etapas():
    try:
        primer_numero, segundo_numero = verificacion_etapas(ruta_imagen_captura)
        primer_numero = int(primer_numero)
        segundo_numero = int(segundo_numero)
        
        while primer_numero < segundo_numero:  # Mientras la condición sea verdadera
            verificacion_pistas()
            primer_numero += 1  # Actualiza la condición para evitar un bucle infinito
            time.sleep(1)
        
        time.sleep(1)
        lucha('lucha.png')
        time.sleep(2)
        pelea()
        time.sleep(2)
        pyautogui.press('0')
    except ValueError as e:
        print(f"Error: {e}")

def pelea():
    global inBattle
    inBattle = True
    #time.sleep(2)
    #pyautogui.press('esc')
    #time.sleep(2)
    pyautogui.press('F1')
    time.sleep(1)
    pyautogui.press('F1')
    time.sleep(6)
    contador = 1
    while inBattle == True:  # Mientras la condición sea verdadera
        time.sleep(6)
        #2 atks
        pyautogui.press('1')
        time.sleep(2)
        buscar_y_clickear_monstruo(ruta_imagen_monstruo)
        time.sleep(1)
        pyautogui.press('F1')
        time.sleep(1)

        #pyautogui.press('1')
        #time.sleep(1)
        #buscar_y_clickear_monstruo(ruta_imagen_monstruo)
        #time.sleep(1)
        #pyautogui.press('F1')  # termina el turno

        # Actualiza la condición para evitar un bucle infinito

def recorte_etapas(ruta_imagen):
    imagen = pyautogui.screenshot()
    imagen.save('captura.png')
    imagen = cv2.imread(ruta_imagen)
    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 603, 172, 640  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte(ruta_imagen):
    imagen = pyautogui.screenshot()
    imagen.save('captura.png')
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 653, 172, 672  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_cordenada_juego(ruta_imagen):
    imagen = pyautogui.screenshot()
    imagen.save('captura.png')
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 5, 70, 95, 105  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)



# limpia coord de salida
def manipulacion_cordenada():
    texto = OCR(ruta_imagen_recortada)
    #print(texto)
    texto = texto.replace("Salida", "")
    texto = texto.replace("o", "6")
    
    # Dividir la cadena usando "," como delimitador
    partes = texto.split(",")

    # Extraer el primer elemento después de eliminar los espacios en blanco
    primer_elemento = partes[0].strip()

    # Extraer el número entre corchetes
    primera_coordenada = primer_elemento.split("[")[-1]

    # ________________________________________________________

    # Encuentra la posición de la coma
    pos_coma = texto.find(',')

    # Encuentra la posición del corchete de cierre "]"
    pos_corchete_cierre = len(texto)

    # Extrae el número después de la coma (excluyendo el corchete de cierre)
    segunda_coordenada = texto[pos_coma + 1: pos_corchete_cierre]

    return primera_coordenada, segunda_coordenada

def manipulacion_cordenada_juego():
    texto = OCR(ruta_imagen_recortada)
    texto = texto.replace(")", "")
    texto = texto.replace("=", "-")
    texto = texto.replace("Salida", "")
    texto = texto.replace("o", "6")
    texto = texto.replace("»", "")
    texto = texto.replace("!", "")
    texto = texto.replace(";", "")
    # Dividir la cadena por la coma
    numeros = texto.split(',')
    # Obtener los valores

    salida_actual_texto = OCR(ruta_imagen_recortada)
    salida_actual_texto = re.findall(r'-?\d+', salida_actual_texto)
    c1 = salida_actual_texto[0]
    c2 = salida_actual_texto[1]

    primera_coordenada = str(numeros[0])
    segunda_coordenada = str(numeros[1])

    return primera_coordenada, segunda_coordenada

def cordenadas():
    buscar_y_clickear_chrome(ruta_imagen_chrome)
    c1, c2 = manipulacion_cordenada()
    time.sleep(1)
    #pyautogui.tripleClick(731, 360)
    reloadNavegador(ruta_imagen_reload_navegador)
    time.sleep(1)
    buscarXenNavegador(ruta_imagen_X_navegador)
    pyautogui.write(c1)
    time.sleep(1)
    #pyautogui.press('tab')
    buscarYenNavegador(ruta_imagen_Y_navegador)
    pyautogui.write(c2)
    time.sleep(1)

def cordenadas_juegos():
    buscar_y_clickear_chrome(ruta_imagen_chrome)
    c1, c2 = manipulacion_cordenada_juego()
    time.sleep(0.5)
    pyautogui.tripleClick(731, 360)
    reloadNavegador(ruta_imagen_reload_navegador)
    time.sleep(0.5)
    buscarXenNavegador(ruta_imagen_X_navegador)
    pyautogui.write(c1)
    time.sleep(0.5)
    #pyautogui.press('tab')
    #time.sleep(0.5)
    buscarYenNavegador(ruta_imagen_Y_navegador)
    pyautogui.write(c2)
    time.sleep(3)
    buscar_y_clickear_dofus(ruta_imagen_dofus)

def recorte_primerapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 673, 300, 700  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def obtener_solo_letras(texto):
    # Busca todas las letras (mayúsculas y minúsculas)
    letras = re.findall(r'[a-zA-Z]', texto)
    # Une las letras encontradas en un solo string
    return ''.join(letras)

def recorte_primerapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 673, 55, 700  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_sextapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 810, 55, 845  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def comparacion_flechas():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    buscar_y_clickear_dofus(ruta_imagen_dofus)
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha1(ruta_imagen_captura)

                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                else:
                    recorte_captura_mesajelargo_flecha1(ruta_imagen_captura)
                    texto = OCR(ruta_imagen_recortada)
                    partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                    texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                    if texto_hasta_coma == "Dirigete hacia el Sur,":
                        navegacion_flechas(ruta_imagen_flecha_abajo2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Norte,":
                        navegacion_flechas(ruta_imagen_flecha_arriba2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                        navegacion_flechas(ruta_imagen_flecha_izquierda2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Este,":
                        navegacion_flechas(ruta_imagen_flecha_derecha2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    break

            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas()

def comparacion_flechas_2pista():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha2(ruta_imagen_captura)
                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                else:
                    recorte_captura_mesajelargo_flecha2(ruta_imagen_captura)
                    texto = OCR(ruta_imagen_recortada)
                    partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                    texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                    if texto_hasta_coma == "Dirigete hacia el Sur,":
                        navegacion_flechas(ruta_imagen_flecha_abajo2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Norte,":
                        navegacion_flechas(ruta_imagen_flecha_arriba2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                        navegacion_flechas(ruta_imagen_flecha_izquierda2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Este,":
                        navegacion_flechas(ruta_imagen_flecha_derecha2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    break

            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas_2pista()

def comparacion_flechas_3pista():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha3(ruta_imagen_captura)
                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                print(texto_hasta_coma)
                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas_3pista()

def comparacion_flechas_4pista():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8
            print(max_val)
            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha4(ruta_imagen_captura)
                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                print(texto_hasta_coma)
                

                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                else:
                    recorte_captura_mesajelargo_flecha4(ruta_imagen_captura)
                    texto = OCR(ruta_imagen_recortada)
                    partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                    texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma
                    if texto_hasta_coma == "Dirigete hacia el Sur,":
                        navegacion_flechas(ruta_imagen_flecha_abajo2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Norte,":
                        navegacion_flechas(ruta_imagen_flecha_arriba2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                        navegacion_flechas(ruta_imagen_flecha_izquierda2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    elif texto_hasta_coma == "Dirigete hacia el Este,":
                        navegacion_flechas(ruta_imagen_flecha_derecha2)
                        time.sleep(0.5)
                        return texto_hasta_coma
                    break
            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas_4pista()

def comparacion_flechas_5pista():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha5(ruta_imagen_captura)
                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma

                print(texto_hasta_coma)
                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas_5pista()

def comparacion_flechas_6pista():
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = [ruta_imagen_recortada]

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Se encontró una imagen alternativa, procede con la búsqueda y acción
            # Tu lógica actual para buscar y hacer clic en la imagen
            altura, ancho, _ = imagen_referencia.shape
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                pyautogui.click(centro_x, centro_y)
                imagen = pyautogui.screenshot()
                imagen.save('captura.png')
                recorte_captura_mesaje_flecha6(ruta_imagen_captura)
                texto = OCR(ruta_imagen_recortada)
                partes = texto.split(",")  # Divide el texto en partes usando la coma como separador
                texto_hasta_coma = partes[0] + ","  # Toma la primera parte antes de la coma

                if texto_hasta_coma == "Dirigete hacia el Sur,":
                    navegacion_flechas(ruta_imagen_flecha_abajo2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Norte,":
                    navegacion_flechas(ruta_imagen_flecha_arriba2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Oeste,":
                    navegacion_flechas(ruta_imagen_flecha_izquierda2)
                    time.sleep(0.5)
                    return texto_hasta_coma
                elif texto_hasta_coma == "Dirigete hacia el Este,":
                    navegacion_flechas(ruta_imagen_flecha_derecha2)
                    time.sleep(0.5)
                    return texto_hasta_coma
            break  # Termina el bucle ya que se encontró y clickeó una imagen
        else:
            print(f"No se encontró la imagen en la ruta: {ruta_alternativa}")

    # Si ninguna de las imágenes alternativas fue encontrada
    else:
        comparacion_flechas_6pista()

#selecciona flecha dirección en navegador
def navegacion_flechas(ruta_imagen):
    global intentos_realizados
    #buscar_y_clickear_chrome(ruta_imagen_chrome)
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    print(max_val)
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
    else:
        navegacion_flechas(ruta_imagen)

def recorte_captura_mesaje_flecha1(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 628, 205, 662  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesaje_flecha2(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 658, 205, 700  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesajelargo_flecha2(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 628, 205, 700  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesajelargo_flecha1(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 608, 205, 662  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesajelargo_flecha4(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 700, 215, 740  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesaje_flecha3(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 678, 205, 720  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesaje_flecha4(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 708, 215, 740  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesaje_flecha5(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 728, 215, 780  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_captura_mesaje_flecha6(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 20, 750, 215, 800  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def direction(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(0.5)
    else:
        direction(ruta_imagen)

def recorte_segundapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 700, 298, 730  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_segundapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 700, 55, 730  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_tercerapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 727, 298, 760  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_cuartapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 754, 298, 783  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_quintapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 780, 298, 813  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_sextapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 50, 820, 298, 850  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_tercerapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 728, 55, 780  # Ejemplo de coordenadas de recorte y1=27 y2= 30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_cuartapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 755, 55, 810  # Ejemplo de coordenadas de recorte y1=27 y2= 30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_quintapista_flecha(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 785, 55, 815  # Ejemplo de coordenadas de recorte y1=27 y2= 30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def recorte_verificacion_pistas(ruta_imagen):
    imagen = pyautogui.screenshot()
    imagen.save('captura.png')
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 30, 700, 300, 855  # Ejemplo de coordenadas de recorte y1=27 y2= 30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)

def cantidad_pistas(ruta_imagen):
    try:
        # Cargar la imagen de la captura de pantalla
        captura_pantalla = cv2.imread(ruta_imagen)
        if captura_pantalla is None:
            raise ValueError(f"No se pudo cargar la imagen de captura de pantalla desde {ruta_imagen}")

        # Cargar la imagen de referencia
        referencia = cv2.imread(ruta_imagen_interrogacion)
        if referencia is None:
            raise ValueError(f"No se pudo cargar la imagen de referencia desde {ruta_imagen_interrogacion}")

        # Buscar la imagen de referencia en la captura de pantalla
        resultado = cv2.matchTemplate(captura_pantalla, referencia, cv2.TM_CCOEFF_NORMED)

        # Definir un umbral de confianza
        umbral_confianza = 0.8
        ubicaciones = np.where(resultado >= umbral_confianza)

        # Convertir ubicaciones a una lista de coordenadas
        ubicaciones = list(zip(*ubicaciones[::-1]))

        # Contar las ocurrencias encontradas
        cantidad_ocurrencias = len(ubicaciones)
        return cantidad_ocurrencias

    except Exception as e:
        print(f"Error al procesar las imágenes: {e}")
        return 0

def etapa_finalizada(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        etapa_finalizada(ruta_imagen_etapa_finalizada)

def lucha(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
    else:
        etapa_finalizada(ruta_imagen_lucha)

def buscarXenNavegador(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        buscarXenNavegador(ruta_imagen)

def buscarYenNavegador(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        buscarYenNavegador(ruta_imagen)

def reloadNavegador(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        reloadNavegador(ruta_imagen)


def chatBox(ruta_imagen):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Carga la imagen de referencia y la captura de pantalla
    imagen_referencia = cv2.imread(ruta_imagen)
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape
    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8
    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2
        # Haz clic en el centro de la imagen encontrada
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        chatBox(ruta_imagen)  


class ImageFinderApp:
    def __init__(self, master=None):
        #self.root = root
        #self.root.title("TH Automation")
        #self.root.geometry("400x400")
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main', master)
        builder.connect_callbacks(self)
        self.boton_presionado = False

        

        # Obtener el Label definido en Pygubu
        self.status_label = self.builder.get_object('lblWInfo')
        self.coordActual = self.builder.get_object('lblCoordActual')
        self.etapaActual = self.builder.get_object('lblEtapaActual')
        self.cantidadPistas = self.builder.get_object('lblPistas')
        self.umbral = self.builder.get_object('entryUmbral')
        self.entryPytesseract = self.builder.get_object('entryPytesseract')
        self.salida = self.builder.get_object('lblSalida')
        self.pista1 = self.builder.get_object('lblPista1')
        self.pista2 = self.builder.get_object('lblPista2')
        self.pista3 = self.builder.get_object('lblPista3')
        self.pista4 = self.builder.get_object('lblPista4')
        self.pista5 = self.builder.get_object('lblPista5')
        self.pista6 = self.builder.get_object('lblPista6')
        self.flecha1 = self.builder.get_object('lblFlecha1')
        self.flecha2 = self.builder.get_object('lblFlecha2')
        self.flecha3 = self.builder.get_object('lblFlecha3')
        self.flecha4 = self.builder.get_object('lblFlecha4')
        self.flecha5 = self.builder.get_object('lblFlecha5')
        self.flecha6 = self.builder.get_object('lblFlecha6')
        self.moverArriba = self.builder.get_object('lblArriba')
        self.moverAbajo = self.builder.get_object('lblAbajo')
        self.moverIzquierda = self.builder.get_object('lblIzquierda')
        self.moverDerecha = self.builder.get_object('lblDerecha')
        self.pistaD5 = self.builder.get_object('lblPistaD5')
        self.chat = self.builder.get_object('lblChat')
        self.btnMerkasako = self.builder.get_object('lblMerkasako')
        self.zaapMerkasako = self.builder.get_object('lblZaapMerkasako')
        self.buscarZaap = self.builder.get_object('lblBuscarZaap')
        self.teleportMerka = self.builder.get_object('lblTeleportMerka')
        self.coordChat = self.builder.get_object('lblCoordChat')
        #self.levelHunt = self.builder.get_object('levelHunt')

        self.reloadNav = self.builder.get_object('lblReload')
        self.navX = self.builder.get_object('lblX')
        self.navY = self.builder.get_object('lblY')
        self.navHint = self.builder.get_object('lblHint')

        self.cboxHuntlvl = self.builder.get_object('cboxHuntlvl')

        #Para resources
        self.image_offset = 25
        self.image_path = None
        self.running = False
        self.search_area = None
        

        # Config data
        ## areas
        self.area_game_coord = None
        self.area_etapa_actual = None
        self.area_salida = None
        self.area_pistas = None ## cantidad símbolos de '?'
        self.area_chat = None

        ## pistas - areas
        self.area_pista_1 = None
        self.area_pista_2 = None
        self.area_pista_3 = None
        self.area_pista_4 = None
        self.area_pista_5 = None 
        self.area_pista_6 = None 

        ## pistas - areas (dirección)
        self.area_arriba = None
        self.area_abajo = None
        self.area_izquierda = None
        self.area_derecha = None
        self.etapa_iniciada = False 
        self.area_pistaD_6 = None

        ## flechas - areas
        self.area_flecha_1 = None
        self.area_flecha_2 = None
        self.area_flecha_3 = None
        self.area_flecha_4 = None
        self.area_flecha_5 = None
        self.area_flecha_6 = None

        ## bot data
        self.mapas_avanzados = 0
        self.numero_pista = 0

        self.load_from_text_file()

    def run(self):
        self.mainwindow.mainloop()

    def load_images(self):
        image_folder = "./resources"
        images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        for image in images:
            self.image_listbox.insert("end", image)

    # seleccion de area y obtención de area
    def select_area(self):
        #self.root.withdraw()
        self.mainwindow.withdraw()
        self.area_selector_window = Toplevel(self.mainwindow)
        self.area_selector_window.title("Select Area")
        self.area_selector_window.attributes('-alpha', 0.3)  # Set transparency level
        self.area_selector_window.attributes('-topmost', True)  # Ensure it's on top
        self.area_selector_window.overrideredirect(True)  # Remove window borders

        screen_width, screen_height = pyautogui.size()
        self.area_selector_window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.canvas = Canvas(self.area_selector_window, cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        #self.root.wait_window(self.area_selector_window)
        #self.root.deiconify()
        self.mainwindow.wait_window(self.area_selector_window)
        self.mainwindow.deiconify()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        self.end_x = event.x
        self.end_y = event.y

        # Asegúrate de que x1 < x2 y y1 < y2
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)

        # Guarda las coordenadas absolutas
        self.search_area = (x1, y1, x2, y2)
        self.area_selector_window.destroy()
        self.status_label.config(text=f"Status: Area selected {self.search_area}")

    # busca imagen, posiciona el cursor sobre el y le da click
    def check_image(self):
        while self.running:
            try:
                pos = pyautogui.locateOnScreen(self.image_path, region=self.search_area, confidence=0.8) if self.search_area else pyautogui.locateOnScreen(self.image_path, confidence=0.8)
                if pos:
                    pyautogui.moveTo(pos[0] + self.image_offset, pos[1] + self.image_offset)
                    pyautogui.click()
                    self.status_label.config(text=f"Status: Found image at {pos}")
                else:
                    self.status_label.config(text="Status: Image not found")
                time.sleep(5)
            except Exception as e:
                self.status_label.config(text=f"Error: {str(e)}")
                self.stop_search()

    def buscar_image(self, ruta_imagen_a_buscar):
        self.capturaPantalla()
        time.sleep(1)
        img_grande = cv2.imread(ruta_imagen_captura, cv2.IMREAD_COLOR)
        img_fragmento = cv2.imread(ruta_imagen_a_buscar, cv2.IMREAD_COLOR)

        resultado = cv2.matchTemplate(img_grande, img_fragmento, cv2.TM_CCOEFF_NORMED)

        # Definir un umbral para determinar si hay coincidencia
        umbral = 0.8
        _, max_val, _, _ = cv2.minMaxLoc(resultado)

        if max_val >= umbral:
            return True
        else:
            return False

    # Funciones para configurar areas
    def configCoordActual(self):
        self.select_area()
        self.area_game_coord = self.search_area
        self.checkGameCoord()
    
    def configEtapaActual(self):
        self.select_area()
        self.area_etapa_actual = self.search_area
        self.checkEtapa()

    def configSalida(self):
        self.select_area()
        self.area_salida = self.search_area
        self.checkSalida()
        
    def configPistas(self):
        self.select_area()
        self.area_pistas = self.search_area
        self.checkPistas()

    def configPista1(self):
        self.select_area()
        self.area_pista_1 = self.search_area
        self.pista1.config(text=f"{self.area_pista_1}")

    def configPista2(self):
        self.select_area()
        self.area_pista_2 = self.search_area
        self.pista2.config(text=f"{self.area_pista_2}")
    
    def configPista3(self):
        self.select_area()
        self.area_pista_3 = self.search_area
        self.pista3.config(text=f"{self.area_pista_3}")

    def configPista4(self):
        self.select_area()
        self.area_pista_4 = self.search_area
        self.pista4.config(text=f"{self.area_pista_4}")

    def configPista5(self):
        self.select_area()
        self.area_pista_5 = self.search_area
        self.pista5.config(text=f"{self.area_pista_5}")
    
    def configPista6(self):
        self.select_area()
        self.area_pista_6 = self.search_area
        self.pista6.config(text=f"{self.area_pista_6}")

    def configFlecha1(self):
        self.select_area()
        self.area_flecha_1 = self.search_area
        self.flecha1.config(text=f"{self.area_flecha_1}")

    def configFlecha2(self):
        self.select_area()
        self.area_flecha_2 = self.search_area
        self.flecha2.config(text=f"{self.area_flecha_2}")
    
    def configFlecha3(self):
        self.select_area()
        self.area_flecha_3 = self.search_area
        self.flecha3.config(text=f"{self.area_flecha_3}")

    def configFlecha4(self):
        self.select_area()
        self.area_flecha_4 = self.search_area
        self.flecha4.config(text=f"{self.area_flecha_4}")

    def configFlecha5(self):
        self.select_area()
        self.area_flecha_5 = self.search_area
        self.flecha5.config(text=f"{self.area_flecha_5}")

    def configFlecha6(self):
        self.select_area()
        self.area_flecha_6 = self.search_area
        self.flecha6.config(text=f"{self.area_flecha_6}")

    def configMoverArriba(self):
        self.select_area()
        self.area_arriba = self.search_area
        self.moverArriba.config(text=f"{self.area_arriba}")
    
    def configMoverAbajo(self):
        self.select_area()
        self.area_abajo = self.search_area
        self.moverAbajo.config(text=f"{self.area_abajo}")
    
    def configMoverIzquierda(self):
        self.select_area()
        self.area_izquierda = self.search_area
        self.moverIzquierda.config(text=f"{self.area_izquierda}")

    def configMoverDerecha(self):
        self.select_area()
        self.area_derecha = self.search_area
        self.moverDerecha.config(text=f"{self.area_derecha}")

    def configDireccionPista5(self):
        self.select_area()
        self.etapa_iniciada = self.search_area
        self.pistaD5.config(text=f"{self.etapa_iniciada}")

    def configDireccionPista6(self):
        self.select_area()
        self.area_chat = self.search_area
        self.chat.config(text=f"{self.area_chat}")
    
    def configDireccionLPista1(self):
        self.select_area()
        area_btnMerkasako = self.search_area
        self.btnMerkasako.config(text=f"{area_btnMerkasako}")

    def configDireccionLPista2(self):
        self.select_area()
        area_zaap_merkasako = self.search_area
        self.zaapMerkasako.config(text=f"{area_zaap_merkasako}")

    def configDireccionLPista3(self):
        self.select_area()
        area_buscar_zaap = self.search_area
        self.buscarZaap.config(text=f"{area_buscar_zaap}")

    def configDireccionLPista4(self):
        self.select_area()
        area_teleport_merka = self.search_area
        self.teleportMerka.config(text=f"{area_teleport_merka}")

    def configSetCoordchat(self):
        self.select_area()
        texto_coord_chat = self.search_area
        self.coordChat.config(text=f"{texto_coord_chat}")

    def configDireccionLPista6(self):
        self.select_area()
        self.area_pistaDL_6 = self.search_area
        self.pistaDL6.config(text=f"{self.area_pistaDL_6}")

    def configChat(self):
        self.select_area()
        texto_area_chat = self.search_area
        self.chat.config(text=f"{texto_area_chat}")

    def configNavReload(self):
        self.select_area()
        texto = self.search_area
        self.reloadNav.config(text=f"{texto}")

    def configNavX(self):
        self.select_area()
        texto = self.search_area
        self.navX.config(text=f"{texto}")

    def configNavY(self):
        self.select_area()
        texto = self.search_area
        self.navY.config(text=f"{texto}")

    def configNavHint(self):
        self.select_area()
        texto = self.search_area
        self.navHint.config(text=f"{texto}")

    ##probar
    def configArea(self, container):
        self.select_area()
        texto = self.search_area
        container.config(text=f"{texto}")

    def get4CoordFromText(self, texto):
        texto = texto.strip("()")
        coords = texto.split(", ")

        if len(coords) == 4:
            x1, y1, x2, y2 = map(int, coords)  # Convierte cada valor a entero
            c1 = int(x1)
            c2 = int(y1)
            return c1, c2  # Utiliza c1 y c2
        else:
            print("Error: No se encontraron exactamente 4 valores en la cadena.")

    def condicion_perforatroz(self, texto_hasta_coma, comienzo_perfo_actual):
        texto_hasta_coma = texto_hasta_coma
        #self.checkGameCoord()
        inicio_perfo_texto = comienzo_perfo_actual
        inicio_perfo_texto = self.cleanText(inicio_perfo_texto)
        primer_numero, segundo_numero = inicio_perfo_texto.split(',')
        primer_numero = int(primer_numero)
        segundo_numero = int(segundo_numero)

        coord_actual_texto = self.coordActual['text']
        coord_actual_texto = self.cleanText(coord_actual_texto)
        primer_coord, segundo_coord = coord_actual_texto.split(',')
        primer_coord = int(primer_coord)
        segundo_coord = int(segundo_coord)


        self.mapas_avanzados = self.mapas_avanzados + 1
        print(f"mapas buscando perforatroz: {self.mapas_avanzados}")

        ##c1, c2 = comienzo_perfo_actual
        if(self.mapas_avanzados > 10):
            self.clickEnImagen(ruta_imagen_chat_box)
            pyautogui.write(f"/travel {primer_numero} {segundo_numero}")
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            self.clickEnImagen(ruta_imagen_llegado_destino)
            chatBox(ruta_imagen_chat_box)
            pyautogui.write('/clear')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')
            self.mapas_avanzados = 0

        if texto_hasta_coma == "Dirigete hacia el Sur,":
            # funcion para moverse abajo
            time.sleep(2)
            print(self.moverAbajo['text'])
            texto = self.moverAbajo['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(5)
            self.buscar_y_clickear_perforatroz(texto_hasta_coma, comienzo_perfo_actual)
        elif texto_hasta_coma == "Dirigete hacia el Norte,":
            # funcion para moverse arriba
            time.sleep(2)
            print(self.moverArriba['text'])
            texto = self.moverArriba['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(5)
            self.buscar_y_clickear_perforatroz(texto_hasta_coma, comienzo_perfo_actual)

        elif texto_hasta_coma == "Dirigete hacia el Oeste,":
            # funcion para moverse izquierda
            time.sleep(2)
            print(self.moverIzquierda['text'])
            texto = self.moverIzquierda['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(5)
            self.buscar_y_clickear_perforatroz(texto_hasta_coma, comienzo_perfo_actual)
        elif texto_hasta_coma == "Dirigete hacia el Este,":
            # funcion para moverse derecha
            time.sleep(2)
            print(self.moverDerecha['text'])
            texto = self.moverDerecha['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(5)
            self.buscar_y_clickear_perforatroz(texto_hasta_coma, comienzo_perfo_actual)

    def buscar_y_clickear_perforatroz(self, texto_hasta_coma, coordActual):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        # Lista de rutas alternativas de imágenes
        rutas_alternativas = ["./treasureHunt/perforatroz.png", 
                            './treasureHunt/perforatroz3.png', './treasureHunt/perforatroz4.png',
                            './treasureHunt/perforatroz5.png', './treasureHunt/perforatroz15.png'
                            ]

        time.sleep(3)
        for ruta_alternativa in rutas_alternativas:
            # Capturar la pantalla en cada iteración
            x1, y1, x2, y2 = 330, 50, 1580, 900
            captura_pantalla = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
            
            imagen_referencia = cv2.imread(ruta_alternativa)
            if imagen_referencia is not None:
                # Obtén las dimensiones de la imagen de referencia
                altura, ancho, _ = imagen_referencia.shape
                # Encuentra la posición de la imagen de referencia en la captura de pantalla
                resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
                # Define un umbral de confianza (puedes ajustar según tus necesidades)
                umbral_confianza = 0.8
                print(max_val)
                if max_val >= umbral_confianza:
                    print(f"se encontró la imagen en la ruta: {ruta_alternativa}")
                    self.clickEnImagen(ruta_imagen_maxBusqueda)
                    time.sleep(2)
                    self.banderita(ruta_imagen_banderita)
                    #time.sleep(0.5)
                    #recorte_cordenada_juego(ruta_imagen_captura)
                    #time.sleep(0.5)
                    #cordenadas_juegos()
                    return  # Termina el bucle ya que se encontró y clickeó una imagen
                    
        self.condicion_perforatroz(texto_hasta_coma, coordActual)

    # Chequeo de datos
    def checkGameCoord(self):
        #self.recorte_Imagen(ruta_imagen_captura, self.area_game_coord)
        #time.sleep(0.5)

        #ruta_tesseract = self.entryPytesseract.get()
        #pytesseract.pytesseract.tesseract_cmd = fr'{ruta_tesseract}\tesseract.exe'
        
        # Leer la imagen recortada
        #imagen = cv2.imread(ruta_imagen_recortada)
        
        # Convertir la imagen a escala de grises
        #imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Aplicar un umbral binario para convertir la imagen a blanco y negro
        #_, imagen_bn = cv2.threshold(imagen_gris, 150, 255, cv2.THRESH_BINARY)
        
        # Realizar OCR en la imagen en blanco y negro
        #salida_actual_texto = pytesseract.image_to_string(imagen_bn)
        
        #print(f"salida de texto {salida_actual_texto}")
        merkaX, merkaY = self.get4CoordFromText(self.btnMerkasako['text'])
        pyautogui.click(merkaX, merkaY)
        time.sleep(2)
        chatX, chatY = self.get4CoordFromText(self.chat['text'])
        pyautogui.click(chatX, chatY)
        pyautogui.write('/clear')
        pyautogui.press('enter')
        pyautogui.write('%pos%')
        pyautogui.press('enter')
        time.sleep(2)
        chatCoordX, chatCoordY = self.get4CoordFromText(self.coordChat['text'])
        pyautogui.tripleClick(chatCoordX, chatCoordY)
        pyautogui.hotkey('ctrl', 'c')
        ruta_actual_copy = pyperclip.paste()

        if '[0,0]' in ruta_actual_copy:
            pyautogui.click(chatX, chatY)
            pyautogui.write('/clear')
            pyautogui.press('enter')
            pyautogui.write('%pos%')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.tripleClick(chatCoordX, chatCoordY)
            pyautogui.hotkey('ctrl', 'c')
            ruta_actual_copy = pyperclip.paste()
        #character_name = self.characterName.get()
        #ruta_actual_copy = ruta_actual_copy.replace(f'{character_name}:', '')
        #ruta_actual_copy = ruta_actual_copy.replace('[', '')
        #ruta_actual_copy = ruta_actual_copy.replace(']', '').strip()
        # Filtrar solo los números de la salida
        salida_actual_texto = re.findall(r'-?\d+', ruta_actual_copy)
        print(f"salida de texto filtrada {salida_actual_texto}")
        pyautogui.click(chatX, chatY)
        pyautogui.write('/clear')
        time.sleep(2)
        pyautogui.press('enter')
        
        # Extraer coordenadas
        #salida_actual_texto = salida_actual_texto.split(',')
        c1 = salida_actual_texto[0]
        c2 = salida_actual_texto[1]
        
        # Actualizar las coordenadas en la interfaz
        game_coords = (c1, c2)
        self.coordActual.config(text=f"{game_coords}")
        self.coordActual.update_idletasks()
        pyautogui.click(merkaX, merkaY)
        time.sleep(2)

    
    def checkEtapa(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_etapa_actual)
        primer_numero, segundo_numero = self.verificacion_etapas(ruta_imagen_captura)
        etapa_actual = (primer_numero, segundo_numero)
        self.etapaActual.config(text=f"{etapa_actual}")
        self.etapaActual.update_idletasks()

    def checkPistas(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_pistas)
        cantidad = cantidad_pistas(ruta_imagen_recortada)
        print(cantidad)
        pistas_actual = cantidad
        self.cantidadPistas.config(text=f"{pistas_actual}")
        self.cantidadPistas.update_idletasks()

    def checkSalida(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
        time.sleep(2)
        ruta_tesseract = self.entryPytesseract.get()
        pytesseract.pytesseract.tesseract_cmd = fr'{ruta_tesseract}\tesseract.exe'

        imagen = cv2.imread(ruta_imagen_recortada)

        # Convertir la imagen a escala de grises
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Aumentar el contraste usando CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(9, 8))
        imagen_contrastada = clahe.apply(imagen_gris)

        # Aplicar umbralización para mejorar la definición del texto
        _, imagen_umbral = cv2.threshold(imagen_contrastada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Realizar OCR en la imagen preprocesada
        salida_actual_texto = pytesseract.image_to_string(imagen_umbral)
        print('texto generado por pytesseract')
        print(salida_actual_texto)

        # Extraer números de la salida
        salida_actual_texto = re.findall(r'-?\d+', salida_actual_texto)

        # Procesar los números
        c1 = salida_actual_texto[0]
        c2 = salida_actual_texto[1]
        salida_actual = (c1, c2) 

        self.salida.config(text=f"{salida_actual}")
        self.salida.update_idletasks()

    def capturaPantalla(self):
        imagen = pyautogui.screenshot()
        imagen.save(ruta_imagen_captura)
        time.sleep(0.5)

    #otros
    def recorte_Imagen(self, ruta_imagen, coords):
        imagen = pyautogui.screenshot()
        imagen.save(ruta_imagen_captura)
        imagen = cv2.imread(ruta_imagen)

        if imagen is None:
            raise FileNotFoundError(f"No se pudo cargar la imagen en la ruta: {ruta_imagen}")

        # Definir las coordenadas del recorte (x1, y1, x2, y2)
        x1, y1, x2, y2 = coords

        # Verifica que las coordenadas estén dentro del rango
        height, width = imagen.shape[:2]
        if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
            raise ValueError("Las coordenadas de recorte están fuera de los límites de la imagen.")

        # Recortar la región de interés
        recorte = imagen[y1:y2, x1:x2]

        # Verifica si el recorte es válido
        if recorte.size == 0:
            raise ValueError("El recorte resultante está vacío. Verifica las coordenadas.")

        # Guardar el recorte en un archivo (opcional)
        cv2.imwrite(ruta_imagen_recortada, recorte)

    def cleanText(self, text):
        texto = text
        texto = texto.replace('(', '')
        texto = texto.replace(')', '')
        texto = texto.replace("'", "") 
        return texto

    def coordEnNav(self, inicio):
        #escribe coord en navegador
        #buscar_y_clickear_chrome(ruta_imagen_chrome)
        #salida_actual_texto = self.coordActual['text']
        salida_actual_texto = self.cleanText(inicio)
        salida_actual_texto = re.findall(r'-?\d+', salida_actual_texto)
        c1 = salida_actual_texto[0]
        c2 = salida_actual_texto[1]
        #print(salida_actual_texto)
        #c1, c2 = salida_actual_texto.split(',')
        #c1 = c1.strip()
        #c2 = c2.strip()
        #time.sleep(1)
        #pyautogui.tripleClick(731, 360)
        self.clickEnImagen(ruta_imagen_navegador1)
        #self.clickEnImagen(ruta_imagen_reload_navegador)
        #time.sleep(2)
        #self.clickEnImagen(ruta_imagen_X_navegador)
        print('click en X')
        xnavX, xnavY = self.get4CoordFromText(self.navX['text'])
        pyautogui.tripleClick(xnavX, xnavY)
        time.sleep(2)
        pyautogui.write(c1)
        time.sleep(2)
        #pyautogui.press('tab')
        #self.clickEnImagen(ruta_imagen_Y_navegador)
        print('click en Y')
        ynavX, ynavY = self.get4CoordFromText(self.navY['text'])
        pyautogui.tripleClick(ynavX, ynavY)
        time.sleep(2)
        pyautogui.write(c2)
        time.sleep(2)

    def moverEnDireccion(self, direccion):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        #buscar_y_clickear_dofus(ruta_imagen_dofus)
        # Lista de rutas alternativas de imágenes
        texto_hasta_coma = direccion  # Toma la primera parte antes de la coma
        if texto_hasta_coma == "Dirigete hacia el Sur,":
            navegacion_flechas(ruta_imagen_flecha_abajo2)
            time.sleep(0.5)
            return texto_hasta_coma
        elif texto_hasta_coma == "Dirigete hacia el Norte,":
            navegacion_flechas(ruta_imagen_flecha_arriba2)
            time.sleep(0.5)
            return texto_hasta_coma
        elif texto_hasta_coma == "Dirigete hacia el Oeste,":
            navegacion_flechas(ruta_imagen_flecha_izquierda2)
            time.sleep(0.5)
            return texto_hasta_coma
        elif texto_hasta_coma == "Dirigete hacia el Este,":
            navegacion_flechas(ruta_imagen_flecha_derecha2)
            time.sleep(0.5)
            return texto_hasta_coma

        # Si ninguna de las imágenes alternativas fue encontrada
        else:
            self.moverEnDireccion(texto_hasta_coma)

    def clickEnImagen(self, ruta_imagen):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        # Carga la imagen de referencia y la captura de pantalla
        imagen_referencia = cv2.imread(ruta_imagen)
        captura_pantalla = pyautogui.screenshot()
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
        # Obtén las dimensiones de la imagen de referencia
        altura, ancho, _ = imagen_referencia.shape
        # Encuentra la posición de la imagen de referencia en la captura de pantalla
        resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
        # Define un umbral de confianza (puedes ajustar según tus necesidades)
        #print(f"max umbral {float(self.umbral.get())} max value {max_val}")
        umbral_confianza = float(self.umbral.get())
        print(max_val)
        if max_val >= umbral_confianza:
            # Obtiene las coordenadas del centro de la imagen de referencia
            centro_x = max_loc[0] + ancho // 2
            centro_y = max_loc[1] + altura // 2
            # Haz clic en el centro de la imagen encontrada
            pyautogui.click(centro_x, centro_y)
            time.sleep(1)
        else:
            self.clickEnImagen(ruta_imagen)     

    def OCR(self, ruta_imagen):
        # Configura la ruta al ejecutable de Tesseract (puede variar según tu instalación)
        ruta_tesseract = self.entryPytesseract.get()
        pytesseract.pytesseract.tesseract_cmd = fr'{ruta_tesseract}\tesseract.exe'
        imagen = cv2.imread(ruta_imagen)
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Realizar OCR en la región recortada
        texto = pytesseract.image_to_string(gray)
        #print(texto)
        texto = texto.replace("\n", "")
        #texto = texto.replace("6", "o")
        texto = texto.replace("‘", "'")
        texto = texto.replace("’", "'")
        texto = texto.replace("}", "")
        texto = texto.replace("]", "")
        texto = texto.replace("|", "")
        texto = texto.replace("_", "")
        texto = texto.replace(".", "")
        texto = texto.replace("eee", "")

        if "Afiche" in texto:
            texto = texto
            return texto
        elif "Champifién" in texto:
            texto = texto.replace("Champifién", "Champinon")
            return texto
        elif "vinturén" in texto:
            texto = texto.replace("vinturén", "Cinturon")
            return texto
        elif "coraz6n" in texto:
            texto = texto.replace("coraz6n", "corazon")
            return texto
        elif "plstico" in texto:
            texto = texto.replace("plstico", "plastico")
            return texto
        elif "Pescado ala plancha en brocheta" in texto:
            texto = texto.replace("Pescado ala plancha en brocheta", "Pescado a la plancha en brocheta")
            return texto
        elif "Cintur6n" in texto:
            texto = texto.replace("Cintur6n", "Cinturon")
            return texto
        elif "croneo" in texto:
            texto = texto.replace("croneo", "craneo")
            return texto
        elif "crneo" in texto:
            texto = texto.replace("crneo", "craneo")
            return texto
        elif "Ilave" in texto:
            texto = texto.replace("Ilave", "llave")
            return texto
        elif ")jo de fab'huritu pintado" in texto:
            texto = texto.replace(")jo", "Ojo")
            return texto
        elif "Seeneaidadvaadan" in texto:
            texto = texto.replace("Seeneaidadvaadan", "Craneo de tymador")
            return texto
        elif "Cajia para kebab" in texto:
            texto = texto.replace("Cajia para kebab", "Cana para kebab")
            return texto
        elif "aquiero" in texto:
            texto = texto.replace("aquiero", "agujero")
            return texto
        elif "Craneo det urikornio" in texto:
            texto = texto.replace("Craneo det urikornio", "Craneo de urikornio")
            return texto
        elif "- Craneo" in texto:
            texto = texto.replace("- Craneo", "Craneo")
            return texto
        elif "sedimentacién" in texto:
            texto = texto.replace("sedimentacién", "sedimentacion")
            return texto
        elif "Roca tallada en espinas de" in texto:
            texto = "Roca tallada en espinas de pescado"
            return texto
        elif "Bot6n" in texto:
            texto = texto.replace("Bot6n", "Boton")
            return texto
        elif "Telade cuadros anudada" in texto:
            texto = texto.replace("Telade cuadros anudada", "Tela de cuadros anudada")
            return texto
        elif "Espantapdjaros" in texto:
            texto = texto.replace("Espantapdjaros", "Espantapajaros")
            return texto
        elif "pleaado" in texto:
            texto = texto.replace("pleaado", "plegado")
            return texto
        elif "draaopavo" in texto:
            texto = texto.replace("draaopavo", "Veleta de dragopavo")
            return texto
        elif "Triao blanco vy nearo" in texto:
            texto = texto.replace("Triao blanco vy nearo", "Trigo blanco y negro")
            return texto
        elif "Crdneo" in texto:
            texto = texto.replace("Crdneo", "Craneo")
            return texto
        elif "*ruz de piedra rota" in texto:
            texto = texto.replace("*ruz", "Cruz")
            return texto
        elif "Seamed nicatee" in texto:
            texto = texto.replace("Seamed nicatee", "Tetera con rayas")
            return texto
        elif "ensanarentada" in texto:
            texto = texto.replace("ensanarentada", "ensangrentada")
            return texto
        elif "Champifion rayadoee" in texto:
            texto= texto.replace("Champifion rayadoee", "Champinon rayado")
            return texto
        elif "Créneo" in texto:
            texto = texto.replace("Créneo", "Craneo")
            return texto
        elif "Craneo de « ocra" in texto:
            texto = texto.replace("Craneo de « ocra", "Craneo de ocra")
            return texto
        elif "rosade" in texto:
            texto = texto.replace("rosade", "rosa de")
            return texto
        elif "See" in texto:
            texto = "Rosa negra"
            return texto
        elif "Este" in texto:
            texto = "Dirigete hacia el Este"
            return texto
        elif "Norte" in texto:
            texto = "Dirigete hacia el Norte"
            return texto
        elif "Oeste" in texto:
            texto = "Dirigete hacia el Oeste"
            return texto
        elif "el Sur" in texto:
            texto = "Dirigete hacia el Sur"
            return texto
        elif "é" in texto:
            texto = texto.replace("é", "o")
            return texto
        elif "ó" in texto:
            texto = texto.replace("ó", "o")
            return texto
        elif "fi" in texto:
            if "firefux" in texto:
                texto = texto
            else:
                texto = texto.replace("fi", "n")
            return texto
        else:
            return texto

    def verificacion_etapas(self, ruta_imagen):
        recorte_etapas(ruta_imagen)
        texto = self.OCR(ruta_imagen_recortada)
        texto = texto.strip()
        
        print(f"Texto extraído por OCR: '{texto}'")  # Agregar impresión de depuración
        
        # Separar la información usando el método split(' ')
        separado = texto.split(' ')
        
        if len(separado) < 2:
            raise ValueError(f"El texto extraído no tiene el formato esperado: '{texto}'")
        
        # Buscar los números en la última parte de la cadena
        numeros = separado[-1].split('/')
        
        if len(numeros) < 2:
            raise ValueError(f"No se encontraron dos números separados por '/'. Texto procesado: '{separado[-1]}'")
        
        # Guardar los números en variables separadas
        primer_numero = numeros[0]
        segundo_numero = numeros[1]
        return primer_numero, segundo_numero

    #save/load
    def save_to_text_file(self):
        with open('variables.txt', 'w') as file:

            # Áreas de recorte
            file.write(f"area_game_coord: {self.area_game_coord}\n")
            file.write(f"area_etapa_actual: {self.area_etapa_actual}\n")
            file.write(f"area_salida: {self.area_salida}\n")
            file.write(f"area_chat: {self.area_chat}\n")

            #'?'
            file.write(f"area_pistas: {self.area_pistas}\n")
            
            #pistas (texto) (flecha - pista - banderita)
            file.write(f"area_pista1: {self.area_pista_1}\n")
            file.write(f"area_pista2: {self.area_pista_2}\n")
            file.write(f"area_pista3: {self.area_pista_3}\n")
            file.write(f"area_pista4: {self.area_pista_4}\n")
            file.write(f"area_pista5: {self.area_pista_5}\n")
            file.write(f"area_pista6: {self.area_pista_6}\n")

            #flechas
            file.write(f"area_flecha_1: {self.area_flecha_1}\n")
            file.write(f"area_flecha_2: {self.area_flecha_2}\n")
            file.write(f"area_flecha_3: {self.area_flecha_3}\n")
            file.write(f"area_flecha_4: {self.area_flecha_4}\n")
            file.write(f"area_flecha_5: {self.area_flecha_5}\n")
            file.write(f"area_flecha_6: {self.area_flecha_6}\n")

            #pista (direccion)
            file.write(f"area_moverArriba: {self.area_arriba}\n")
            file.write(f"area_moverAbajo: {self.area_abajo}\n")
            file.write(f"area_moverIzquierda: {self.area_izquierda}\n")
            file.write(f"area_moverDerecha: {self.area_derecha}\n")
            file.write(f"etapa_iniciada: {self.etapa_iniciada}\n")
            file.write(f"area_chat: {self.chat['text']}\n")

            file.write(f"area_merkasako: {self.btnMerkasako['text']}\n")
            file.write(f"area_zaap_merka: {self.zaapMerkasako['text']}\n")
            file.write(f"area_buscar_zaap: {self.buscarZaap['text']}\n")
            file.write(f"area_teleport_merka: {self.teleportMerka['text']}\n")
            file.write(f"area_coord_chat: {self.coordChat['text']}\n")
            file.write(f"levelHunt: {self.cboxHuntlvl.get()}\n")

            file.write(f"ruta_tesseract: {self.entryPytesseract.get()}\n")
            file.write(f"umbral: {self.umbral.get()}\n")

            file.write(f"reloadNav: {self.reloadNav['text']}\n")
            file.write(f"XNav: {self.navX['text']}\n")
            file.write(f"YNav: {self.navY['text']}\n")
            file.write(f"hintNav: {self.navHint['text']}\n")
        
        self.status_label.config(text=f"Datos guardados")

    def load_from_text_file(self):
        with open('variables.txt', 'r') as file:
            lines = file.readlines()

            if len(lines) > 0 and lines[0].strip():
                self.area_game_coord = eval(lines[0].split(': ')[1].strip())
                #self.checkGameCoord()

            if len(lines) > 1 and lines[1].strip():
                self.area_etapa_actual = eval(lines[1].split(': ')[1].strip())
                #self.checkEtapa()

            if len(lines) > 2 and lines[2].strip():
                self.area_salida = eval(lines[2].split(': ')[1].strip())
                #self.checkSalida()

            if len(lines) > 3 and lines[3].strip():
                texto_area_chat = eval(lines[3].split(': ')[1].strip())   
                self.chat.config(text=f"{texto_area_chat}")

            if len(lines) > 4 and lines[4].strip():
                self.area_pistas = eval(lines[4].split(': ')[1].strip())
                #self.checkPistas()

            if len(lines) > 5 and lines[5].strip():
                self.area_pista_1 = eval(lines[5].split(': ')[1].strip())
                self.pista1.config(text=f"{self.area_pista_1}")

            if len(lines) > 6 and lines[6].strip():
                self.area_pista_2 = eval(lines[6].split(': ')[1].strip())
                self.pista2.config(text=f"{self.area_pista_2}")

            if len(lines) > 7 and lines[7].strip():
                self.area_pista_3 = eval(lines[7].split(': ')[1].strip())
                self.pista3.config(text=f"{self.area_pista_3}")

            if len(lines) > 8 and lines[8].strip():
                self.area_pista_4 = eval(lines[8].split(': ')[1].strip())
                self.pista4.config(text=f"{self.area_pista_4}")

            if len(lines) > 9 and lines[9].strip():
                self.area_pista_5 = eval(lines[9].split(': ')[1].strip())
                self.pista5.config(text=f"{self.area_pista_5}")

            if len(lines) > 10 and lines[10].strip():
                self.area_pista_6 = eval(lines[10].split(': ')[1].strip())
                self.pista6.config(text=f"{self.area_pista_6}")

            if len(lines) > 11 and lines[11].strip():
                self.area_flecha_1 = eval(lines[11].split(': ')[1].strip())
                self.flecha1.config(text=f"{self.area_flecha_1}")

            if len(lines) > 12 and lines[12].strip():
                self.area_flecha_2 = eval(lines[12].split(': ')[1].strip())
                self.flecha2.config(text=f"{self.area_flecha_2}")

            if len(lines) > 13 and lines[13].strip():
                self.area_flecha_3 = eval(lines[13].split(': ')[1].strip())
                self.flecha3.config(text=f"{self.area_flecha_3}")

            if len(lines) > 14 and lines[14].strip():
                self.area_flecha_4 = eval(lines[14].split(': ')[1].strip())
                self.flecha4.config(text=f"{self.area_flecha_4}")

            if len(lines) > 15 and lines[15].strip():
                self.area_flecha_5 = eval(lines[15].split(': ')[1].strip())
                self.flecha5.config(text=f"{self.area_flecha_5}")

            if len(lines) > 16 and lines[16].strip():
                self.area_flecha_6 = eval(lines[16].split(': ')[1].strip())
                self.flecha6.config(text=f"{self.area_flecha_6}")

            if len(lines) > 17 and lines[17].strip():
                self.area_arriba = eval(lines[17].split(': ')[1].strip())
                self.moverArriba.config(text=f"{self.area_arriba}")

            if len(lines) > 18 and lines[18].strip():
                self.area_abajo = eval(lines[18].split(': ')[1].strip())
                self.moverAbajo.config(text=f"{self.area_abajo}")

            if len(lines) > 19 and lines[19].strip():
                self.area_izquierda = eval(lines[19].split(': ')[1].strip())
                self.moverIzquierda.config(text=f"{self.area_izquierda}")

            if len(lines) > 20 and lines[20].strip():
                self.area_derecha = eval(lines[20].split(': ')[1].strip())
                self.moverDerecha.config(text=f"{self.area_derecha}")

            if len(lines) > 21 and lines[21].strip():
                self.etapa_iniciada = eval(lines[21].split(': ')[1].strip())
                self.pistaD5.config(text=f"{self.etapa_iniciada}")

            if len(lines) > 22 and lines[22].strip():
                texto_chat = eval(lines[22].split(': ')[1].strip())
                self.chat.config(text=f"{texto_chat}")

            if len(lines) > 23 and lines[23].strip():
                texto_area_merkasako = eval(lines[23].split(': ')[1].strip())
                self.btnMerkasako.config(text=f"{texto_area_merkasako}")

            if len(lines) > 24 and lines[24].strip():
                area_zaap_merka = eval(lines[24].split(': ')[1].strip())
                self.zaapMerkasako.config(text=f"{area_zaap_merka}")

            if len(lines) > 25 and lines[25].strip():
                area_buscar_merka = eval(lines[25].split(': ')[1].strip())
                self.buscarZaap.config(text=f"{area_buscar_merka}")

            if len(lines) > 26 and lines[26].strip():
                area_teleport_merka = eval(lines[26].split(': ')[1].strip())
                self.teleportMerka.config(text=f"{area_teleport_merka}")

            if len(lines) > 27 and lines[27].strip():
                texto_chat_coord = eval(lines[27].split(': ')[1].strip())
                self.coordChat.config(text=f"{texto_chat_coord}")

            if len(lines) > 28 and lines[28].strip():
                texto_charcater_name = lines[28].split(': ')[1].strip()
                self.cboxHuntlvl.set(texto_charcater_name)
                #self.characterName.insert(0, f"{texto_charcater_name}")

            if len(lines) > 29 and lines[29].strip():
                texto_entryPytesseract = lines[29].strip()
                texto_entryPytesseract = texto_entryPytesseract.replace('ruta_tesseract: ', '')
                self.entryPytesseract.insert(0, texto_entryPytesseract)

            if len(lines) > 30 and lines[30].strip():
                texto_umbral = eval(lines[30].split(': ')[1].strip())
                self.umbral.insert(0, texto_umbral)     

            if len(lines) > 31 and lines[31].strip():
                texto = eval(lines[31].split(': ')[1].strip())
                self.reloadNav.config(text=f"{texto}")

            if len(lines) > 32 and lines[32].strip():
                texto = eval(lines[32].split(': ')[1].strip())
                self.navX.config(text=f"{texto}") 

            if len(lines) > 33 and lines[33].strip():
                texto = eval(lines[33].split(': ')[1].strip())
                self.navY.config(text=f"{texto}") 

            if len(lines) > 34 and lines[34].strip():
                texto = eval(lines[34].split(': ')[1].strip())
                self.navHint.config(text=f"{texto}") 
        
        self.status_label.config(text=f"Datos cargados")

    def resize_image_if_needed(self, imagen, plantilla):
        h_imagen, w_imagen = imagen.shape[:2]
        h_plantilla, w_plantilla = plantilla.shape[:2]

        if h_plantilla > h_imagen or w_plantilla > w_imagen:
            scale_height = h_imagen / h_plantilla
            scale_width = w_imagen / w_plantilla
            scale = min(scale_height, scale_width)
            plantilla = cv2.resize(plantilla, (int(w_plantilla * scale), int(h_plantilla * scale)))
        
        return plantilla

    def detectar_direccion(self):
        # Cargar la imagen que se quiere analizar
        imagen = cv2.imread(ruta_imagen_recortada, cv2.IMREAD_GRAYSCALE)

        # Cargar las imágenes de referencia de las flechas
        flecha_arriba = cv2.imread(ruta_imagen_flecha_arriba1, cv2.IMREAD_GRAYSCALE)
        flecha_abajo = cv2.imread(ruta_imagen_flecha_abajo1, cv2.IMREAD_GRAYSCALE)
        flecha_izquierda = cv2.imread(ruta_imagen_flecha_izquierda1, cv2.IMREAD_GRAYSCALE)
        flecha_derecha = cv2.imread(ruta_imagen_flecha_derecha1, cv2.IMREAD_GRAYSCALE)

        # Lista de direcciones y sus respectivas imágenes
        direcciones = {
            "Dirigete hacia el Sur,": flecha_abajo,
            "Dirigete hacia el Norte,": flecha_arriba,
            "Dirigete hacia el Oeste,": flecha_izquierda,
            "Dirigete hacia el Este,": flecha_derecha
        }

        # Inicializar las variables para almacenar la mejor coincidencia
        mejor_direccion = None
        mejor_valor = -1

        # Realizar coincidencia de plantillas con cada flecha
        for direccion, plantilla in direcciones.items():
            plantilla = self.resize_image_if_needed(imagen, plantilla)  # Redimensionar si es necesario
            resultado = cv2.matchTemplate(imagen, plantilla, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(resultado)

            # Si esta coincidencia es mejor que las anteriores, la guardamos
            if max_val > mejor_valor:
                mejor_valor = max_val
                mejor_direccion = direccion

        print(mejor_direccion)
        return mejor_direccion

    def verificacionPistas(self):
        #recorte_verificacion_pistas(ruta_imagen_captura)
        #time.sleep(1)
        #cantidad_pistas(ruta_imagen_recortada)
        #self.cantidadPistas = cantidad_pistas(ruta_imagen_recortada)
        # Realizar acciones según la cantidad de símbolos "?"
        #self.checkPistas()
        cantPistasTexto = self.cantidadPistas['text']
        #self.cantidadPistas = int(cantPistasTexto)

        if cantPistasTexto == "0":
            print("Cero '?'")

            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)
        if cantPistasTexto == "1":
            print("Uno '?'")

            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            self.pista(texto_hasta_coma)

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_2)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "2":
            print("Dos '?'")
            
            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            self.pista(texto_hasta_coma)

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_2)
            self.pista(texto_hasta_coma)

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_3)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "3":
            print("Tres '?'")

            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            self.pista(texto_hasta_coma)

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_2)
            self.pista(texto_hasta_coma)

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_3)
            self.pista(texto_hasta_coma)

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_4)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == '4':
            print("Cuatro '?'")

            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            self.pista(texto_hasta_coma)
            

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_2)
            self.pista(texto_hasta_coma)

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_3)
            self.pista(texto_hasta_coma)

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_4)
            self.pista(texto_hasta_coma)

            print("Pista5")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_5)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "5":
            print("Cinco '?'")

            print("Pista1")
            #obtiene coord de salida
            self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
            #escribe coord de salida en navegador
            #cordenadas()
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            #recorta flecha de primera pista
            #recorte_primerapista_flecha(ruta_imagen_captura)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_1)
            time.sleep(0.5)
            #obtiene la direccion segun la flecha
            #texto_hasta_coma = self.obtenerDireccion(self.area_arriba, self.area_pistaDL_1) #comparacion_flechas()
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            # obtiene recorte de pista
            #recorte_primerapista(ruta_imagen_captura)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            #obtiene texto de pista de recorte
            #OCR(ruta_imagen_recortada)
            #mueve el personaje según la pista obtenida
            self.pista(texto_hasta_coma)

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_2)
            self.pista(texto_hasta_coma)

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_3)
            self.pista(texto_hasta_coma)

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_4)
            self.pista(texto_hasta_coma)

            print("Pista5")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_5)
            self.pista(texto_hasta_coma)

            print("Pista6")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(ruta_imagen_captura, self.area_flecha_6)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_6)
            self.pista(texto_hasta_coma)
            etapa_finalizada(ruta_imagen_etapa_finalizada)    

    def irACofreTesoros(self):
        self.clickEnImagen(ruta_imagen_merkasako)
        self.clickEnImagen(ruta_imagen_zaap_merka)
        self.clickEnImagen(ruta_imagen_buscar_zaap)
        ##escribir coord
        pyautogui.write('Campos de Cania')
        self.clickEnImagen(ruta_imagen_teleport_btn)
        time.sleep(2)
        self.clickEnImagen(ruta_imagen_chat_box)
        pyautogui.write('/travel -25 -36')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        self.clickEnImagen(ruta_imagen_entreda_cofre)
        pyautogui.click()
        self.clickEnImagen(ruta_imagen_mover2)
        self.clickEnImagen(ruta_imagen_chat_box)
        pyautogui.write('/clear')
        time.sleep(0.5)
        pyautogui.press('enter')

    def travel(self):
        #buscar_y_clickear_dofus(ruta_imagen_dofus)
        #pyautogui.press('w')
        #chatBox(ruta_imagen_chat_box)
        chatX, chatY = self.get4CoordFromText(self.chat['text'])
        #self.clickEnImagen(ruta_imagen_chat_box)
        pyautogui.tripleClick(chatX, chatY)
        time.sleep(2)
        text_coordactual = pyperclip.paste()
        if '/travel 22 -27' in text_coordactual:
            pyautogui.write('/travel 23, -27')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            self.clickEnImagen(ruta_imagen_llegado_destino)
            pyautogui.tripleClick(chatX, chatY)
            pyautogui.write('/travel 22, -27')
        if '/travel 21 -37' in text_coordactual:
            pyautogui.write('/travel 20, -37')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            self.clickEnImagen(ruta_imagen_llegado_destino)
            pyautogui.tripleClick(chatX, chatY)
            pyautogui.write('/travel 21, -37')
        else:
            pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        self.ha_llegado_destino(ruta_imagen_llegado_destino)

    def eliminar_chat(self):
        #pyautogui.press('w')
        chatBox(ruta_imagen_chat_box)
        pyautogui.write('/clear')
        pyautogui.press('enter')
        time.sleep(0.5)

    def banderita(self, ruta_imagen):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        # Carga la imagen de referencia y la captura de pantalla
        imagen_referencia = cv2.imread(ruta_imagen)
        captura_pantalla = pyautogui.screenshot()
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

        # Obtén las dimensiones de la imagen de referencia
        altura, ancho, _ = imagen_referencia.shape

        # Encuentra la posición de la imagen de referencia en la captura de pantalla
        resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        # Define un umbral de confianza (puedes ajustar según tus necesidades)
        umbral_confianza = 0.8

        if max_val >= umbral_confianza:
            # Obtiene las coordenadas del centro de la imagen de referencia
            centro_x = max_loc[0] + ancho // 2
            centro_y = max_loc[1] + altura // 2

            # Haz clic en el centro de la imagen encontrada
            pyautogui.tripleClick(centro_x, centro_y)
            time.sleep(0.5)
            self.eliminar_chat()
            time.sleep(0.5)
            imagen = pyautogui.screenshot()
            imagen.save(ruta_imagen_captura)
            time.sleep(1)

        else:
            self.banderita(ruta_imagen_banderita)

    def ha_llegado_destino(self, ruta_imagen):
        global intentos_realizados

        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1

        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return

        imagen_referencia = cv2.imread(ruta_imagen)
        captura_pantalla = pyautogui.screenshot()
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

        altura, ancho, _ = imagen_referencia.shape
        resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        umbral_confianza = 0.8

        if max_val >= umbral_confianza:
            # banderita(ruta_imagen_banderita)
            self.banderita(ruta_imagen_banderita)
            

        else:
            # Agregar una pausa entre intentos para reducir la carga de CPU
            time.sleep(1)
            self.ha_llegado_destino(ruta_imagen_llegado_destino)  # Llamada recursiva

    def pista(self, texto_hasta_coma):
        texto_hasta_coma = texto_hasta_coma
        texto = self.OCR(ruta_imagen_recortada)
        #texto = re.findall(r'[a-zA-Z ]', texto)
        #texto = ''.join(texto)
        print(texto)
        time.sleep(0.5)
        #print(texto)
        #print(texto_hasta_coma)
        if "Perforatroz" in texto:
            #buscar_y_clickear_dofus(ruta_imagen_dofus)
            self.clickEnImagen(ruta_imagen_minBusqueda)
            #self.checkGameCoord()
            time.sleep(2)
            comienzo_perfo_actual = self.coordActual['text']
            self.condicion_perforatroz(texto_hasta_coma, comienzo_perfo_actual)
        else:
            #pyautogui.tripleClick(755, 727)
            self.hintBox(ruta_imagen_hint_box)
            for char in texto:
                if char == 'ñ':
                    pyautogui.write('n')
                else:
                    pyautogui.write(char)
            time.sleep(1)
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(1)
            #pyautogui.tripleClick(657, 766)
            self.travel()

    def cerrar_ventana(self, event=None):
        """Función para cerrar la ventana al presionar Esc"""
        self.area_selector_window.destroy()

    def mostrar_area(self, fn, area):
        # Coordenadas del área (ejemplo)
        #coords = game_coords
        
        # Crea una ventana flotante transparente para la selección de área
        self.area_selector_window = Toplevel(self.mainwindow)
        self.area_selector_window.attributes('-alpha', 0.3)  # Nivel de transparencia
        self.area_selector_window.attributes('-topmost', True)  # Mantener siempre arriba
        self.area_selector_window.overrideredirect(True)  # Sin bordes
        self.area_selector_window.bind("<Escape>", self.cerrar_ventana)

        # Establece la ventana para que cubra toda la pantalla
        screen_width, screen_height = pyautogui.size()
        self.area_selector_window.geometry(f"{screen_width}x{screen_height}+0+0")

        # Crear un canvas donde se dibujará el área
        self.canvas = Canvas(self.area_selector_window, cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Dibujar el rectángulo basado en las coordenadas de game_coords
        x1, y1, x2, y2 = self.area_pistas
        self.rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline='red', width=2)

        # Mantener la ventana visible hasta que el usuario la cierre
        self.area_selector_window.update()
        #self.checkSalida()
        fn()
        self.cerrar_ventana()

    def buscar_y_clickear_200(self, ruta_imagen):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        # Carga la imagen de referencia y la captura de pantalla
        imagen_referencia = cv2.imread(ruta_imagen)
        captura_pantalla = pyautogui.screenshot()
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

        # Obtén las dimensiones de la imagen de referencia
        altura, ancho, _ = imagen_referencia.shape

        # Encuentra la posición de la imagen de referencia en la captura de pantalla
        resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        # Define un umbral de confianza (puedes ajustar según tus necesidades)
        umbral_confianza = 0.8

        if max_val >= umbral_confianza:
            # Obtiene las coordenadas del centro de la imagen de referencia
            centro_x = max_loc[0] + ancho // 2
            centro_y = max_loc[1] + altura // 2

            # Haz clic en el centro de la imagen encontrada
            pyautogui.tripleClick(centro_x, centro_y)
            time.sleep(5)
            self.etapa_iniciada = True
            self.save_to_text_file()
        else:
            self.buscar_y_clickear_200(ruta_imagen_200)

    def hintBox(self, ruta_imagen):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1
        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return
        # Carga la imagen de referencia y la captura de pantalla
        imagen_referencia = cv2.imread(ruta_imagen)
        imagen_referencia2 = cv2.imread(ruta_imagen_validar)
        captura_pantalla = pyautogui.screenshot()
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)
        # Obtén las dimensiones de la imagen de referencia
        altura, ancho, _ = imagen_referencia.shape
        altura2, ancho2, _ = imagen_referencia2.shape
        # Encuentra la posición de la imagen de referencia en la captura de pantalla
        resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
        resultado2 = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(resultado2)
        # Define un umbral de confianza (puedes ajustar según tus necesidades)
        umbral_confianza = 0.8
        if max_val >= umbral_confianza or max_val2 >= umbral_confianza:
            if max_val >= umbral_confianza:
                # Obtiene las coordenadas del centro de la imagen de referencia
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2
                # Haz clic en el centro de la imagen encontrada
                pyautogui.click(centro_x, centro_y)
                time.sleep(1)
            if max_val2 >= umbral_confianza:
                # Obtiene las coordenadas del centro de la imagen de referencia
                #click en nav 2
                cnac2_x = max_loc2[0] + ancho2// 2
                nav2_y = max_loc2[1] + altura2 // 2
                # Haz clic en el centro de la imagen encontrada
                #pyautogui.click(cnac2_x, nav2_y)
                time.sleep(1)
                self.clickEnImagen(ruta_imagen_navegador2)
                time.sleep(1)
                #self.checkSalida()
                inicio = self.salida['text']
                self.coordEnNav(inicio)
                time.sleep(1)
                self.hintBox(ruta_imagen)
        else:
            self.hintBox(ruta_imagen)


    # start/stop th
    def starTask(self):
        self.status_label.config(text=f"Iniciando búsqueda")
        
        ##obtener busqueda
        if (self.etapa_iniciada == False):
            self.irACofreTesoros()
            time.sleep(5)
            #print(f"Valor: {etapa_actual}, Tipo: {type(etapa_actual)}")
            print('obtener busqueda')
            buscar_y_clickear_tesoro(ruta_imagen_tesoro)
            levelSeleccionado = self.cboxHuntlvl.get()
            if levelSeleccionado:
                valor_guardado = levelSeleccionado
                print(f"Level de treasure hunt seleccionado: {valor_guardado}")
                if valor_guardado == "140":
                    self.buscar_y_clickear_200(ruta_imagen_140)
                if valor_guardado == "160":
                    self.buscar_y_clickear_200(ruta_imagen_160)
                if valor_guardado == "180":
                    self.buscar_y_clickear_200(ruta_imagen_180)
                if valor_guardado == "200":
                    self.buscar_y_clickear_200(ruta_imagen_200)
            else:
                print("No hay selección")
            
            buscar_y_clickear_salir(ruta_imagen_salir)
            buscar_y_clickear_salir_puerta(ruta_imagen_salir_puerta)
            
        self.capturaPantalla()
        print('captura realizada')

        try:
            self.checkPistas()
            self.checkEtapa()
            self.checkGameCoord()
            self.checkSalida()
            etapa_actual_texto = self.etapaActual['text']
            etapa_actual_texto = self.cleanText(etapa_actual_texto)
            primer_numero, segundo_numero = etapa_actual_texto.split(',')
            primer_numero = int(primer_numero)
            segundo_numero = int(segundo_numero)

            salida_actual_texto = self.salida['text']
            print(salida_actual_texto)
            salida_actual_texto = self.cleanText(salida_actual_texto)
            primer_coord, segundo_coord = salida_actual_texto.split(',')
            primer_coord = int(primer_coord)
            segundo_coord = int(segundo_coord)

            

            print(f"coordenada salida: {primer_coord}, {segundo_coord}")
            print(f"etapa actual: {primer_numero}, {segundo_numero}")
            print(f"numero de pista: {self.numero_pista}")

            if (primer_numero == 1 and self.numero_pista == 0):
                coordenada_cercana, nombre_cercano = coordenada_mas_cercana(primer_coord, segundo_coord, coordenadas_zaap)
                print(f"El zaap más cercano a la Salida es: {nombre_cercano}, {coordenada_cercana}")

                ##ir a coordenadas más cercanas
                ##entrar al merkasako, buscar el teleport mas cercano e ir
                #self.clickEnImagen(ruta_imagen_merkasako)
                #self.clickEnImagen(ruta_imagen_zaap_merka)
                #self.clickEnImagen(ruta_imagen_buscar_zaap)
                merkaX, merkaY = self.get4CoordFromText(self.btnMerkasako['text'])
                zaapMerkaX, zaapMerkaY = self.get4CoordFromText(self.zaapMerkasako['text'])
                buscarZaapX, buscarZaapY = self.get4CoordFromText(self.buscarZaap['text'])
                teleport_zaapX, teleport_zaapY = self.get4CoordFromText(self.teleportMerka['text'])
                pyautogui.click(merkaX, merkaY)
                time.sleep(3)
                pyautogui.click(zaapMerkaX, zaapMerkaY)
                time.sleep(2)
                pyautogui.click(buscarZaapX, buscarZaapY)
                time.sleep(2)
                ##escribir coord
                pyautogui.write(nombre_cercano)
                time.sleep(2)
                pyautogui.click(teleport_zaapX, teleport_zaapY)
                #self.clickEnImagen(ruta_imagen_teleport_btn)
                time.sleep(1)
                self.checkGameCoord()
                #self.coordActual.config(text=f"{game_coords}")
                #time.sleep(1)
                ##teleport a inicio de busqueda 
                print(f"Salida {self.salida['text']}")
                print(f"Coordenada actual {self.coordActual['text']}")
                if(f"{self.salida['text']}" != f"{self.coordActual['text']}"):
                    chatX, chatY = self.get4CoordFromText(self.chat['text'])
                    #self.clickEnImagen(ruta_imagen_chat_box)
                    pyautogui.click(chatX, chatY)
                    time.sleep(1)
                    pyautogui.write(f"/travel {primer_coord} {segundo_coord}")
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(0.5) 
                    pyautogui.press('enter')
                    self.clickEnImagen(ruta_imagen_llegado_destino)
                    time.sleep(1)   
                    self.eliminar_chat()
                    game_coords = (primer_coord, segundo_coord)
                    self.coordActual.config(text=f"{game_coords}")
                    self.coordActual.update_idletasks()

            while primer_numero < segundo_numero: # Mientras la condición sea verdadera
                self.checkPistas()
                self.verificacionPistas()
                primer_numero += 1  # Actualiza la condición para evitar un bucle infinito
                time.sleep(1)
            
            time.sleep(1)
            lucha(ruta_imagen_lucha)
            time.sleep(2)
            pelea()
            #time.sleep(6)
            self.etapa_iniciada = False
            self.save_to_text_file()
            time.sleep(2)
            #pyautogui.press('enter')
            pyautogui.press('enter')
            #self.clickEnImagen(ruta_imagen_cerrar_bat)
            self.status_label.config(text=f"Búsqueda terminada")
            #pyautogui.press('0')
        except ValueError as e:
            print(f"Error: {e}")

        self.starTask()

#buscar_y_clickear_dofus(ruta_imagen_dofus)
# moverse()
# moverse()
# buscar_y_clickear_puerta(ruta_imagen_puerta)
# buscar_y_clickear_moverse(ruta_imagen_moverse)
# buscar_y_clickear_tesoro(ruta_imagen_tesoro)
# buscar_y_clickear_200(ruta_imagen_160)
# buscar_y_clickear_salir(ruta_imagen_salir)
# buscar_y_clickear_salir_puerta(ruta_imagen_salir_puerta)
##comenzar_etapas()
##pelea()

#while n > 5:
#comenzar_etapas()
#time.sleep(2)
#buscar_y_clickear_tesoro(ruta_imagen_tesoro)
#buscar_y_clickear_200(ruta_imagen_160)
#buscar_y_clickear_salir(ruta_imagen_salir)
#buscar_y_clickear_salir_puerta(ruta_imagen_salir_puerta)

if __name__ == "__main__":
    #root = Tk()
    app = ImageFinderApp()
    app.run()
    #root.mainloop()

