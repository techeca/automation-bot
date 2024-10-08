import time

import cv2
import numpy as np
import pyautogui
import pytesseract

import os
import threading
from tkinter import ttk, Tk, Button, Label, Listbox, Scrollbar, Toplevel, Canvas, BooleanVar
import pathlib
import pygubu
import re
import math
import pyperclip
import gc
from specWords import REEMPLAZOS
from zaap import COORDENADAS_ZAAP

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
ruta_imagen_banderita_brillante = './treasureHunt/banderita_brillante.png'
ruta_imagen_subirLvl = './treasureHunt/lvlok.png'
ruta_imagen_cerrar_busqueda = './treasureHunt/cerrar_busqueda.png'

# rutas recursos
ruta_imagen_recurso_trigo = './resources/Trigo.png'
ruta_imagen_recurso_hierro = './resources/hierro'

# rutas battle
ruta_imagen_rojo = './treasureHunt/battle/rojo.png'
ruta_imagen_moob = './treasureHunt/battle/mob'

limite_intentos = 200000000000000000000
intentos_realizados = 0

# Game data (eliminar?)
game_coords = None
etapa_actual = None
salida_actual = None
pistas_actual = None
comienzo_perfo_actual = None
inBattle = False


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
        # print(f"Calculando distancia de ({x}, {y}) a ({coord_x}, {coord_y}): {distancia:.2f} - {nombre}")

        if distancia < distancia_minima:
            distancia_minima = distancia
            coordenada_mas_cercana = (coord_x, coord_y)
            nombre_mas_cercano = nombre

        if x == -55 and y == -64:
            coordenada_mas_cercana = (-78, -41)
            nombre_mas_cercano = "Burgo"

    print(
        f"La coordenada más cercana es: {coordenada_mas_cercana} - {nombre_mas_cercano} con una distancia de {distancia_minima:.2f}")
    return coordenada_mas_cercana, nombre_mas_cercano

