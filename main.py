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

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"

ruta_imagen_chrome = './treasureHunt/chrome.png'
ruta_imagen_dofus = './treasureHunt/dofus.png'
ruta_imagen_puerta = './treasureHunt/puerta.png'
ruta_imagen_moverse = './treasureHunt/mover.png'
ruta_imagen_tesoro = './treasureHunt/tesoro.png'
ruta_imagen_200 = './treasureHunt/nivel200.png'
ruta_imagen_160 = './treasureHunt/nivel160.png'
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
limite_intentos = 200000000000000000000
intentos_realizados = 0

### Game data
game_coords = None
etapa_actual = None


all_portal = ["", "", "", ""]


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
        time.sleep(1)
    else:
        buscar_y_clickear_dofus(ruta_imagen_dofus)


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


def buscar_y_clickear_200(ruta_imagen):
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
    else:
        buscar_y_clickear_200(ruta_imagen_200)


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


def verificacion_etapas(ruta_imagen):
    recorte_etapas(ruta_imagen)
    texto = OCR(ruta_imagen_recortada)
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
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('F1')
    time.sleep(5)
    contador = 0
    while contador < 2:  # Mientras la condición sea verdadera
        time.sleep(5)
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('2')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('2')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        pyautogui.press('F1')  # Haz algo
        contador += 1  # Actualiza la condición para evitar un bucle infinito


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


def OCR(ruta_imagen):
    # Configura la ruta al ejecutable de Tesseract (puede variar según tu instalación)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jpvas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    imagen = cv2.imread(ruta_imagen)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Realizar OCR en la región recortada
    texto = pytesseract.image_to_string(gray)

    print(texto)

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

    
    print("texto en OCR ")
    print(texto)

    if "Afiche" in texto:
        texto = texto
        return texto
    elif "Champifién" in texto:
        texto = texto.replace("Champifién", "Champinon")
        return texto
    elif "vinturén" in texto:
        texto = texto.replace("vinturén", "Cinturon")
        return texto
    elif ")jo de fab'huritu pintado" in texto:
        texto = texto.replace(")jo", "Ojo")
        return texto
    elif "Seeneaidadvaadan" in texto:
        texto = texto.replace("Seeneaidadvaadan", "Craneo de tymador")
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
    elif "fi" in texto:
        if "firefux" in texto:
            texto = texto
        else:
            texto = texto.replace("fi", "n")
        return texto
    else:
        return texto


def manipulacion_cordenada():
    texto = OCR(ruta_imagen_recortada)
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
    print(texto)
    texto = texto.replace(")", "")
    texto = texto.replace("=", "-")
    texto = texto.replace("Salida", "")
    texto = texto.replace("o", "6")
    # Dividir la cadena por la coma
    numeros = texto.split(',')
    # Obtener los valores
    primera_coordenada = str(numeros[0])
    segunda_coordenada = str(numeros[1])

    return primera_coordenada, segunda_coordenada


def cordenadas():
    #buscar_y_clickear_chrome(ruta_imagen_chrome)
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


def condicion_perforatroz(texto_hasta_coma):
    texto_hasta_coma = texto_hasta_coma
    if texto_hasta_coma == "Dirigete hacia el Sur,":
        # funcion para moverse abajo
        time.sleep(2)
        pyautogui.tripleClick(721, 899)
        time.sleep(5)
        buscar_y_clickear_perforatroz(texto_hasta_coma)
    elif texto_hasta_coma == "Dirigete hacia el Norte,":
        # funcion para moverse arriba
        time.sleep(2)
        pyautogui.tripleClick(945, 33)
        time.sleep(5)
        buscar_y_clickear_perforatroz(texto_hasta_coma)

    elif texto_hasta_coma == "Dirigete hacia el Oeste,":
        # funcion para moverse izquierda
        time.sleep(2)
        pyautogui.tripleClick(82, 428)
        time.sleep(5)
        buscar_y_clickear_perforatroz(texto_hasta_coma)
    elif texto_hasta_coma == "Dirigete hacia el Este,":
        # funcion para moverse derecha
        time.sleep(2)
        pyautogui.tripleClick(1619, 646)
        time.sleep(5)
        buscar_y_clickear_perforatroz(texto_hasta_coma)


