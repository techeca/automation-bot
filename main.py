import time

import cv2
import numpy as np
import pyautogui
import pytesseract

ruta_imagen_chrome = 'chrome.png'
ruta_imagen_dofus = 'dofus.png'
ruta_imagen_puerta = 'puerta.png'
ruta_imagen_moverse = 'mover.png'
ruta_imagen_tesoro = 'tesoro.png'
ruta_imagen_200 = 'nivel200.png'
ruta_imagen_salir = 'salir.png'
ruta_imagen_salir_puerta = 'salir_puerta.png'
ruta_imagen_captura = 'captura.png'
ruta_imagen_recortada = 'captura_recorte.png'
ruta_imagen_flecha_abajo1 = 'flecha_abajo1.png'
ruta_imagen_flecha_abajo2 = 'flecha_abajo2.png'
ruta_imagen_flecha_arriba1 = 'flecha_arriba1.png'
ruta_imagen_flecha_arriba2 = 'flecha_arriba2.png'
ruta_imagen_flecha_izquierda1 = 'flecha_izquierda1.png'
ruta_imagen_flecha_izquierda2 = 'flecha_izquierda2.png'
ruta_imagen_flecha_derecha1 = 'flecha_derecha1.png'
ruta_imagen_flecha_derecha2 = 'flecha_derecha2.png'
ruta_imagen_llegado_destino = 'llegado_destino.png'
ruta_imagen_banderita = 'banderita.png'
ruta_imagen_perforatroz = 'perforatroz.png'
limite_intentos = 200000000000000000000
intentos_realizados = 0


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
    # Separar la información usando el método split(' ')
    separado = texto.split(' ')
    # Buscar los números en la última parte de la cadena
    numeros = separado[-1].split('/')
    # Guardar los números en variables separadas
    primer_numero = numeros[0]
    segundo_numero = numeros[1]
    return primer_numero, segundo_numero


def comenzar_etapas():
    primer_numero, segundo_numero = verificacion_etapas(ruta_imagen_captura)
    primer_numero = int(primer_numero)
    segundo_numero = int(segundo_numero)
    while primer_numero < segundo_numero:  # Mientras la condición sea verdadera
        verificacion_pistas()
        primer_numero += 1  # Actualiza la condición para evitar un bucle infinito
        time.sleep(1)
    time.sleep(1)
    lucha('lucha.png')
    time.sleep(1)


def pelea():
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(3)
    contador = 0
    while contador < 2:  # Mientras la condición sea verdadera
        time.sleep(5)
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('2')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(2)
        pyautogui.press('3')
        time.sleep(1)
        buscar_y_clickear_monstruo('monstruo.png')
        time.sleep(3)
        pyautogui.press('space')  # Haz algo
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
    x1, y1, x2, y2 = 60, 653, 172, 672  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)


def recorte_cordenada_juego(ruta_imagen):
    imagen = pyautogui.screenshot()
    imagen.save('captura.png')
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 5, 70, 85, 105  # Ejemplo de coordenadas de recorte

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)


def OCR(ruta_imagen):
    # Configura la ruta al ejecutable de Tesseract (puede variar según tu instalación)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jjpor\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    imagen = cv2.imread(ruta_imagen)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Realizar OCR en la región recortada
    texto = pytesseract.image_to_string(gray)
    texto = texto.replace("\n", "")
    texto = texto.replace("6", "o")
    texto = texto.replace("‘", "'")
    texto = texto.replace("’", "'")
    texto = texto.replace("}", "")
    texto = texto.replace("]", "")
    texto = texto.replace("|", "")
    texto = texto.replace("_", "")
    texto = texto.replace(".", "")
    texto = texto.replace("eee", "")
    print(texto)
    if "Afiche" in texto:
        texto = texto
        return texto
    elif "Champifién" in texto:
        texto = texto.replace("Champifién", "Champinon")
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
    elif "Dirigete hacia el Este" in texto:
        texto = "Dirigete hacia el Este"
        return texto
    elif "Dirigete hacia el Norte" in texto:
        texto = "Dirigete hacia el Norte"
        return texto
    elif "Dirigete hacia el Oeste" in texto:
        texto = "Dirigete hacia el Oeste"
        return texto
    elif "Dirigete hacia el Sur" in texto:
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
    texto = texto.replace("o", "6")
    # Dividir la cadena por la coma
    numeros = texto.split(',')
    # Obtener los valores
    primera_coordenada = str(numeros[0])
    segunda_coordenada = str(numeros[1])

    return primera_coordenada, segunda_coordenada