def chatBox(ruta_imagen):
    global intentos_realizados

    # Carga la imagen de referencia y verifica si se cargó correctamente
    imagen_referencia = cv2.imread(ruta_imagen)
    if imagen_referencia is None:
        print(f"Error: No se pudo cargar la imagen de la ruta: {ruta_imagen}")
        return

    # Se hace un seguimiento de los intentos realizados
    intentos_realizados += 1

    # Límite de intentos alcanzado
    if intentos_realizados > limite_intentos:
        print("Límite de intentos alcanzado. La imagen no se encontró.")
        return

    # Captura la pantalla actual
    captura_pantalla = pyautogui.screenshot()
    captura_pantalla_np = np.array(captura_pantalla)
    captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

    # Obtén las dimensiones de la imagen de referencia
    altura, ancho, _ = imagen_referencia.shape

    # Encuentra la posición de la imagen de referencia en la captura de pantalla
    resultado = cv2.matchTemplate(
        captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Define un umbral de confianza (puedes ajustar según tus necesidades)
    umbral_confianza = 0.8

    if max_val >= umbral_confianza:
        # Obtiene las coordenadas del centro de la imagen de referencia
        centro_x = max_loc[0] + ancho // 2
        centro_y = max_loc[1] + altura // 2

        # Haz clic en el centro de la imagen encontrada
        print(
            f"Imagen encontrada con {max_val:.2f} de confianza, haciendo clic en ({centro_x}, {centro_y})")
        pyautogui.click(centro_x, centro_y)
        time.sleep(1)
    else:
        # Espera un poco antes de volver a intentar
        time.sleep(0.5)
        print(
            f"No se encontró la imagen, reintentando... Intento {intentos_realizados}")
        # Reintenta la búsqueda sin usar una recursividad infinita
        chatBox(ruta_imagen)

class ImageFinderApp:
    def __init__(self, master=None):
        # self.root = root
        # self.root.title("TH Automation")
        # self.root.geometry("400x400")
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
        # self.levelHunt = self.builder.get_object('levelHunt')

        self.reloadNav = self.builder.get_object('lblReload')
        self.navX = self.builder.get_object('lblX')
        self.navY = self.builder.get_object('lblY')
        self.navHint = self.builder.get_object('lblHint')

        self.cboxHuntlvl = self.builder.get_object('cboxHuntlvl')
        self.pistaDL6 = self.builder.get_object('lblPistaDL6')

        self.buscarPerforatroz = self.builder.get_object('checkPerforatroz')
        self.buscar_var = BooleanVar()

        # Para resources
        self.image_offset = 25
        self.image_path = None
        self.running = False
        self.search_area = None

        # Config data
        # areas
        self.area_game_coord = None
        self.area_etapa_actual = None
        self.area_salida = None
        self.area_pistas = None  # cantidad símbolos de '?'
        self.area_chat = None

        # pistas - areas
        self.area_pista_1 = None 
        self.area_pista_2 = None 
        self.area_pista_3 = None 
        self.area_pista_4 = None
        self.area_pista_5 = None
        self.area_pista_6 = None

        # direccion - areas (clic arriba, abajo, izq, der)
        self.area_arriba = None
        self.area_abajo = None
        self.area_izquierda = None
        self.area_derecha = None
        self.etapa_iniciada = False
        self.area_pistaD_6 = None

        # flechas - areas
        self.area_flecha_1 = None
        self.area_flecha_2 = None
        self.area_flecha_3 = None
        self.area_flecha_4 = None
        self.area_flecha_5 = None
        self.area_flecha_6 = None

        # bot data
        self.mapas_avanzados = 0
        self.numero_pista = 0
        self.navegador_actual = ''
        self.inicio_proceso = False
        self.reset = False
        self.direccionActual = None

        self.load_from_text_file()

    def run(self):
        self.mainwindow.mainloop()

    # seleccion de area y obtención de area
    def select_area(self):
        # self.root.withdraw()
        self.mainwindow.withdraw()
        self.area_selector_window = Toplevel(self.mainwindow)
        self.area_selector_window.title("Select Area")
        self.area_selector_window.attributes(
            '-alpha', 0.3)  # Set transparency level
        self.area_selector_window.attributes(
            '-topmost', True)  # Ensure it's on top
        self.area_selector_window.overrideredirect(
            True)  # Remove window borders

        screen_width, screen_height = pyautogui.size()
        self.area_selector_window.geometry(
            f"{screen_width}x{screen_height}+0+0")

        self.canvas = Canvas(self.area_selector_window,
                             cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # self.root.wait_window(self.area_selector_window)
        # self.root.deiconify()
        self.mainwindow.wait_window(self.area_selector_window)
        self.mainwindow.deiconify()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x,
                           self.start_y, event.x, event.y)

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
        self.status_label.config(
            text=f"Status: Area selected {self.search_area}")

    def mostrar_area(self, fn, area):
        # Coordenadas del área (ejemplo)
        # coords = game_coords

        # Crea una ventana flotante transparente para la selección de área
        self.area_selector_window = Toplevel(self.mainwindow)
        self.area_selector_window.attributes(
            '-alpha', 0.3)  # Nivel de transparencia
        self.area_selector_window.attributes(
            '-topmost', True)  # Mantener siempre arriba
        self.area_selector_window.overrideredirect(True)  # Sin bordes
        self.area_selector_window.bind("<Escape>", self.cerrar_ventana)

        # Establece la ventana para que cubra toda la pantalla
        screen_width, screen_height = pyautogui.size()
        self.area_selector_window.geometry(
            f"{screen_width}x{screen_height}+0+0")

        # Crear un canvas donde se dibujará el área
        self.canvas = Canvas(self.area_selector_window,
                             cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Dibujar el rectángulo basado en las coordenadas de game_coords
        x1, y1, x2, y2 = area
        self.rect = self.canvas.create_rectangle(
            x1, y1, x2, y2, outline='red', width=2)

        # Mantener la ventana visible hasta que el usuario la cierre
        self.area_selector_window.update()
        # self.checkSalida()
        fn()
        self.cerrar_ventana()

    # busca imagen, posiciona el cursor sobre el
    def check_image(self):
        while self.running:
            try:
                pos = pyautogui.locateOnScreen(self.image_path, region=self.search_area,
                                               confidence=0.8) if self.search_area else pyautogui.locateOnScreen(self.image_path, confidence=0.8)
                if pos:
                    pyautogui.moveTo(
                        pos[0] + self.image_offset, pos[1] + self.image_offset)
                    pyautogui.click()
                    self.status_label.config(
                        text=f"Status: Found image at {pos}")
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

        resultado = cv2.matchTemplate(
            img_grande, img_fragmento, cv2.TM_CCOEFF_NORMED)

        # Definir un umbral para determinar si hay coincidencia
        umbral = 0.8
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= umbral:
            # Obtener el tamaño de la imagen buscada
            altura, ancho = img_fragmento.shape[:2]

            # Obtener la posición de la esquina superior izquierda donde se encuentra la imagen
            top_left = max_loc

            # Calcular el centro de la imagen para hacer clic
            centro_x = top_left[0] + ancho // 2
            centro_y = top_left[1] + altura // 2

            # Hacer clic en el centro de la imagen encontrada
            # pyautogui.click(centro_x, centro_y)
            print(
                f"Imagen encontrada en ({centro_x}, {centro_y}), realizando clic.")
            return True
        else:
            # print(f"No hay recurso, volviendo a buscar.")
            # self.buscar_image(ruta_imagen_a_buscar)
            return False

    # --------------------------------#
    # Funciones para configurar areas
    # --------------------------------#

    def configCoordActual(self):
        self.select_area()
        self.area_game_coord = self.search_area
        self.checkGameCoord()

    def configEtapaActual(self):
        self.capturaPantalla()
        self.select_area()
        self.area_etapa_actual = self.search_area
        self.checkEtapa()

    def configSalida(self):
        self.capturaPantalla()
        self.select_area()
        self.area_salida = self.search_area
        self.checkSalida()

    def configPistas(self):
        self.capturaPantalla()
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


    def configDireccionPista6(self):
        self.select_area()
        self.area_chat = self.search_area
        self.chat.config(text=f"{self.area_chat}")

    def configSetCoordchat(self):
        self.select_area()
        texto_coord_chat = self.search_area
        self.coordChat.config(text=f"{texto_coord_chat}")
        
    def configSetPrimeraBanderita(self):
        self.select_area()
        #configSetPrimeraBanderita
        texto = self.search_area
        self.pistaDL6.config(text=f"{texto}")
        
    def configSetMerkasako(self):
        self.select_area()
        texto = self.search_area
        self.btnMerkasako.config(text=f"{texto}")

    def configSetZaap(self):
        self.select_area()
        texto = self.search_area
        self.zaapMerkasako.config(text=f"{texto}")
        
    def configSetBuscarZaap(self):
        self.select_area()
        texto = self.search_area
        self.buscarZaap.config(text=f"{texto}")
        
    def configSetTeleport(self):
        self.select_area()
        texto = self.search_area
        self.teleportMerka.config(text=f"{texto}")

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

     # probar

    def configArea(self, container):
        self.select_area()
        texto = self.search_area
        container.config(text=f"{texto}")

    # --------------------#
    # Funcion de OCR
    # --------------------#

    def OCR(self, ruta_imagen):
        # Configura la ruta al ejecutable de Tesseract (puede variar según tu instalación)
        ruta_tesseract = self.entryPytesseract.get()
        pytesseract.pytesseract.tesseract_cmd = fr'{ruta_tesseract}\tesseract.exe'

        # Cargar la imagen y convertirla a escala de grises
        imagen = cv2.imread(ruta_imagen)
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Realizar OCR en la imagen en escala de grises
        texto = pytesseract.image_to_string(gray)

        # Limpiar el texto
        texto = texto.replace("\n", "").replace("‘", "'").replace("’", "'")
        texto = texto.replace("}", "").replace("]", "").replace("|", "")
        texto = texto.replace("_", "").replace(".", "").replace("eee", "")

        # Mapeo de reemplazos específicos

        # Realizar los reemplazos
        for k, v in REEMPLAZOS.items():
            if k in texto:
                texto = texto.replace(k, v)

        # Liberar la imagen de la memoria
        cv2.destroyAllWindows()
        del gray
        del imagen

        # Retornar el texto procesado
        return texto

    # -------------------#
    # Chequeo de datos
    # -------------------#

    def checkGameCoord(self):
        merkaX, merkaY = self.get4CoordFromText(self.btnMerkasako['text'])
        pyautogui.click(merkaX, merkaY)
        time.sleep(4)
        chatX, chatY = self.get4CoordFromText(self.chat['text'])
        pyautogui.click(chatX, chatY)
        pyautogui.write('/clear')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('/s %pos%')
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
            pyautogui.write('/s %pos%')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.tripleClick(chatCoordX, chatCoordY)
            pyautogui.hotkey('ctrl', 'c')
            ruta_actual_copy = pyperclip.paste()
        # Filtrar solo los números de la salida
        salida_actual_texto = re.findall(r'-?\d+', ruta_actual_copy)
        print(f"Coordenada actual In-Game: {salida_actual_texto}")
        pyautogui.click(chatX, chatY)
        pyautogui.write('/clear')
        time.sleep(2)
        pyautogui.press('enter')

        # Extraer coordenadas
        c1 = salida_actual_texto[0]
        c2 = salida_actual_texto[1]

        # Actualizar las coordenadas en la interfaz
        game_coords = (c1, c2)
        self.coordActual.config(text=f"{game_coords}")
        self.coordActual.update_idletasks()
        time.sleep(1)
        pyautogui.click(merkaX, merkaY)
        time.sleep(2)

    def checkPistas(self):
        self.recorte_Imagen(self.area_pistas)
        cantidad = self.cantidad_pistas()
        self.cantidadPistas.config(text=f"{cantidad}")
        self.cantidadPistas.update_idletasks()

    def cantidad_pistas(self):
        try:
            # Cargar la imagen de la captura de pantalla
            captura_pantalla = cv2.imread(ruta_imagen_recortada)
            if captura_pantalla is None:
                raise ValueError(
                    f"No se pudo cargar la imagen de captura de pantalla desde {ruta_imagen_recortada}")

            # Cargar la imagen de referencia
            referencia = cv2.imread(ruta_imagen_interrogacion)
            if referencia is None:
                raise ValueError(
                    f"No se pudo cargar la imagen de referencia desde {ruta_imagen_interrogacion}")

            # Buscar la imagen de referencia en la captura de pantalla
            resultado = cv2.matchTemplate(
                captura_pantalla, referencia, cv2.TM_CCOEFF_NORMED)

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

        finally:
            # Liberar recursos para evitar acumulación de memoria
            del captura_pantalla, referencia, resultado, ubicaciones
            gc.collect()  # Llamar al recolector de basura para limpiar memoria
            # Asegurarse de que cualquier ventana de OpenCV se cierre correctamente
            cv2.destroyAllWindows()

    def checkEtapa(self):
        self.recorte_Imagen(self.area_etapa_actual)
        primer_numero, segundo_numero = self.verificacion_etapas()
        etapa_actual = (primer_numero, segundo_numero)
        self.etapaActual.config(text=f"{etapa_actual}")
        self.etapaActual.update_idletasks()

    def verificacion_etapas(self):
        try:
            # Realizar OCR en la imagen recortada
            # Suponiendo que OCR es tu método para extraer texto de imágenes
            texto = self.OCR(ruta_imagen_recortada)
            texto = texto.strip()

            # Impresión de depuración
            #print(f"Texto extraído por OCR: '{texto}'")

            # Separar la información en partes usando el espacio como delimitador
            separado = texto.split(' ')

            if len(separado) < 2:
                raise ValueError(
                    f"El texto extraído no tiene el formato esperado: '{texto}'")

            # Buscar los números en la última parte de la cadena separada
            numeros = separado[-1].split('/')

            if len(numeros) < 2:
                raise ValueError(
                    f"No se encontraron dos números separados por '/'. Texto procesado: '{separado[-1]}'")

            # Guardar los números en variables separadas
            primer_numero = numeros[0]
            segundo_numero = numeros[1]

            return primer_numero, segundo_numero

        except Exception as e:
            print(f"Error en verificacion_etapas: {e}")
            return None, None  # Devuelve valores por defecto si hay error

        finally:
            # Asegurar la liberación de memoria si se utilizaron variables que contienen imágenes u otros recursos
            gc.collect()  # Recolección de basura para liberar memoria no utilizada
            cv2.destroyAllWindows()  # Cerrar cualquier ventana abierta por OpenCV

    def checkSalida(self):
        self.capturaPantalla()
        try:
            self.recorte_Imagen(self.area_salida)
            time.sleep(2)

            # Realizar OCR en la imagen preprocesada
            salida_actual_texto = self.OCR(ruta_imagen_recortada)
            print(salida_actual_texto)

            # Extraer números de la salida
            salida_actual_texto = re.findall(r'-?\d+', salida_actual_texto)
            if len(salida_actual_texto) < 2:
                raise ValueError(
                    "No se encontraron suficientes números en la salida de Tesseract.")

            # Procesar los números
            c1 = salida_actual_texto[0]
            c2 = salida_actual_texto[1]
            salida_actual = (c1, c2)

            self.salida.config(text=f"{salida_actual}")
            self.salida.update_idletasks()

        except Exception as e:
            # Lanzar la excepción para que sea capturada en startTask()
            print(f"Error en checkSalida: {e}")
            raise
    
    # ----------------------------#
    # Funciones de treasure hunt
    # ----------------------------#

    # Mueve el personaje hasta el mapa del cofre -25, -36 (ingresa al edificio)
    def irACofreTesoros(self):
        self.clickEnImagen(ruta_imagen_merkasako, 100)
        time.sleep(0.5)
        self.clickEnImagen(ruta_imagen_zaap_merka, 100)
        time.sleep(0.5)
        self.clickEnImagen(ruta_imagen_buscar_zaap, 100)
        time.sleep(0.5)
        # escribir coord
        pyautogui.write('Campos de Cania')
        time.sleep(0.5)
        self.clickEnImagen(ruta_imagen_teleport_btn, 100)
        time.sleep(2)
        self.clickEnImagen(ruta_imagen_chat_box, 100)
        time.sleep(0.5)
        pyautogui.write('/travel -25 -36')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        self.clickEnImagen(ruta_imagen_entreda_cofre, 1000)
        pyautogui.click()
        self.clickEnImagen(ruta_imagen_mover2, 100)
        self.clickEnImagen(ruta_imagen_chat_box, 100)
        pyautogui.write('/clear')
        pyautogui.press('enter')
        time.sleep(1)

    def obtenerBusqueda(self):
        self.clickEnImagen(ruta_imagen_tesoro, 300)
        pyautogui.click()
        time.sleep(3)
        levelSeleccionado = self.cboxHuntlvl.get()
        if levelSeleccionado:
            valor_guardado = levelSeleccionado
            print(f"Level de treasure hunt seleccionado: {valor_guardado}")
            if valor_guardado == "140":
                self.clickEnImagen(ruta_imagen_140, 300)
            if valor_guardado == "160":
                self.clickEnImagen(ruta_imagen_160, 300)
            if valor_guardado == "180":
                self.clickEnImagen(ruta_imagen_180, 300)
            if valor_guardado == "200":
                self.clickEnImagen(ruta_imagen_200, 300)
        else:
            print("No hay level seleccionado")
        pyautogui.click()
        time.sleep(5)
        self.etapa_iniciada = True
        self.save_to_text_file()
        self.clickEnImagen(ruta_imagen_salir, 300)
        time.sleep(4)
        self.clickEnImagen(ruta_imagen_salir_puerta, 300)
        time.sleep(5)

    def irACoordenadaMasCercana(self, nombre_cercano):
        # recibe nombre de teleport
        merkaX, merkaY = self.get4CoordFromText(self.btnMerkasako['text'])
        zaapMerkaX, zaapMerkaY = self.get4CoordFromText(
            self.zaapMerkasako['text'])
        buscarZaapX, buscarZaapY = self.get4CoordFromText(
            self.buscarZaap['text'])
        teleport_zaapX, teleport_zaapY = self.get4CoordFromText(
            self.teleportMerka['text'])
        pyautogui.click(merkaX, merkaY)
        time.sleep(3)
        pyautogui.click(zaapMerkaX, zaapMerkaY)
        time.sleep(2)
        pyautogui.click(buscarZaapX, buscarZaapY)
        time.sleep(2)
        # escribir coord
        pyautogui.write(nombre_cercano)
        time.sleep(2)
        pyautogui.click(teleport_zaapX, teleport_zaapY)
        # self.clickEnImagen(ruta_imagen_teleport_btn)
        time.sleep(2)
        self.checkGameCoord()

    def verificacionPistas(self):
        # Realiza la busqueda según la cantidad de pistas (?)
        cantPistasTexto = self.cantidadPistas['text']
        # self.cantidadPistas = int(cantPistasTexto)

        if cantPistasTexto == "0":
            print("Cero '?'")

            print("Pista1")
            self.recorte_Imagen(self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_1)
            self.pista(texto_hasta_coma)
            if self.etapa_iniciada == False or self.reset == True:
                return
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)
        if cantPistasTexto == "1":
            print("Uno '?'")

            print("Pista1")
            self.recorte_Imagen(self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_1)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_2)
            self.pista(texto_hasta_coma)
            if self.etapa_iniciada == False or self.reset == True:
                return
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "2":
            print("Dos '?'")

            print("Pista1")
            self.recorte_Imagen(self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_1)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_2)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_3)
            self.pista(texto_hasta_coma)
            if self.etapa_iniciada == False or self.reset == True:
                return
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "3":
            print("Tres '?'")

            print("Pista1")
            self.recorte_Imagen(self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_1)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_2)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_3)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_4)
            self.pista(texto_hasta_coma)
            if self.etapa_iniciada == False or self.reset == True:
                return
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == '4':
            print("Cuatro '?'")

            print("Pista1")
            self.recorte_Imagen(self.area_salida)
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_1)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_2)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_3)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_4)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista5")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_5)
            self.pista(texto_hasta_coma)
            if self.etapa_iniciada == False or self.reset == True:
                return
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)
        elif cantPistasTexto == "5":
            print("Cinco '?'")

            print("Pista1")
            # obtiene coord de salida
            self.recorte_Imagen(self.area_salida)
            # escribe coord de salida en navegador
            # cordenadas()
            self.checkSalida()
            inicio = self.salida['text']
            self.coordEnNav(inicio)
            # recorta flecha de primera pista
            # recorte_primerapista_flecha(ruta_imagen_captura)
            self.recorte_Imagen(self.area_flecha_1)
            time.sleep(0.5)
            # obtiene la direccion segun la flecha
            # texto_hasta_coma = self.obtenerDireccion(self.area_arriba, self.area_pistaDL_1) #comparacion_flechas()
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            # obtiene recorte de pista
            # recorte_primerapista(ruta_imagen_captura)
            self.recorte_Imagen(self.area_pista_1)
            # obtiene texto de pista de recorte
            # OCR(ruta_imagen_recortada)
            # mueve el personaje según la pista obtenida
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista2")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_2)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_2)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista3")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_3)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_3)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista4")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_4)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_4)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista5")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_5)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_5)
            self.pista(texto_hasta_coma)

            if self.etapa_iniciada == False or self.reset == True:
                return

            print("Pista6")
            self.checkGameCoord()
            inicio = self.coordActual['text']
            self.coordEnNav(inicio)
            self.recorte_Imagen(self.area_flecha_6)
            texto_hasta_coma = self.detectar_direccion()
            time.sleep(0.5)
            self.moverEnDireccion(texto_hasta_coma)
            self.recorte_Imagen(self.area_pista_6)
            self.pista(texto_hasta_coma)
            
            if self.etapa_iniciada == False or self.reset == True:
                return
            
            self.etapa_finalizada(ruta_imagen_etapa_finalizada)

    def coordEnNav(self, inicio):
        # Ingresa las coordenadas entregadas en el navegador
        salida_actual_texto = self.cleanText(inicio)
        salida_actual_texto = re.findall(r'-?\d+', salida_actual_texto)
        c1 = salida_actual_texto[0]
        c2 = salida_actual_texto[1]
        print('click en X')
        xnavX, xnavY = self.get4CoordFromText(self.navX['text'])
        pyautogui.tripleClick(xnavX, xnavY)
        time.sleep(2)
        pyautogui.write(c1)
        time.sleep(2)
        print('click en Y')
        ynavX, ynavY = self.get4CoordFromText(self.navY['text'])
        pyautogui.tripleClick(ynavX, ynavY)
        time.sleep(2)
        pyautogui.write(c2)
        time.sleep(2)
        self.capturaPantalla()
    
    def detectar_direccion(self):
        # reconoce hacia donde apunta la flecha
        try:
            # Cargar la imagen que se quiere analizar en escala de grises
            imagen = cv2.imread(ruta_imagen_recortada, cv2.IMREAD_GRAYSCALE)
            if imagen is None:
                raise FileNotFoundError(f"No se pudo cargar la imagen en la ruta: {ruta_imagen_recortada}")

            # Cargar las imágenes de referencia de las flechas
            flecha_arriba = cv2.imread(
                ruta_imagen_flecha_arriba1, cv2.IMREAD_GRAYSCALE)
            flecha_abajo = cv2.imread(
                ruta_imagen_flecha_abajo1, cv2.IMREAD_GRAYSCALE)
            flecha_izquierda = cv2.imread(
                ruta_imagen_flecha_izquierda1, cv2.IMREAD_GRAYSCALE)
            flecha_derecha = cv2.imread(
                ruta_imagen_flecha_derecha1, cv2.IMREAD_GRAYSCALE)

            # Verificar que todas las imágenes de referencia se carguen correctamente
            if any(flecha is None for flecha in [flecha_arriba, flecha_abajo, flecha_izquierda, flecha_derecha]):
                raise FileNotFoundError(
                    "Una o más imágenes de referencia de flechas no se pudieron cargar.")

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
                # Redimensionar la imagen de referencia si es necesario
                # Suponiendo que este método está implementado
                plantilla = self.resize_image_if_needed(imagen, plantilla)
                if plantilla is not None:
                    resultado = cv2.matchTemplate(imagen, plantilla, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, _ = cv2.minMaxLoc(resultado)

                    # Si esta coincidencia es mejor que las anteriores, la guardamos
                    if max_val > mejor_valor:
                        mejor_valor = max_val
                        mejor_direccion = direccion

            # Imprimir y devolver la mejor dirección encontrada
            print(f"La direccion de la pista es: {mejor_direccion}")
            return mejor_direccion

        except Exception as e:
            print(f"Error al detectar la dirección: {e}")
            return None  # Devuelve None si ocurre algún error

        finally:
            # Liberar recursos y limpiar la memoria
            del flecha_arriba, flecha_abajo, flecha_izquierda, flecha_derecha, resultado, imagen
            gc.collect()
            cv2.destroyAllWindows()
    
    def moverEnDireccion(self, direccion):
        # Capturamos el texto antes de la coma
        texto_hasta_coma = direccion
        self.direccionActual = texto_hasta_coma
        # Si la dirección es hacia el sur
        if texto_hasta_coma == "Dirigete hacia el Sur,":
            #self.navegacion_flechas(ruta_imagen_flecha_abajo2)
            self.seleccionarDireccionNav('down')
            time.sleep(0.5)
            return texto_hasta_coma

        # Si la dirección es hacia el norte
        elif texto_hasta_coma == "Dirigete hacia el Norte,":
            #self.navegacion_flechas(ruta_imagen_flecha_arriba2)
            self.seleccionarDireccionNav('up')
            time.sleep(0.5)
            return texto_hasta_coma

            # Si la dirección es hacia el oeste
        elif texto_hasta_coma == "Dirigete hacia el Oeste,":
            #self.navegacion_flechas(ruta_imagen_flecha_izquierda2)
            self.seleccionarDireccionNav('left')
            time.sleep(0.5)
            return texto_hasta_coma

            # Si la dirección es hacia el este
        elif texto_hasta_coma == "Dirigete hacia el Este,":
            #self.navegacion_flechas(ruta_imagen_flecha_derecha2)
            self.seleccionarDireccionNav('right')
            time.sleep(0.5)
            return texto_hasta_coma

        
    
    def navegacion_flechas(self, ruta_imagen):
        # seleccionar la flecha en navegador
        # si se activa la el mensaje de captcha, seleciona el segundo navegar y reintenta
        global intentos_realizados
        try:
            # Incrementar los intentos realizados
            intentos_realizados += 1

            # Límite de intentos alcanzado
            if intentos_realizados > limite_intentos:
                print("Límite de intentos alcanzado. La imagen no se encontró.")
                return

            # Cargar la imagen de referencia
            imagen_referencia = cv2.imread(ruta_imagen)
            if imagen_referencia is None:
                raise FileNotFoundError(
                    f"No se pudo cargar la imagen de referencia desde: {ruta_imagen}")

            # Capturar la pantalla actual
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Obtener dimensiones de la imagen de referencia
            altura, ancho = imagen_referencia.shape[:2]

            # Realizar coincidencia de plantillas
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Definir un umbral de confianza
            umbral_confianza = 0.8
            print(f"Valor de coincidencia: {max_val}")

            if max_val >= umbral_confianza:
                # Obtener las coordenadas del centro de la imagen de referencia
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2

                # Hacer clic en el centro de la imagen encontrada
                pyautogui.click(centro_x, centro_y)
            else:
                # Recursión si no se encuentra la imagen
                print("Imagen no encontrada, reintentando...")
                self.navegacion_flechas(ruta_imagen)

        except Exception as e:
            print(f"Error durante la navegación con flechas: {e}")
            return

        finally:
            # Liberar recursos y limpiar la memoria
            del resultado, captura_pantalla, captura_pantalla_np, captura_pantalla_cv2, imagen_referencia
            gc.collect()
            cv2.destroyAllWindows()

        # Busca la imagen 'Ha llegado a destino' en chat

    #NUEVO en prueba
    def seleccionarDireccionNav(self, direction):
        print('click en espacio en blanco (usar ubicacion de reload)')
        xnavX, xnavY = self.get4CoordFromText(self.reloadNav['text'])
        pyautogui.click(xnavX, xnavY)
        pyautogui.press(direction)
        time.sleep(2)
        #chequear si aparecio el captcha

    def pista(self, texto_hasta_coma):
            # Chequeo de pista, si tiene Perforatroz lo busca, si no, lo escribe en el navegador
            texto_hasta_coma = texto_hasta_coma
            texto = self.OCR(ruta_imagen_recortada)
            # texto = re.findall(r'[a-zA-Z ]', texto)
            # texto = ''.join(texto)
            print(texto)
            time.sleep(0.5)
            # print(texto)
            # print(texto_hasta_coma)
            if "Perforatroz" in texto:
                # buscar_y_clickear_dofus(ruta_imagen_dofus)
                if self.buscar_var.get():
                    self.clickEnImagen(ruta_imagen_minBusqueda, 100)
                    self.checkGameCoord()
                    time.sleep(2)
                    comienzo_perfo_actual = self.coordActual['text']
                    self.condicion_perforatroz(texto_hasta_coma, comienzo_perfo_actual)
                else:
                    # eliminar busqueda()
                    self.eliminarBusqueda()
                    self.numero_pista = 0
                    self.etapa_iniciada = False
                    self.save_to_text_file()
                    # raise Exception("Busqueda eliminada")
            else:
                # pyautogui.tripleClick(755, 727)
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
                # pyautogui.tripleClick(657, 766)
                self.travel()

    def condicion_perforatroz(self, texto_hasta_coma, comienzo_perfo_actual):
        texto_hasta_coma = texto_hasta_coma
        # self.checkGameCoord()
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

        # c1, c2 = comienzo_perfo_actual
        if (self.mapas_avanzados > 10):
            self.clickEnImagen(ruta_imagen_chat_box, 100)
            pyautogui.write(f"/travel {primer_numero} {segundo_numero}")
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
            chatBox(ruta_imagen_chat_box)
            pyautogui.write('/clear')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            self.mapas_avanzados = 0

        if texto_hasta_coma == "Dirigete hacia el Sur,":
            # funcion para moverse abajo
            #time.sleep(2)
            print(self.moverAbajo['text'])
            texto = self.moverAbajo['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(7)
            self.buscar_y_clickear_perforatroz(
                texto_hasta_coma, comienzo_perfo_actual)
        elif texto_hasta_coma == "Dirigete hacia el Norte,":
            # funcion para moverse arriba
            #time.sleep(2)
            print(self.moverArriba['text'])
            texto = self.moverArriba['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(6)
            self.buscar_y_clickear_perforatroz(
                texto_hasta_coma, comienzo_perfo_actual)
        elif texto_hasta_coma == "Dirigete hacia el Oeste,":
            # funcion para moverse izquierda
            #time.sleep(2)
            print(self.moverIzquierda['text'])
            texto = self.moverIzquierda['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(6)
            self.buscar_y_clickear_perforatroz(
                texto_hasta_coma, comienzo_perfo_actual)
        elif texto_hasta_coma == "Dirigete hacia el Este,":
            # funcion para moverse derecha
            #time.sleep(2)
            print(self.moverDerecha['text'])
            texto = self.moverDerecha['text']
            c1, c2 = self.get4CoordFromText(texto)
            pyautogui.tripleClick(c1, c2)
            time.sleep(6)
            self.buscar_y_clickear_perforatroz(
                texto_hasta_coma, comienzo_perfo_actual)

    def travel(self):
        # Mueve al personaje hacia un destino
        # buscar_y_clickear_dofus(ruta_imagen_dofus)
        # pyautogui.press('w')
        # chatBox(ruta_imagen_chat_box)
        chatX, chatY = self.get4CoordFromText(self.chat['text'])
        # self.clickEnImagen(ruta_imagen_chat_box)
        pyautogui.tripleClick(chatX, chatY)
        time.sleep(2)
        texto = pyperclip.paste()
        #si el texto tiene [] quiere decir que no se encontró la pista
        print(texto)
        if '[' in texto:
            print('No se encontró la pista, tal vez deberia reiniciar busqueda}')
            #self.restablecerEtapa()
        else:
        #pandala    
            if '19 -26' in texto:
                    pyautogui.write('/travel 25 -28')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                    time.sleep(1)
                    self.eliminar_chat()
                    time.sleep(1)
            if '23 -26' in texto:
                    pyautogui.write('/travel 25 -28')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                    time.sleep(1)
                    self.eliminar_chat()
                    time.sleep(1)
            if '20 -26' in texto:
                    pyautogui.write('/travel 25 -28')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                    time.sleep(1)
                    self.eliminar_chat()
                    time.sleep(1)
            if '21 -26' in texto:
                    pyautogui.write('/travel 25 -28')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                    time.sleep(1)
                    self.eliminar_chat()
                    time.sleep(1)
            if '19 -34' in texto:
                    pyautogui.write('/travel 20 -32')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                    time.sleep(1)
                    self.eliminar_chat()
                    time.sleep(1)
            
            #brakmar
            if '-22 35' in texto:
                pyautogui.write('/travel -24 39')
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                time.sleep(1)
                self.eliminar_chat()
                
            if '-22 32' in texto:
                pyautogui.write('/travel -24 39')
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                time.sleep(1)
                self.eliminar_chat()
                
            if '-21 39' in texto:
                pyautogui.write('/travel -24 39')
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                time.sleep(1)
                self.eliminar_chat()
                
            if '-22 39' in texto:
                pyautogui.write('/travel -24 39')
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
                self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                time.sleep(1)
                self.eliminar_chat()
            
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            self.ha_llegado_destino(ruta_imagen_llegado_destino)

    def pelea(self):
        global inBattle
        inBattle = True
        # self.click_mas_lejano()
        # time.sleep(2)
        # pyautogui.press('esc')
        self.checkBattle()
        time.sleep(3)
        pyautogui.press('F1')
        time.sleep(2)
        pyautogui.press('F1')
        time.sleep(6)
        while inBattle == True:  # Mientras la condición sea verdadera
            time.sleep(5)
            # 2 atks
            pyautogui.press('1')
            time.sleep(2)
            self.buscar_y_clickear_monstruo(ruta_imagen_monstruo)
            time.sleep(1)
            pyautogui.press('F1')
            time.sleep(1)

    # ------------#
    # Save/Load
    # ------------#

    def save_to_text_file(self):
        with open('variables.txt', 'w') as file:

            # Áreas de recorte
            file.write(f"area_game_coord: {self.area_game_coord}\n")
            file.write(f"area_etapa_actual: {self.area_etapa_actual}\n")
            file.write(f"area_salida: {self.area_salida}\n")
            file.write(f"area_chat: {self.area_chat}\n")

            # '?'
            file.write(f"area_pistas: {self.area_pistas}\n")

            # pistas (texto) (flecha - pista - banderita)
            file.write(f"area_pista1: {self.area_pista_1}\n")
            file.write(f"area_pista2: {self.area_pista_2}\n")
            file.write(f"area_pista3: {self.area_pista_3}\n")
            file.write(f"area_pista4: {self.area_pista_4}\n")
            file.write(f"area_pista5: {self.area_pista_5}\n")
            file.write(f"area_pista6: {self.area_pista_6}\n")

            # flechas
            file.write(f"area_flecha_1: {self.area_flecha_1}\n")
            file.write(f"area_flecha_2: {self.area_flecha_2}\n")
            file.write(f"area_flecha_3: {self.area_flecha_3}\n")
            file.write(f"area_flecha_4: {self.area_flecha_4}\n")
            file.write(f"area_flecha_5: {self.area_flecha_5}\n")
            file.write(f"area_flecha_6: {self.area_flecha_6}\n")

            # pista (direccion)
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

            file.write(f"bandera1: {self.pistaDL6['text']}\n")
            file.write(f"buscar_perforatroz: {self.buscar_var.get()}\n")

        self.status_label.config(text=f"Datos guardados")

    def load_from_text_file(self):
        with open('variables.txt', 'r') as file:
            lines = file.readlines()

            if len(lines) > 0 and lines[0].strip():
                self.area_game_coord = eval(lines[0].split(': ')[1].strip())
                # self.checkGameCoord()

            if len(lines) > 1 and lines[1].strip():
                self.area_etapa_actual = eval(lines[1].split(': ')[1].strip())
                # self.checkEtapa()

            if len(lines) > 2 and lines[2].strip():
                self.area_salida = eval(lines[2].split(': ')[1].strip())
                # self.checkSalida()

            if len(lines) > 3 and lines[3].strip():
                texto_area_chat = eval(lines[3].split(': ')[1].strip())
                self.chat.config(text=f"{texto_area_chat}")

            if len(lines) > 4 and lines[4].strip():
                self.area_pistas = eval(lines[4].split(': ')[1].strip())
                # self.checkPistas()

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
                # self.characterName.insert(0, f"{texto_charcater_name}")

            if len(lines) > 29 and lines[29].strip():
                texto_entryPytesseract = lines[29].strip()
                texto_entryPytesseract = texto_entryPytesseract.replace(
                    'ruta_tesseract: ', '')
                self.entryPytesseract.delete(0, 'end')
                self.entryPytesseract.insert(0, texto_entryPytesseract)

            if len(lines) > 30 and lines[30].strip():
                texto_umbral = eval(lines[30].split(': ')[1].strip())
                self.umbral.delete(0, 'end')
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

            if len(lines) > 35 and lines[35].strip():
                texto = eval(lines[35].split(': ')[1].strip())
                self.pistaDL6.config(text=f"{texto}")

            if len(lines) > 36 and lines[36].strip():
                texto = eval(lines[36].split(': ')[1].strip())
                # self.pistaDL6.config(text=f"{texto}")
                nuevo_valor = texto  # == "True"
                self.buscar_var.set(nuevo_valor)
                self.buscarPerforatroz.config(variable=self.buscar_var)
                self.buscarPerforatroz.update_idletasks()

        self.status_label.config(text=f"Datos cargados")

    # -------#
    # Utils
    # -------#

    def eliminar_chat(self):
        # pyautogui.press('w')
        # chatBox(ruta_imagen_chat_box)
        chatX, chatY = self.get4CoordFromText(self.chat['text'])
        pyautogui.tripleClick(chatX, chatY)
        pyautogui.write('/clear')
        pyautogui.press('enter')
        time.sleep(0.5)

    def resize_image_if_needed(self, imagen, plantilla):
        h_imagen, w_imagen = imagen.shape[:2]
        h_plantilla, w_plantilla = plantilla.shape[:2]

        if h_plantilla > h_imagen or w_plantilla > w_imagen:
            scale_height = h_imagen / h_plantilla
            scale_width = w_imagen / w_plantilla
            scale = min(scale_height, scale_width)
            plantilla = cv2.resize(
                plantilla, (int(w_plantilla * scale), int(h_plantilla * scale)))

        return plantilla

    def cerrar_ventana(self, event=None):
        """Función para cerrar la ventana al presionar Esc"""
        self.area_selector_window.destroy()

    def recorte_Imagen(self, coords):
        # Capturar la pantalla con pyautogui y guardar la captura
        #imagen = pyautogui.screenshot()
        #imagen.save(ruta_imagen_captura)

        # Cargar la imagen guardada con OpenCV
        imagen_cv2 = cv2.imread(ruta_imagen_captura)

        # Verificar si la imagen se cargó correctamente
        if imagen_cv2 is None:
            raise FileNotFoundError(
                f"No se pudo cargar la imagen en la ruta: {ruta_imagen_captura}")

        try:
            # Definir las coordenadas del recorte (x1, y1, x2, y2)
            x1, y1, x2, y2 = coords

            # Verificar que las coordenadas estén dentro del rango de la imagen
            height, width = imagen_cv2.shape[:2]
            if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
                raise ValueError(
                    "Las coordenadas de recorte están fuera de los límites de la imagen.")

            # Realizar el recorte de la región de interés
            recorte = imagen_cv2[y1:y2, x1:x2]

            # Verificar si el recorte es válido
            if recorte.size == 0:
                raise ValueError(
                    "El recorte resultante está vacío. Verifica las coordenadas.")

            # Guardar el recorte en un archivo
            cv2.imwrite(ruta_imagen_recortada, recorte)

        finally:
            # Liberar recursos de OpenCV
            del imagen_cv2, recorte
            gc.collect()  # Llamar al recolector de basura para limpiar memoria
            # Asegurarse de que cualquier ventana de OpenCV se cierre correctamente
            cv2.destroyAllWindows()

    def cleanText(self, text):
        texto = text
        texto = texto.replace('(', '')
        texto = texto.replace(')', '')
        texto = texto.replace("'", "")
        return texto

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

    def capturaPantalla(self):
        try:
            # Verifica si la ruta es válida
            if not ruta_imagen_captura:
                raise ValueError(
                    "La ruta para guardar la captura de pantalla no está definida.")

            # Realiza la captura de pantalla
            imagen = pyautogui.screenshot()

            # Intenta guardar la imagen en la ruta especificada
            imagen.save(ruta_imagen_captura)
            print(f"Captura de pantalla guardada en {ruta_imagen_captura}")

            # Elimina la imagen para liberar memoria
            del imagen

            # Pausa para asegurar que la captura se complete
            time.sleep(1)

            # Forzar la recolección de basura para liberar memoria
            gc.collect()

        except Exception as e:
            print(f"Error al capturar o guardar la imagen: {e}")

    def resetTreasure(self):
        self.etapa_iniciada = False
        self.pistaD5.config(text=f"{self.etapa_iniciada}")

    def restablecerEtapa(self):
        self.numero_pista == 0
        enMerka = self.buscar_image(ruta_imagen_zaap_merka)
        time.sleep(1)
        hayBanderitaActivada = self.buscar_image(ruta_imagen_banderita_brillante)
        hayBanderita = self.buscar_image(ruta_imagen_banderita)
        time.sleep(1)
        if enMerka == True:
            print('en merka, hay que salir')
            # clic boton merka para salir
            merkaX, merkaY = self.get4CoordFromText(self.btnMerkasako['text'])
            pyautogui.click(merkaX, merkaY)
            time.sleep(3)
        # hay banderita brillante?
        if hayBanderitaActivada == True:
            # si hay, presionar
            print('borrar pistas encontradas')
            bandBriX, bandBriY = self.get4CoordFromText(self.pistaDL6['text'])
            pyautogui.click(bandBriX, bandBriY)
            #self.etapa_iniciada = True
        self.numero_pista = 0
        self.capturaPantalla()
        self.checkEtapa()
        self.checkPistas()
        self.checkSalida(1)
        #self.numero_pista = 0
        #self.etapa_iniciada = False
        self.reset = True
        self.save_to_text_file()

   # Elimina la busqueda actual

    def eliminarBusqueda(self):
        self.clickEnImagen(ruta_imagen_cerrar_busqueda, 100)
        time.sleep(1)
        pyautogui.press('enter')

    def encontrar_imagen(lista_rutas_imagenes, captura_pantalla, precision=0.8, clic=True):
        # captura_pantalla = pyautogui.screenshot()
        captura_np = np.array(captura_pantalla)
        captura_gray = cv2.cvtColor(captura_np, cv2.COLOR_BGR2GRAY)

        for ruta_imagen in lista_rutas_imagenes:
            # Cargar la imagen de plantilla
            imagen_template = cv2.imread(ruta_imagen, 0)
            if imagen_template is None:
                print(f"Error al cargar la imagen {ruta_imagen}")
                continue

            # Ejecutar la comparación de la plantilla
            resultado = cv2.matchTemplate(
                captura_gray, imagen_template, cv2.TM_CCOEFF_NORMED)
            ubicaciones = np.where(resultado >= precision)

            # Si se encuentra una coincidencia
            if len(ubicaciones[0]) > 0:
                print(f"Imagen encontrada: {ruta_imagen}")
                # Calcular el punto central de la imagen detectada
                punto_max = (ubicaciones[1][0], ubicaciones[0][0])
                h, w = imagen_template.shape
                centro = (punto_max[0] + w // 2, punto_max[1] + h // 2)

                # Realizar clic en la posición si es necesario
                if clic:
                    pyautogui.click(centro[0], centro[1])
                return True  # Se encontró y se hizo clic en la imagen
        return False  # No se encontró ninguna imagen

    def distancia(self, p1, p2):
        """Calcula la distancia euclidiana entre dos puntos"""
        return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def click_mas_lejano(self):
        """Encuentra y hace clic en la imagen roja más lejana del monstruo"""
        # Captura de pantalla
        screenshot = pyautogui.screenshot()

        rutas_alternativas = [
            "./treasureHunt/battle/1.png",
            './treasureHunt/battle/2.png',
            './treasureHunt/battle/3.png',
            './treasureHunt/battle/4.png'
        ]

        rutas_rojo = [
            './treasureHunt/battle/rojo.png'
        ]

        # Encontrar el monstruo
        monstruo_coincidencias = self.encontrar_imagen(
            rutas_alternativas, screenshot)

        if not monstruo_coincidencias:
            print("No se encontró el monstruo en la pantalla.")
            return

        # Asumimos que solo hay un monstruo
        monstruo_pos = monstruo_coincidencias[0]

        # Encontrar todas las coincidencias de la imagen roja
        rojo_coincidencias = self.encontrar_imagen(rutas_rojo, screenshot)

        if not rojo_coincidencias:
            print("No se encontró ninguna imagen roja en la pantalla.")
            return

        # Encontrar la coincidencia más lejana
        max_distancia = 0
        rojo_mas_lejano = None

        for rojo_pos in rojo_coincidencias:
            dist = self.distancia(monstruo_pos, rojo_pos)
            if dist > max_distancia:
                max_distancia = dist
                rojo_mas_lejano = rojo_pos

        # Hacer clic en la imagen roja más lejana
        if rojo_mas_lejano:
            print(f"Click en la posición más lejana: {rojo_mas_lejano}")
            pyautogui.click(rojo_mas_lejano[0], rojo_mas_lejano[1])

        # Liberar memoria de la captura de pantalla
        del screenshot

        # Cerrar todas las ventanas abiertas de OpenCV si se hubieran abierto (aunque no lo estamos usando aquí)
        cv2.destroyAllWindows()

    # -----------------------------------------
    # Click en imagenes, ESTAS PODRIAN CAMBIAR
    # -----------------------------------------

    def clickEnImagen(self, ruta_imagen, cantidad):
        # Seguimiento de los intentos realizados
        intentos_realizados = 0

        while intentos_realizados < cantidad:
            try:
                # Incrementar los intentos realizados
                intentos_realizados += 1

                # Carga la imagen de referencia y la captura de pantalla
                imagen_referencia = cv2.imread(ruta_imagen)
                captura_pantalla = pyautogui.screenshot()
                captura_pantalla_np = np.array(captura_pantalla)
                captura_pantalla_cv2 = cv2.cvtColor(
                    captura_pantalla_np, cv2.COLOR_RGB2BGR)

                # Verifica que las imágenes se hayan cargado correctamente
                if imagen_referencia is None or captura_pantalla_cv2 is None:
                    raise ValueError("Error al cargar las imágenes.")

                # Obtén las dimensiones de la imagen de referencia
                altura, ancho, _ = imagen_referencia.shape

                # Encuentra la posición de la imagen de referencia en la captura de pantalla
                resultado = cv2.matchTemplate(
                    captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

                # Define un umbral de confianza (ajusta según tus necesidades)
                umbral_confianza = float(self.umbral.get())
                print(f"Valor de coincidencia: {max_val}")

                if max_val >= umbral_confianza:
                    # Obtiene las coordenadas del centro de la imagen de referencia
                    centro_x = max_loc[0] + ancho // 2
                    centro_y = max_loc[1] + altura // 2

                    # Haz clic en el centro de la imagen encontrada
                    pyautogui.click(centro_x, centro_y)
                    print(f"Clic realizado en ({centro_x}, {centro_y})")
                    time.sleep(1)

                    # Libera la memoria de las imágenes antes de salir
                    del imagen_referencia
                    del captura_pantalla_cv2
                    return  # Salir de la función después de hacer clic exitosamente

                else:
                    print("Imagen no encontrada, intentando de nuevo...")
                    # Añadir un pequeño retraso antes de reintentar
                    time.sleep(1)

                # Libera la memoria de las imágenes antes de la siguiente iteración
                del imagen_referencia
                del captura_pantalla_cv2

            except Exception as e:
                print(f"Error en clickEnImagen: {e}")
                break  # Salir del bucle si hay un error crítico

        raise RuntimeError(
            "Límite de intentos alcanzado o error crítico, no se encontró la imagen.")

    def buscar_y_clickear_perforatroz(self, texto_hasta_coma, coordActual):
        global intentos_realizados
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1

        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return

        # Lista de rutas alternativas de imágenes
        rutas_alternativas = [
            "./treasureHunt/perforatroz.png",
            './treasureHunt/perforatroz3.png',
            './treasureHunt/perforatroz4.png',
            './treasureHunt/perforatroz5.png',
            './treasureHunt/perforatroz15.png'
        ]

        # Captura la pantalla completa solo una vez
        x1, y1, x2, y2 = 330, 50, 1580, 900
        captura_pantalla = pyautogui.screenshot(
            region=(x1, y1, x2 - x1, y2 - y1))
        captura_pantalla_np = np.array(captura_pantalla)
        captura_pantalla_cv2 = cv2.cvtColor(
            captura_pantalla_np, cv2.COLOR_RGB2BGR)

        time.sleep(3)

        # Iterar sobre las rutas alternativas de las imágenes
        for ruta_alternativa in rutas_alternativas:
            imagen_referencia = cv2.imread(ruta_alternativa)

            if imagen_referencia is not None:
                # Obtén las dimensiones de la imagen de referencia
                altura, ancho, _ = imagen_referencia.shape

                # Encuentra la posición de la imagen de referencia en la captura de pantalla
                resultado = cv2.matchTemplate(
                    captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

                # Define un umbral de confianza (puedes ajustar según tus necesidades)
                umbral_confianza = 0.8
                print(f"Confianza: {max_val} en la ruta: {ruta_alternativa}")

                if max_val >= umbral_confianza:
                    print(f"Imagen encontrada en la ruta: {ruta_alternativa}")

                    # Realiza el clic en la imagen
                    self.clickEnImagen(ruta_imagen_maxBusqueda, 100)
                    time.sleep(2)

                    # Llama a la función banderita
                    self.banderita(ruta_imagen_banderita)
                    # self.checkGameCoord()
                    # Termina el bucle ya que se encontró y clickeó una imagen
                    return
            else:
                print(
                    f"Error al cargar la imagen de la ruta: {ruta_alternativa}")

        # Si no se encuentra ninguna imagen, llama a la función de condición de perforatroz
        self.condicion_perforatroz(texto_hasta_coma, coordActual)

    def hintBox(self, ruta_imagen):
        global intentos_realizados

        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1

        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return

        try:
            # Carga las imágenes de referencia y la captura de pantalla
            imagen_referencia = cv2.imread(ruta_imagen)
            imagen_referencia2 = cv2.imread(ruta_imagen_validar)
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Verifica si las imágenes se cargaron correctamente
            if imagen_referencia is None or imagen_referencia2 is None or captura_pantalla_cv2 is None:
                raise ValueError("Error al cargar las imágenes.")

            # Obtén las dimensiones de las imágenes de referencia
            altura, ancho, _ = imagen_referencia.shape
            altura2, ancho2, _ = imagen_referencia2.shape

            # Encuentra la posición de ambas imágenes en la captura de pantalla
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            resultado2 = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia2, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
            min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(resultado2)

            # Define un umbral de confianza
            umbral_confianza = 0.8

            if max_val >= umbral_confianza or max_val2 >= umbral_confianza:
                if max_val >= umbral_confianza:
                    # Obtiene las coordenadas del centro de la imagen de referencia
                    centro_x = max_loc[0] + ancho // 2
                    centro_y = max_loc[1] + altura // 2
                    pyautogui.click(centro_x, centro_y)
                    time.sleep(1)

                if max_val2 >= umbral_confianza:
                    # Haz clic en el centro de la segunda imagen de referencia
                    cnac2_x = max_loc2[0] + ancho2 // 2
                    nav2_y = max_loc2[1] + altura2 // 2
                    pyautogui.click(cnac2_x, nav2_y)
                    pyautogui.write('F5')
                    time.sleep(2)

                    # Alterna entre navegadores si es necesario
                    #if self.navegador_actual == ruta_imagen_navegador1:
                    #    self.clickEnImagen(ruta_imagen_navegador2, 100)
                    #    self.navegador_actual = ruta_imagen_navegador2
                    #else:
                    #    self.clickEnImagen(ruta_imagen_navegador1, 100)
                    #    self.navegador_actual = ruta_imagen_navegador1

                    # Realiza una serie de operaciones después del clic
                    inicio = self.coordActual['text']
                    self.coordEnNav(inicio)
                    #self.recorte_Imagen(self.area_flecha_1)
                    
                    #texto_hasta_coma = self.detectar_direccion()
                    time.sleep(1)
                    self.moverEnDireccion(self.direccionActual)
                    time.sleep(1)
                    # Llamada recursiva solo si la imagen se encuentra
                    self.hintBox(ruta_imagen)

            else:
                print("Imagen no encontrada, intentando de nuevo...")
                time.sleep(1)
                self.hintBox(ruta_imagen)

        except Exception as e:
            print(f"Error en hintBox: {e}")

        finally:
            # Libera la memoria de las imágenes
            del imagen_referencia
            del imagen_referencia2
            del captura_pantalla_cv2

    def banderita(self, ruta_imagen):
        global intentos_realizados

        # Se hace un seguimiento de los intentos realizados
        intentos_realizados += 1

        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return

        try:
            # Carga la imagen de referencia y la captura de pantalla
            imagen_referencia = cv2.imread(ruta_imagen)
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Verifica si la imagen de referencia se cargó correctamente
            if imagen_referencia is None:
                raise ValueError(
                    f"No se pudo cargar la imagen de referencia: {ruta_imagen}")

            # Obtén las dimensiones de la imagen de referencia
            altura, ancho, _ = imagen_referencia.shape

            # Encuentra la posición de la imagen de referencia en la captura de pantalla
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Define un umbral de confianza
            umbral_confianza = 0.8

            if max_val >= umbral_confianza:
                # Obtiene las coordenadas del centro de la imagen de referencia
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2

                # Haz clic en el centro de la imagen encontrada (triple clic)
                pyautogui.tripleClick(centro_x, centro_y)
                self.numero_pista = self.numero_pista + 1

                # Realiza las acciones siguientes
                time.sleep(0.5)
                self.eliminar_chat()  # Elimina el chat después de hacer clic
                time.sleep(0.5)

                # Guarda una captura de pantalla
                imagen = pyautogui.screenshot()
                imagen.save(ruta_imagen_captura)
                time.sleep(1)
            else:
                print("Imagen no encontrada, intentando con otra bandera...")
                # Llamada recursiva controlada para buscar otra imagen
                self.banderita(ruta_imagen_banderita)

        except Exception as e:
            print(f"Error en banderita: {e}")

        finally:
            # Libera memoria
            del imagen_referencia
            del captura_pantalla_cv2

    def ha_llegado_destino(self, ruta_imagen):
        global intentos_realizados
        umbral_confianza = 0.8

        while intentos_realizados <= limite_intentos:
            # Incrementar el número de intentos
            intentos_realizados += 1

            # Leer la imagen de referencia
            imagen_referencia = cv2.imread(ruta_imagen)
            if imagen_referencia is None:
                print(
                    f"No se pudo cargar la imagen de referencia: {ruta_imagen}")
                return

            # Captura de pantalla usando pyautogui
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Procesar la comparación
            altura, ancho, _ = imagen_referencia.shape
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Si se encuentra la coincidencia con suficiente confianza
            if max_val >= umbral_confianza:
                # Ejecutar acción al encontrar el destino
                self.banderita(ruta_imagen_banderita)

                # Liberar memoria asociada con las imágenes
                del imagen_referencia, captura_pantalla_np, captura_pantalla_cv2, resultado
                cv2.destroyAllWindows()
                return  # Salir de la función si se encontró el destino

            else:
                # Pausa para reducir la carga en la CPU
                time.sleep(1)

            # Liberar memoria después de cada intento
            del imagen_referencia, captura_pantalla_np, captura_pantalla_cv2, resultado
            cv2.destroyAllWindows()

        # Si se alcanzó el límite de intentos
        print("Límite de intentos alcanzado. La imagen no se encontró.")

    def etapa_finalizada(self, ruta_imagen):
        global intentos_realizados
        try:
            # Incrementar los intentos realizados
            intentos_realizados += 1

            # Límite de intentos alcanzado
            if intentos_realizados > limite_intentos:
                print("Límite de intentos alcanzado. La imagen no se encontró.")
                return

            # Cargar la imagen de referencia
            imagen_referencia = cv2.imread(ruta_imagen)
            if imagen_referencia is None:
                raise FileNotFoundError(
                    f"No se pudo cargar la imagen de referencia desde: {ruta_imagen}")

            # Capturar la pantalla actual
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Obtener dimensiones de la imagen de referencia
            altura, ancho = imagen_referencia.shape[:2]

            # Realizar coincidencia de plantillas
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Definir un umbral de confianza
            umbral_confianza = 0.8
            print(f"Valor de coincidencia: {max_val}")

            if max_val >= umbral_confianza:
                # Obtener las coordenadas del centro de la imagen de referencia
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2

                # Hacer clic en el centro de la imagen encontrada
                pyautogui.click(centro_x, centro_y)

                # Pausa para evitar clicks rápidos
                time.sleep(1)

                # Resetear el contador de pistas y verificar la etapa
                self.numero_pista = 0
                self.capturaPantalla()
                self.checkEtapa()

                # Pausa adicional después de la verificación
                time.sleep(1)
            else:
                # Reintentar la búsqueda si la imagen no se encuentra
                print("Imagen no encontrada, reintentando...")
                self.etapa_finalizada(ruta_imagen)

        except Exception as e:
            print(f"Error en la verificación de la etapa: {e}")
            return

        finally:
            # Liberar recursos y limpiar la memoria
            del resultado, captura_pantalla_cv2, imagen_referencia
            gc.collect()
            cv2.destroyAllWindows()

    def lucha(self, ruta_imagen):
        global intentos_realizados
        try:
            # Incrementar el contador de intentos realizados
            intentos_realizados += 1

            # Verificar si se ha alcanzado el límite de intentos
            if intentos_realizados > limite_intentos:
                print("Límite de intentos alcanzado. La imagen no se encontró.")
                return

            # Cargar la imagen de referencia
            imagen_referencia = cv2.imread(ruta_imagen)
            if imagen_referencia is None:
                raise FileNotFoundError(
                    f"No se pudo cargar la imagen de referencia desde: {ruta_imagen}")

            # Capturar la pantalla actual
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Obtener las dimensiones de la imagen de referencia
            altura, ancho = imagen_referencia.shape[:2]

            # Realizar coincidencia de plantillas
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Definir un umbral de confianza
            umbral_confianza = 0.8
            print(f"Valor de coincidencia: {max_val}")

            if max_val >= umbral_confianza:
                # Calcular las coordenadas del centro de la imagen encontrada
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2

                # Hacer clic en el centro de la imagen encontrada
                pyautogui.click(centro_x, centro_y)
            else:
                # Si la imagen no se encuentra, reintentar la búsqueda
                print("Imagen de lucha no encontrada, reintentando...")
                self.lucha(ruta_imagen)

        except Exception as e:
            print(f"Error en la verificación de la lucha: {e}")
            return

        finally:
            # Liberar recursos y limpiar la memoria
            gc.collect()
            cv2.destroyAllWindows()

    def buscar_y_clickear_monstruo(self, ruta_imagen):
        global intentos_realizados
        global inBattle

        # Seguimiento de los intentos realizados
        intentos_realizados += 1

        # Límite de intentos alcanzado
        if intentos_realizados > limite_intentos:
            print("Límite de intentos alcanzado. La imagen no se encontró.")
            return False

        # Cargar las imágenes de referencia
        imagen_referencia = cv2.imread(ruta_imagen)
        imagen_referencia2 = cv2.imread(ruta_imagen_cerrar_bat)
        imagen_referencia3 = cv2.imread(ruta_imagen_subirLvl)

        if imagen_referencia is None or imagen_referencia2 is None or imagen_referencia3 is None:
            print("Error al cargar una o más imágenes de referencia.")
            return False

        try:
            # Captura la pantalla
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Obtener las dimensiones de las imágenes de referencia
            altura, ancho, _ = imagen_referencia.shape
            altura2, ancho2, _ = imagen_referencia2.shape
            altura3, ancho3, _ = imagen_referencia3.shape

            # Encontrar las posiciones de las imágenes de referencia en la captura de pantalla
            resultado = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            resultado2 = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia2, cv2.TM_CCOEFF_NORMED)
            resultado3 = cv2.matchTemplate(
                captura_pantalla_cv2, imagen_referencia3, cv2.TM_CCOEFF_NORMED)

            # Obtener los valores máximos de coincidencia
            _, max_val, _, max_loc = cv2.minMaxLoc(resultado)
            _, max_val2, _, max_loc2 = cv2.minMaxLoc(resultado2)
            _, max_val3, _, max_loc3 = cv2.minMaxLoc(resultado3)

            # Definir el umbral de confianza
            umbral_confianza = 0.8

            # Si se encuentra una coincidencia con suficiente confianza, realizar clic
            if max_val >= umbral_confianza or max_val2 >= umbral_confianza or max_val3 >= umbral_confianza:
                # Si es un monstruo
                if max_val >= umbral_confianza:
                    centro_x = max_loc[0] + ancho // 2
                    centro_y = max_loc[1] + altura // 2
                    pyautogui.tripleClick(centro_x, centro_y)

                # Si es cerrar batalla
                if max_val2 >= umbral_confianza:
                    inBattle = False
                    btX = max_loc2[0] + ancho2 // 2
                    btY = max_loc2[1] + altura2 // 2
                    pyautogui.click(btX, btY)

                # Si es subir de nivel
                if max_val3 >= umbral_confianza:
                    inBattle = False
                    lvlOkX = max_loc3[0] + ancho3 // 2
                    lvlOkY = max_loc3[1] + altura3 // 2
                    pyautogui.click(lvlOkX, lvlOkY)

                time.sleep(1)
                return True  # Imagen encontrada

            else:
                # Si no se encontró ninguna coincidencia, intenta otra acción
                self.buscar_y_clickear_monstruo(ruta_imagen)
                return False

        finally:
            # Liberar recursos de OpenCV
            del imagen_referencia, imagen_referencia2, imagen_referencia3, captura_pantalla_cv2
            gc.collect()  # Llamar al recolector de basura para limpiar memoria
            # Asegurarse de que cualquier ventana de OpenCV se cierre correctamente
            cv2.destroyAllWindows()

    # ----------------------------
    # Toma de Recursos
    # ----------------------------

    def buscar_recursos_y_click(self, carpeta_imagenes, escalas=[1.0, 0.9, 0.8, 0.7]):
        # Captura de pantalla antes de buscar las imágenes
        self.capturaPantalla()
        time.sleep(1)

        # Cargar la captura de pantalla
        img_grande = cv2.imread(ruta_imagen_captura, cv2.IMREAD_COLOR)

        # Definir un umbral para determinar si hay coincidencia
        umbral = 0.8

        # Iterar sobre las imágenes en la carpeta
        for imagen_nombre in os.listdir(carpeta_imagenes):
            ruta_imagen_a_buscar = os.path.join(
                carpeta_imagenes, imagen_nombre)
            img_fragmento = cv2.imread(ruta_imagen_a_buscar, cv2.IMREAD_COLOR)

            if img_fragmento is None:
                continue  # Ignorar archivos que no sean imágenes

            # Probar diferentes escalas de la imagen fragmento
            for escala in escalas:
                # Redimensionar la imagen fragmento según la escala
                ancho_escalado = int(img_fragmento.shape[1] * escala)
                alto_escalado = int(img_fragmento.shape[0] * escala)
                img_fragmento_escalado = cv2.resize(
                    img_fragmento, (ancho_escalado, alto_escalado))

                # Realizar la búsqueda de la imagen escalada
                resultado = cv2.matchTemplate(
                    img_grande, img_fragmento_escalado, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

                # Si la imagen se encuentra con un valor de coincidencia mayor al umbral
                if max_val >= umbral:
                    # Obtener el tamaño de la imagen buscada
                    altura, ancho = img_fragmento_escalado.shape[:2]

                    # Obtener la posición de la esquina superior izquierda donde se encuentra la imagen
                    top_left = max_loc

                    # Calcular el centro de la imagen para hacer clic
                    centro_x = top_left[0] + ancho // 2
                    centro_y = top_left[1] + altura // 2

                    # Hacer clic en el centro de la imagen encontrada
                    pyautogui.click(centro_x, centro_y)
                    print(
                        f"Imagen '{imagen_nombre}' encontrada en ({centro_x}, {centro_y}), realizando clic.")
                    return True  # Salir de la función al encontrar la primera coincidencia

        print("Ninguna imagen encontrada.")
        return False

    def recolectar_recurso(self, ruta_imagen_recurso, cantidad):
        recolectados = 0
        cantidad_recolectar = cantidad

        while recolectados <= cantidad_recolectar:
            self.buscar_recursos_y_click(ruta_imagen_recurso_hierro)
            print('buscando recurso')
            recolectados = recolectados + 1
            time.sleep(3)

    def iniciar_recoleccion(self):
        recurso = ruta_imagen_recurso_trigo
        self.recolectar_recurso(recurso, 100)

    # ----------------------------------#
    # ----------------------------------#
    # ----------------------------------#

    def startTreasureHunt(self):
        self.inicio_proceso = True
        limite_busqueda = 100
        contador_busquedas = 0
        #self.etapa_iniciada = True
        while contador_busquedas <= limite_busqueda:
            try:
                self.treasureHunt()
                contador_busquedas = contador_busquedas + 1
                print(f"Busquedas realizadas: {contador_busquedas}")
            except Exception as e:
                print(f"Error durante la busqueda {e}")

    def stopTreasureHunt(self):
        self.etapa_iniciada = False

    def treasureHunt(self):
        self.status_label.config(text="Iniciando búsqueda")

        try:
                # Obtener busqueda
                if not self.etapa_iniciada:
                    print('Obtener busqueda')
                    self.irACofreTesoros()
                    self.obtenerBusqueda()
                    # self.irACoordenadaMasCercana(nombre_cercano)
                self.capturaPantalla()
                self.checkPistas()      #Cantidad de pistas a realizar
                self.checkEtapa()       #Etapa actual
                self.checkGameCoord()   #Coordenada actual in-game    
                self.checkSalida()      #Salida de etapa actual
                # 
                etapa_actual_texto = self.etapaActual['text']
                etapa_actual_texto = self.cleanText(etapa_actual_texto)
                primer_numero, segundo_numero = etapa_actual_texto.split(',')
                primer_numero = int(primer_numero)
                segundo_numero = int(segundo_numero)

                salida_actual_texto = self.salida['text']
                salida_actual_texto = self.cleanText(salida_actual_texto)
                primer_coord, segundo_coord = salida_actual_texto.split(',')
                primer_coord = int(primer_coord)
                segundo_coord = int(segundo_coord)

                print(f"coordenada salida: {primer_coord}, {segundo_coord}")
                print(f"etapa actual: {primer_numero}, {segundo_numero}")
                print(f"Cantidad de pistas: {self.cantidadPistas['text']}")
                coordenada_cercana, nombre_cercano = coordenada_mas_cercana(primer_coord, segundo_coord, COORDENADAS_ZAAP)
                print(f"El zaap más cercano a la Salida es: {nombre_cercano}, {coordenada_cercana}")

                if (self.numero_pista == 0):  # primer_numero == 1 and
                    self.irACoordenadaMasCercana(nombre_cercano)

                    print(f"Salida: {self.salida['text']}")
                    print(f"Coordenada actual in-game: {self.coordActual['text']}")
                    if (f"{self.salida['text']}" != f"{self.coordActual['text']}"):
                        chatX, chatY = self.get4CoordFromText(self.chat['text'])
                        pyautogui.click(chatX, chatY)
                        time.sleep(1)
                        texto = self.salida['text']
                        if "('22', '-27')" in texto:
                            pyautogui.write('/travel 23 -27')
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            self.clickEnImagen(
                                ruta_imagen_llegado_destino, 1000)
                            time.sleep(1)
                            self.eliminar_chat()
                            time.sleep(1)
                        if "('21', '-37')" in texto:
                            pyautogui.write('/travel 20 -32')
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            self.clickEnImagen(
                                ruta_imagen_llegado_destino, 1000)
                            time.sleep(1)
                            self.eliminar_chat()
                            time.sleep(1)
                        if "('20', '39')" in texto:
                            pyautogui.write('/travel 22 37')
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            self.clickEnImagen(
                                ruta_imagen_llegado_destino, 1000)
                            time.sleep(1)
                            self.eliminar_chat()
                            time.sleep(1)

                        pyautogui.tripleClick(chatX, chatY)
                        time.sleep(1)

                        if (f"{self.salida['text']}" != f"{self.coordActual['text']}"):
                            pyautogui.write(f"/travel {primer_coord} {segundo_coord}")
                            time.sleep(1)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            self.clickEnImagen(ruta_imagen_llegado_destino, 1000)
                            time.sleep(1)
                        self.eliminar_chat()
                        time.sleep(1)
                        self.checkGameCoord()

                while primer_numero < segundo_numero and self.etapa_iniciada:  # Mientras la condición sea verdadera
                    self.capturaPantalla()
                    self.reset = False #Para resetear busqueda
                    self.checkPistas()
                    self.verificacionPistas()
                    primer_numero += 1  # Actualiza la condición para evitar un bucle infinito
                    time.sleep(1)

                if self.etapa_iniciada == True:
                    time.sleep(1)
                    self.lucha(ruta_imagen_lucha)
                    time.sleep(2)
                    self.pelea()
                    # time.sleep(6)
                self.etapa_iniciada = False
                self.numero_pista = 0
                self.save_to_text_file()
                time.sleep(2)
                # pyautogui.press('enter')
                pyautogui.press('enter')
                # self.clickEnImagen(ruta_imagen_cerrar_bat)
                self.status_label.config(text=f"Búsqueda terminada")
                # pyautogui.press('0')

        except Exception as e:
                print(f"Error: {e}")
                print("El programa is dead, vamos a limpiar")
                print("Limpiando")
                cv2.destroyAllWindows()
                self.restablecerEtapa()

        finally:
                # Cerrar ventanas y liberar recursos aquí
                cv2.destroyAllWindows()
                #self.load_from_text_file()  # Si es necesario restaurar datos

        # Vuelve a programar la tarea para evitar recursión infinita
        #threading.Timer(3, self.startTreasureHunt).start()  # Repetir después de 3 segundos
    
    def checkBattle(self):
        try:
            self.capturaPantalla()
            time.sleep(1)
            mobX, mobY = self.checkCoordMob(10)
            cantidad, cuadroLejano = self.getCantidadImagen(ruta_imagen_rojo, mobX, mobY)
            clX, clY, clAn, clAl = cuadroLejano
            
            # Calcular el centro de la imagen
            centroX = clX + clAn // 2
            centroY = clY + clAl // 2
            
            #click en el cuadro rojo mas lejano al mob
            pyautogui.click(centroX, centroY)
            
        except Exception as e:
            print(f"Error: {e} no se pudo chequear la batalla")
            return
    #----------------------------#
    #-----------BATTLE-----------#
    #----------------------------#
    def checkImagenEnCaptura(self, ruta_imagen, cantidad):
        # Seguimiento de los intentos realizados
        intentos_realizados = 0

        while intentos_realizados < cantidad:
            try:
                # Incrementar los intentos realizados
                intentos_realizados += 1

                # Carga la imagen de referencia y la captura de pantalla
                imagen_referencia = cv2.imread(ruta_imagen)
                captura_pantalla = pyautogui.screenshot()
                captura_pantalla_np = np.array(captura_pantalla)
                captura_pantalla_cv2 = cv2.cvtColor(
                    captura_pantalla_np, cv2.COLOR_RGB2BGR)

                # Verifica que las imágenes se hayan cargado correctamente
                if imagen_referencia is None or captura_pantalla_cv2 is None:
                    raise ValueError("Error al cargar las imágenes.")

                # Obtén las dimensiones de la imagen de referencia
                altura, ancho, _ = imagen_referencia.shape

                # Encuentra la posición de la imagen de referencia en la captura de pantalla
                resultado = cv2.matchTemplate(
                    captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

                # Define un umbral de confianza (ajusta según tus necesidades)
                umbral_confianza = float(self.umbral.get())
                print(f"Valor de coincidencia: {max_val}")

                if max_val >= umbral_confianza:
                    # Obtiene las coordenadas del centro de la imagen de referencia
                    centro_x = max_loc[0] + ancho // 2
                    centro_y = max_loc[1] + altura // 2

                    # Haz clic en el centro de la imagen encontrada
                    #pyautogui.click(centro_x, centro_y)
                    #print(f"Clic realizado en ({centro_x}, {centro_y})")
                    #time.sleep(1)
                    print(f"Imagen {ruta_imagen} encontrada")
                    return centro_x, centro_y

                    # Libera la memoria de las imágenes antes de salir
                    #del imagen_referencia
                    #del captura_pantalla_cv2
                    #return  # Salir de la función después de hacer clic exitosamente

                else:
                    print("Imagen no encontrada, intentando de nuevo...")
                    # Añadir un pequeño retraso antes de reintentar
                    time.sleep(1)
                    return None


            except Exception as e:
                print(f"Error en clickEnImagen: {e}")
                break  # Salir del bucle si hay un error crítico

        raise RuntimeError(
            "Límite de intentos alcanzado o error crítico, no se encontró la imagen.")
    
    def checkCoordMob(self, cantidad):
        # Se hace un seguimiento de los intentos realizados
        intentos_realizados = 0

        # Límite de intentos alcanzado
        while intentos_realizados < cantidad:
            
            # Lista de rutas alternativas de imágenes
            rutas_alternativas = [
                "./treasureHunt/battle/1.png",
                './treasureHunt/battle/2.png',
                './treasureHunt/battle/3.png',
                './treasureHunt/battle/4.png'
            ]

            # Captura la pantalla completa solo una vez
            x1, y1, x2, y2 = 330, 50, 1580, 900
            captura_pantalla = pyautogui.screenshot(
                region=(x1, y1, x2 - x1, y2 - y1))
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(
                captura_pantalla_np, cv2.COLOR_RGB2BGR)

            time.sleep(3)

            # Iterar sobre las rutas alternativas de las imágenes
            for ruta_alternativa in rutas_alternativas:
                imagen_referencia = cv2.imread(ruta_alternativa)

                if imagen_referencia is not None:
                    # Obtén las dimensiones de la imagen de referencia
                    altura, ancho, _ = imagen_referencia.shape

                    # Encuentra la posición de la imagen de referencia en la captura de pantalla
                    resultado = cv2.matchTemplate(
                        captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

                    # Define un umbral de confianza (puedes ajustar según tus necesidades)
                    umbral_confianza = 0.8
                    print(f"Confianza: {max_val} en la ruta: {ruta_alternativa}")

                    if max_val >= umbral_confianza:
                        print(f"Imagen encontrada en la ruta: {ruta_alternativa}")

                        # Realiza el clic en la imagen
                        #self.clickEnImagen(ruta_imagen_maxBusqueda, 100)
                        #time.sleep(2)
                        centro_x = max_loc[0] + ancho // 2
                        centro_y = max_loc[1] + altura // 2
                        print(f"Ubicacion de mon: {centro_x}, {centro_y}")
                        # Llama a la función banderita
                        #self.banderita(ruta_imagen_banderita)
                        # self.checkGameCoord()
                        # Termina el bucle ya que se encontró y clickeó una imagen
                        return centro_x, centro_y
                else:
                    print(f"Error al cargar la imagen de la ruta: {ruta_alternativa}")
            
            # Incrementar intentos después de cada intento fallido
            intentos_realizados += 1
            print(f"Intentos realizados: {intentos_realizados}/{cantidad}")
        
        # Si no se encontró nada tras todos los intentos
        print("No se encontró ninguna coincidencia tras todos los intentos.")
        return None, None
    
    def getCantidadImagen(self, ruta_imagen, mobX, mobY):
        try:
            # Cargar la imagen de la captura de pantalla
            captura_pantalla = cv2.imread(ruta_imagen_captura)
            if captura_pantalla is None:
                raise ValueError(f"No se pudo cargar la imagen de captura de pantalla desde {ruta_imagen_captura}")

            # Cargar la imagen de referencia (el cuadro rojo)
            referencia = cv2.imread(ruta_imagen)
            if referencia is None:
                raise ValueError(f"No se pudo cargar la imagen de referencia desde {ruta_imagen}")

            # Obtener las dimensiones de la imagen de referencia
            h, w = referencia.shape[:2]

            # Buscar la imagen de referencia en la captura de pantalla
            resultado = cv2.matchTemplate(captura_pantalla, referencia, cv2.TM_CCOEFF_NORMED)

            # Definir un umbral de confianza
            umbral_confianza = 0.8
            ubicaciones = np.where(resultado >= umbral_confianza)

            # Convertir ubicaciones a una lista de coordenadas
            ubicaciones = list(zip(*ubicaciones[::-1]))

            if len(ubicaciones) == 0:
                print(f"No se encontraron coincidencias para {ruta_imagen}.")
                return 0

            # Crear rectángulos a partir de las ubicaciones para usar groupRectangles
            rectangulos = [(*pt, w, h) for pt in ubicaciones]

            # Aplicar groupRectangles para eliminar duplicados cercanos
            rectangulos, _ = cv2.groupRectangles(rectangulos, groupThreshold=1, eps=0.5)

            # Contar las ocurrencias que coinciden exactamente en tamaño
            cantidad_ocurrencias = 0
            coincidencia_mas_lejana = None
            max_distancia = -1

            for (x, y, w_encontrado, h_encontrado) in rectangulos:
                # Verificar si las dimensiones coinciden con la referencia
                if w_encontrado == w and h_encontrado == h:
                    cantidad_ocurrencias += 1
                    
                    # Calcular la distancia desde mobX, mobY
                    distancia = calcular_distancia(mobX, mobY, x, y)
                    
                    # Si es la distancia más lejana encontrada hasta ahora
                    if distancia > max_distancia:
                        max_distancia = distancia
                        coincidencia_mas_lejana = (x, y, w_encontrado, h_encontrado)

            if coincidencia_mas_lejana:
                print(f"Coordenadas más lejanas: {coincidencia_mas_lejana} a distancia: {max_distancia}")
            else:
                print(f"No se encontraron coincidencias con el tamaño exacto.")

            return cantidad_ocurrencias, coincidencia_mas_lejana

        except Exception as e:
            print(f"Error al procesar las imágenes: {e}")
            return 0

        finally:
            # Liberar recursos para evitar acumulación de memoria
            captura_pantalla = None
            referencia = None
            resultado = None
            ubicaciones = None
            rectangulos = None
            gc.collect()  # Llamar al recolector de basura para limpiar memoria
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # root = Tk()
    app = ImageFinderApp()
    app.run()
    # root.mainloop()