def pista(texto_hasta_coma):
    texto_hasta_coma = texto_hasta_coma
    texto = OCR(ruta_imagen_recortada)
    time.sleep(0.5)
    print(texto)
    print(texto_hasta_coma)
    if "Perforatroz" in texto:
        buscar_y_clickear_dofus(ruta_imagen_dofus)
        condicion_perforatroz(texto_hasta_coma)
    else:
        #pyautogui.tripleClick(755, 727)
        hintBox(ruta_imagen_hint_box)
        for char in texto:
            if char == 'ñ':
                pyautogui.write('n')
            else:
                pyautogui.write(char)
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.tripleClick(657, 766)
        time.sleep(0.5)
        travel()


def buscar_y_clickear_perforatroz(texto_hasta_coma):
    global intentos_realizados
    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1
    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return
    # Lista de rutas alternativas de imágenes
    rutas_alternativas = ["perforatroz.png", 'perforatroz2.png', 'perforatroz3.png', 'perforatroz4.png',
                          'perforatroz5.png', 'perforatroz6.png', 'perforatroz7.png', 'perforatroz8.png',
                          'perforatroz9.png']

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
                banderita('banderita_final.png')
                time.sleep(0.5)
                recorte_cordenada_juego(ruta_imagen_captura)
                time.sleep(0.5)
                cordenadas_juegos()
                return  # Termina el bucle ya que se encontró y clickeó una imagen
                
    condicion_perforatroz(texto_hasta_coma)



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


def navegacion_flechas(ruta_imagen):
    global intentos_realizados
    buscar_y_clickear_chrome(ruta_imagen_chrome)
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


def travel():
    buscar_y_clickear_dofus(ruta_imagen_dofus)
    #pyautogui.press('w')
    chatBox(ruta_imagen_chat_box)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    ha_llegado_destino(ruta_imagen_llegado_destino)


def eliminar_chat():
    #pyautogui.press('w')
    chatBox(ruta_imagen_chat_box)
    pyautogui.write('/clear')
    pyautogui.press('enter')
    time.sleep(0.5)


def banderita(ruta_imagen):
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
        eliminar_chat()
        time.sleep(0.5)
        imagen = pyautogui.screenshot()
        imagen.save('captura.png')
        time.sleep(1)

    else:
        banderita(ruta_imagen_banderita)


def ha_llegado_destino(ruta_imagen):
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
        banderita('banderita_final.png')

    else:
        # Agregar una pausa entre intentos para reducir la carga de CPU
        time.sleep(1)
        ha_llegado_destino(ruta_imagen_llegado_destino)  # Llamada recursiva


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
    # Capturar la pantalla
    captura_pantalla = cv2.imread(ruta_imagen)
    captura_pantalla = np.array(captura_pantalla)
    #captura_pantalla = cv2.cvtColor(captura_pantalla, cv2.COLOR_RGB2BGR)

    # Cargar la imagen de referencia
    referencia = cv2.imread(ruta_imagen_interrogacion)

    # Buscar la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(captura_pantalla, referencia, cv2.TM_CCOEFF_NORMED)

    # Definir un umbral de confianza
    umbral_confianza = 0.8
    ubicaciones = np.where(resultado >= umbral_confianza)

    # Contar las ocurrencias encontradas
    cantidad_ocurrencias = len(list(zip(*ubicaciones[::-1])))
    return cantidad_ocurrencias


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
        etapa_finalizada('etapa_finalizada.png')


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
        etapa_finalizada('lucha.png')

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