def cordenadas():
    buscar_y_clickear_chrome(ruta_imagen_chrome)
    c1, c2 = manipulacion_cordenada()
    time.sleep(0.5)
    pyautogui.tripleClick(731, 360)
    time.sleep(0.5)
    pyautogui.write(c1)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.write(c2)
    time.sleep(0.5)


def cordenadas_juegos():
    buscar_y_clickear_chrome(ruta_imagen_chrome)
    c1, c2 = manipulacion_cordenada_juego()
    time.sleep(0.5)
    pyautogui.tripleClick(731, 360)
    time.sleep(0.5)
    pyautogui.write(c1)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(c2)
    time.sleep(3)
    buscar_y_clickear_dofus(ruta_imagen_dofus)


def recorte_primerapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 60, 673, 300, 700  # Ejemplo de coordenadas de recorte

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
    if "Perforatroz" in texto:
        buscar_y_clickear_dofus(ruta_imagen_dofus)
        condicion_perforatroz(texto_hasta_coma)
    else:
        pyautogui.tripleClick(755, 727)
        for char in texto:
            if char == 'ñ':
                pyautogui.write('n')
            else:
                pyautogui.write(char)
        time.sleep(0.5)
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
                          'perforatroz5.png']

    for ruta_alternativa in rutas_alternativas:
        imagen_referencia = cv2.imread(ruta_alternativa)
        if imagen_referencia is not None:
            # Capturar la pantalla
            x1, y1, x2, y2 = 330, 50, 1580, 900
            captura_pantalla = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
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
    x1, y1, x2, y2 = 30, 750, 215, 800  # Ejemplo de coordenadas de recorte

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
    pyautogui.press('w')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    ha_llegado_destino(ruta_imagen_llegado_destino)


def eliminar_chat():
    pyautogui.press('w')
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
    x1, y1, x2, y2 = 60, 700, 298, 730  # Ejemplo de coordenadas de recorte

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
    x1, y1, x2, y2 = 60, 727, 298, 760  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)


def recorte_cuartapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 60, 754, 298, 783  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)


def recorte_quintapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 60, 780, 298, 813  # Ejemplo de coordenadas de recorte   y1=27, y2=30

    # Recortar la región de interés
    recorte = imagen[y1:y2, x1:x2]

    # Guardar el recorte en un archivo (opcional)
    cv2.imwrite('captura_recorte.png', recorte)


def recorte_sextapista(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    # Definir las coordenadas del recorte (x1, y1, x2, y2)
    x1, y1, x2, y2 = 60, 820, 298, 850  # Ejemplo de coordenadas de recorte   y1=27, y2=30

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
    captura_pantalla = cv2.cvtColor(captura_pantalla, cv2.COLOR_RGB2BGR)

    # Cargar la imagen de referencia
    referencia = cv2.imread('interrogacion.png')

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


buscar_y_clickear_dofus(ruta_imagen_dofus)
# moverse()
# moverse()
# buscar_y_clickear_puerta(ruta_imagen_puerta)
# buscar_y_clickear_moverse(ruta_imagen_moverse)
# buscar_y_clickear_tesoro(ruta_imagen_tesoro)
# buscar_y_clickear_200(ruta_imagen_200)
# buscar_y_clickear_salir(ruta_imagen_salir)
# buscar_y_clickear_salir_puerta(ruta_imagen_salir_puerta)
comenzar_etapas()
pelea()