def hintBox(ruta_imagen):
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
        hintBox(ruta_imagen)

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

        # Obtener el Label definido en Pygubu
        self.status_label = self.builder.get_object('lblWInfo')
        self.coordActual = self.builder.get_object('lblCoordActual')
        self.etapaActual = self.builder.get_object('lblEtapaActual')
        self.cantidadPistas = self.builder.get_object('lblPistas')
        self.salida = self.builder.get_object('lblSalida')
        self.pista1 = self.builder.get_object('lblPista1')
        self.pista2 = self.builder.get_object('lblPista2')
        self.pista3 = self.builder.get_object('lblPista3')
        self.pista4 = self.builder.get_object('lblPista4')
        self.pista5 = self.builder.get_object('lblPista5')

        self.image_offset = 25
        self.image_path = None
        self.running = False
        self.search_area = None

        # Config data
        ## areas
        self.area_game_coord = None
        self.area_etapa_actual = None
        self.area_salida = None
        self.area_pistas = None

        ## pistas areas
        self.area_pista_1 = None
        self.area_pista_2 = None
        self.area_pista_3 = None
        self.area_pista_4 = None
        self.area_pista_5 = None 

        ## bot data

    def run(self):
        self.mainwindow.mainloop()
        
        # self.label = Label(root, text="Select an image to search for:")
        # self.label.pack()

        # self.image_listbox = Listbox(root, height=10)
        # self.image_listbox.pack()

        # scrollbar = Scrollbar(root)
        # scrollbar.pack(side="right", fill="y")

        # self.image_listbox.config(yscrollcommand=scrollbar.set)
        # scrollbar.config(command=self.image_listbox.yview)

        # self.load_images()

        # self.select_area_button = Button(root, text="Select Search Area", command=self.select_area)
        # self.select_area_button.pack()

        # self.check_button = Button(root, text="Check values", command=self.checkGameCoord)
        # self.check_button.pack()

        # self.start_button = Button(root, text="Start Searching", command=self.start_search)
        # self.start_button.pack()

        # self.stop_button = Button(root, text="Stop Searching", command=self.stop_search)
        # self.stop_button.pack()

        # self.status_label = Label(root, text="Status: Waiting to start")
        # self.status_label.pack()

    def load_images(self):
        image_folder = "./resources"
        images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        for image in images:
            self.image_listbox.insert("end", image)

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


    def start_search(self):
        if self.image_listbox.curselection():
            self.image_path = os.path.join("./resources", self.image_listbox.get(self.image_listbox.curselection()))
            self.running = True
            self.status_label.config(text="Status: Searching for image...")
            self.search_thread = threading.Thread(target=self.check_image)
            self.search_thread.start()
        else:
            self.status_label.config(text="Status: Please select an image first")

    def stop_search(self):
        self.running = False
        self.status_label.config(text="Status: Stopped searching")

    def check_image(self):
        while self.running:
            try:
                pos = pyautogui.locateOnScreen(self.image_path, region=self.search_area, confidence=0.8) if self.search_area else pg.locateOnScreen(self.image_path, confidence=0.8)
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

    # Chequeo de datos

    def checkGameCoord(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_game_coord)
        c1, c2 = manipulacion_cordenada_juego()
        game_coords = (c1, c2)
        self.status_label.config(text=f"Coordenadas guardadas {c1, c2}")
        self.coordActual.config(text=f"{game_coords}")
    
    def checkEtapa(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_etapa_actual)
        primer_numero, segundo_numero = verificacion_etapas(ruta_imagen_captura)
        etapa_actual = (primer_numero, segundo_numero)
        self.status_label.config(text=f"Etapa guardada {primer_numero, segundo_numero}")
        self.etapaActual.config(text=f"{etapa_actual}")

    def checkPistas(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_pistas)
        cantidad = cantidad_pistas(ruta_imagen_recortada)
        self.status_label.config(text=f"Pistas encontradas: {cantidad}")
        self.cantidadPistas.config(text=f"{cantidad}")

    def checkSalida(self):
        self.recorte_Imagen(ruta_imagen_captura, self.area_salida)
        c1, c2 = manipulacion_cordenada()
        self.salida.config(text=f"{c1, c2}")
    #otros

    def recorte_Imagen(self, ruta_imagen, coords):
        imagen = pyautogui.screenshot()
        imagen.save('./treasureHunt/captura.png')
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
        cv2.imwrite('./treasureHunt/captura_recorte.png', recorte)

    def cleanText(self, text):
        texto = text
        texto = texto.replace('(', '')
        texto = texto.replace(')', '')
        texto = texto.replace("'", "") 
        return texto

    #save/load

    def save_to_text_file(self):
        with open('variables.txt', 'w') as file:
            file.write(f"area_game_coord: {self.area_game_coord}\n")
            file.write(f"area_etapa_actual: {self.area_etapa_actual}\n")
            file.write(f"area_salida: {self.area_salida}\n")
            file.write(f"area_pistas: {self.area_pistas}\n")
            file.write(f"area_pista1: {self.area_pista_1}\n")
        
        self.status_label.config(text=f"Datos guardados")

    def load_from_text_file(self):
        with open('variables.txt', 'r') as file:
            lines = file.readlines()
            # search_area = eval(lines[0].split(': ')[1].strip())
            self.area_game_coord = eval(lines[0].split(': ')[1].strip())
            self.checkGameCoord()

            # other_variable = lines[1].split(': ')[1].strip()
            self.area_etapa_actual = eval(lines[1].split(': ')[1].strip())
            self.checkEtapa()
            # return search_area #, other_variable

            self.area_salida = eval(lines[2].split(': ')[1].strip())
            self.checkSalida()

            self.area_pistas = eval(lines[3].split(': ')[1].strip())
            self.checkPistas()

            self.area_pistas = eval(lines[4].split(': ')[1].strip())
        
        self.status_label.config(text=f"Datos cargados")

    def verificacionPistas(self):
        self.checkPistas()
        #recorte_verificacion_pistas(ruta_imagen_captura)
        #time.sleep(1)
        #cantidad_pistas(ruta_imagen_recortada)
        #self.cantidadPistas = cantidad_pistas(ruta_imagen_recortada)
        # Realizar acciones según la cantidad de símbolos "?"
        if self.cantidadPistas == 0:
            print("Cero '?'")
            print("Pista1")
            #recorta texto de pista 1
            #self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
            recorte(ruta_imagen_captura)
            #escribe cordenadas en navegador
            cordenadas()
            recorte_primerapista_flecha(ruta_imagen_captura)
            texto_hasta_coma = comparacion_flechas()
            recorte_primerapista(ruta_imagen_captura)
            OCR(ruta_imagen_recortada)
            pista(texto_hasta_coma)
            etapa_finalizada('etapa_finalizada.png')
        if self.cantidadPistas == 1:
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
        elif self.cantidadPistas == 2:
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
        elif self.cantidadPistas == 3:
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
        elif self.cantidadPistas == 4:
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
        elif self.cantidadPistas == 5:
            print("Cinco '?'")
            print("Pista1")
            self.recorte_Imagen(ruta_imagen_captura, self.area_pista_1)
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

            print("Pista6")
            recorte_sextapista_flecha(ruta_imagen_captura)
            texto_hasta_coma = comparacion_flechas_6pista()
            recorte_sextapista(ruta_imagen_captura)
            OCR(ruta_imagen_recortada)
            pista(texto_hasta_coma)
            etapa_finalizada('etapa_finalizada.png')    

    def starTask(self):
        self.status_label.config(text=f"Iniciando búsqueda")
        try:
            etapa_actual_texto = self.etapaActual['text']
            etapa_actual_texto = self.cleanText(etapa_actual_texto)
            primer_numero, segundo_numero = etapa_actual_texto.split(',')
            primer_numero = int(primer_numero)
            segundo_numero = int(segundo_numero)
            
            while primer_numero < segundo_numero:  # Mientras la condición sea verdadera
                self.verificacionPistas()
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

