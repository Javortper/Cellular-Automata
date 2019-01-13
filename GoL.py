# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:31:19 2018

@author: Javi, Fabio_
"""
import pygame

screen = pygame.display.set_mode((640,480))
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GRAY = (156,156,156)
PAUSE = 1

WIDTH = 8
HEIGHT = 8
MARGIN = 1
WINDOW_CTE = WIDTH + MARGIN
EXTRA_WINDOW = 400
BORRAR = False
UNA_ITERACION = False
PAUSA_STR = "Pausado"
ITERACIONES = 0
POBLACION = 0

print("Introducir dimensión (recomendado: 60)")
DIMENSION = int(input())
REGLAS = []
print("¿Cúantos vecinos para que nazca una célula?")
REGLAS.append(int(input()))
print("¿Cúantos vecinos para que viva una célula? (introducir dos números, primer número (enter) segundo número)")
REGLAS.append(int(input()))

REGLAS.append(int(input()))
tablero = []
for row in range(DIMENSION):
    tablero.append([])
    for column in range(DIMENSION):
        tablero[row].append(0)

pygame.init()

WINDOW_SIZE = [WINDOW_CTE*DIMENSION + EXTRA_WINDOW, WINDOW_CTE*DIMENSION]
print(WINDOW_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")
done = False
clock = pygame.time.Clock()

# -------- Texto -----------
pygame.font.init()
FONT_CABECERA = pygame.font.SysFont('Arial',50)
FONT_START = pygame.font.SysFont('Arial',15)
FONT_AUTORES = pygame.font.SysFont('Arial',15)
TEXT_CABECERA = FONT_CABECERA.render('Game of Life', True, WHITE)
INFO_TEXT1 = FONT_START.render("Pulsa espacio para reanudar/pausar el juego.", True, WHITE)
INFO_TEXT3 = FONT_START.render("Con el juego en pausa, pulsa R para reiniciar el juego.", True, WHITE)
INFO_TEXT4 = FONT_START.render("Con el juego en pausa, pulsa S para realizar una iteración.", True, WHITE)
INFO_TEXT2 = FONT_START.render("REGLAS DEL JUEGO: " +"B"+str(REGLAS[0])+"/S"+str(REGLAS[1])+str(REGLAS[2]), True, WHITE)
BLINKER_TEXT = FONT_START.render("Tecla 1: Blinker", True, WHITE)
BACON_TEXT = FONT_START.render("Tecla 2: Bacon", True, WHITE)
TOAD_TEXT = FONT_START.render("Tecla 3: Toad", True, WHITE)
DIRTYPUFFER_TEXT = FONT_START.render("Tecla 4: Dirty Puffer", True, WHITE)
GLIDER_TEXT = FONT_START.render("Tecla 5: Glider", True, WHITE)
LWSS_TEXT = FONT_START.render("Tecla 6: Lwss", True, WHITE)
CLEANPUFFER_TEXT = FONT_START.render("Tecla 7: Clean Puffer", True, WHITE)
C5SPACESHIP_TEXT = FONT_START.render("Tecla 8: C5 Space Ship", True, WHITE)
GLIDERGUN_TEXT = FONT_START.render("Tecla 9: Glinder Gun", True, WHITE)
PULSAR_TEXT = FONT_START.render("Tecla 0: Pulsar", True, WHITE)
PAUSA_TEXT = FONT_START.render("El juego está actualmente: " +PAUSA_STR, True, WHITE)
ITERA_TEXT = FONT_START.render("Número de iteraciones: " + str(ITERACIONES), True, WHITE)
POBLACION_TEXT = FONT_START.render("Población" + str(POBLACION), True, WHITE)
AUTORES_TEXT = FONT_AUTORES.render("Proyecto realizado por Fabio Rodríguez Macías y Javier Ortiz Pérez", True, WHITE)
AUTORES_TEXT2 = FONT_AUTORES.render("Matemáticas para la Computación", True, WHITE)
AUTORES_TEXT3 = FONT_AUTORES.render("Universidad de Sevilla", True, WHITE)
AUTORES_TEXT4 = FONT_AUTORES.render("Grado en Ingeniería Informática - Tecnologías Informáticas", True, WHITE)
AUTORES_TEXT5 = FONT_AUTORES.render("Curso 2018/2019", True, WHITE)









def listener(tablero): #Está a la escucha del raton
    global PAUSE
    global UNA_ITERACION
    global BORRAR
    global PAUSA_STR
    global PAUSA_TEXT
    for event in pygame.event.get():  # usuario hace algo
        if event.type == pygame.QUIT:  # si el usuario hace click, cierra
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]: #Se ejecuta cada vez que se clicka
            pos = pygame.mouse.get_pos()
            if pos[0] < WINDOW_CTE*DIMENSION:
            # Cambiamos las coordenadas x/y por las del tablero
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
            # ponemos esta posición en 1
                if PAUSE == 1:
                    tablero[row][column] = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if PAUSE==0:
                PAUSA_STR = "Pausado"
                PAUSA_TEXT = FONT_START.render("El juego está actualmente: " +PAUSA_STR, True, WHITE)
                PAUSE = 1
                print(PAUSA_STR)
            elif PAUSE == 1:
                PAUSA_STR = "En ejecución"
                PAUSA_TEXT = FONT_START.render("El juego está actualmente: " + PAUSA_STR, True, WHITE)
                PAUSE = 0
                print(PAUSA_STR)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and PAUSE == 1:
            BORRAR = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1 and PAUSE == 1:
            crearBlinker(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2 and PAUSE == 1:
            crearBacon(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3 and PAUSE == 1:
            crearToad(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_4 and PAUSE == 1:
            crearDirtyPuffer(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_5 and PAUSE == 1:
            crearGlider(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_6 and PAUSE == 1:
            crearLWSS(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_7 and PAUSE == 1:
            crearCleanPuffer(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_8 and PAUSE == 1:
            crearC5spaceship(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_9 and PAUSE == 1:
            crearGliderGun(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_0 and PAUSE == 1:
            crearPulsar(int(DIMENSION/2),int(DIMENSION/2))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and PAUSE == 1:
            UNA_ITERACION = True

def dibujado(tablero_vacio): # Colorea las celulas vivas
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = BLACK
            if tablero_vacio[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

def iteracion(tablero, tablero_vacio): # Se modifica el tablero según las reglas del juego pero no se dibuja
    for row in range(len(tablero_vacio)):
        for column in range(len(tablero_vacio)):
            try:
                vecinos_vivos = contar_vecinos(tablero, row, column)
                celula = tablero[row][column]
                if celula == 1:
                    if (vecinos_vivos > REGLAS[2]) or (vecinos_vivos < REGLAS[1]):
                        tablero_vacio[row][column] = 0
                    else:
                        tablero_vacio[row][column] = 1
                else:
                    if vecinos_vivos == REGLAS[0]:
                        tablero_vacio[row][column] = 1
            except:
                pass

    return tablero_vacio

def contar_vecinos_clasico(tablero, x, y):
    vecinos = [[x-1, y-1], [x-1, y], [x-1, y+1],
               [x, y-1],             [x, y+1],
               [x+1, y-1], [x+1, y], [x+1, y+1]]
    vecinos_vivos = 0
    for vecino in vecinos:
            if tablero[vecino[0]][vecino[1]] == 1:
                vecinos_vivos = vecinos_vivos + 1
    return vecinos_vivos

def contar_vecinos(tablero,x,y):
    vecinos_vivos = 0
    vecinos = [[x, (y - 1) % DIMENSION], [x, (y + 1) % DIMENSION], [(x - 1) % DIMENSION, y], [(x + 1) % DIMENSION, y],
               [(x - 1) % DIMENSION, (y - 1) % DIMENSION], [(x - 1) % DIMENSION, (y + 1) % DIMENSION],
               [(x + 1) % DIMENSION, (y - 1) % DIMENSION], [(x + 1) % DIMENSION, (y + 1) % DIMENSION]]
    for vecino in vecinos:
        if tablero[vecino[0]][vecino[1]] == 1:
            vecinos_vivos = vecinos_vivos + 1
    return vecinos_vivos

def contador_poblacion(tablero):
    cont = 0
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if tablero[i][j] == 1:
                cont += 1
    return cont

def tablero_vacio():
    tablero_vacio = []
    for r in range(DIMENSION):
        row = []
        for c in range(DIMENSION):
            row.append(0)
        tablero_vacio.append(row)
    return tablero_vacio

# -------------------- CREACIÓN DE FIGURAS --------------------
def crearBlinker(x,y):
    tablero[x][y] = True
    tablero[x][y-1] = True
    tablero[x][y + 1] = True
    return tablero

def crearBacon(x, y):
    tablero[x][y] = True
    tablero[x+1][y] = True
    tablero[x][y+1] = True
    tablero[x+1][y+1] = True
    tablero[x-1][y-1] = True
    tablero[x-2][y-1] = True
    tablero[x-1][y-2] = True
    tablero[x-2][y-2] = True
    return tablero

def crearToad(x, y):
    tablero[x][y] = True
    tablero[x+1][y] = True
    tablero[x-1][y] = True
    tablero[x][y-1] = True
    tablero[x+1][y-1] = True
    tablero[x+2][y-1] = True
    return tablero

def crearDirtyPuffer(x, y):
    # arriba
    tablero[x][y - 6] = True
    tablero[x - 1][y - 6] = True
    tablero[x + 1][y - 6] = True
    tablero[x + 2][y - 6] = True
    tablero[x - 2][y - 7] = True
    tablero[x + 2][y - 7] = True
    tablero[x + 2][y - 8] = True
    tablero[x + 1][y - 9] = True
    # medio
    tablero[x][y] = True
    tablero[x][y + 1] = True
    tablero[x][y - 1] = True
    tablero[x - 1][y + 2] = True
    tablero[x - 1][y - 1] = True
    tablero[x - 2][y - 2] = True
    # abajo
    tablero[x][y + 8] = True
    tablero[x - 1][y + 8] = True
    tablero[x + 1][y + 8] = True
    tablero[x + 2][y + 8] = True
    tablero[x + 2][y + 7] = True
    tablero[x + 2][y + 6] = True
    tablero[x + 1][y + 5] = True
    tablero[x - 2][y + 7] = True

    return tablero

def crearGlider(x, y):
    tablero[x - 1][y - 1] = True
    tablero[x][y] = True
    tablero[x + 1][y] = True
    tablero[x][y + 1] = True
    tablero[x - 1][y + 1] = True
    return tablero

def crearLWSS(x, y):
    tablero[x][y] = True
    tablero[x - 1][y] = True
    tablero[x - 2][y - 1] = True
    tablero[x + 1][y] = True
    tablero[x + 2][y] = True
    tablero[x + 2][y - 1] = True
    tablero[x + 2][y - 2] = True
    tablero[x + 1][y - 3] = True
    tablero[x - 2][y - 3] = True
    return tablero

def crearCleanPuffer(x, y):
    # bottom part
    tablero[x][y] = True
    tablero[x][y + 1] = True
    tablero[x + 1][y + 1] = True
    tablero[x - 1][y + 2] = True
    tablero[x][y + 2] = True
    tablero[x + 1][y + 2] = True
    tablero[x + 2][y + 2] = True
    tablero[x - 1][y + 3] = True
    tablero[x][y + 3] = True
    tablero[x + 2][y + 3] = True
    tablero[x + 3][y + 3] = True
    tablero[x + 1][y + 4] = True
    tablero[x + 2][y + 4] = True
    # top part
    tablero[x - 2][y - 1] = True
    tablero[x + 2][y - 1] = True
    tablero[x - 6][y - 2] = True
    tablero[x - 5][y - 2] = True
    tablero[x - 3][y - 2] = True
    tablero[x + 3][y - 2] = True
    tablero[x - 4][y - 3] = True
    tablero[x - 3][y - 3] = True
    tablero[x + 3][y - 3] = True
    tablero[x - 2][y - 4] = True
    tablero[x - 1][y - 4] = True
    tablero[x][y - 4] = True
    tablero[x + 1][y - 4] = True
    tablero[x + 2][y - 4] = True
    tablero[x + 3][y - 4] = True

    return tablero

def crearC5spaceship(x, y):
    # medio
    tablero[x - 1][y] = True
    tablero[x - 1][y - 1] = True
    tablero[x - 1][y + 1] = True
    tablero[x + 1][y] = True
    tablero[x + 1][y - 1] = True
    tablero[x + 1][y + 1] = True
    # izq
    tablero[x - 2][y - 3] = True
    tablero[x - 3][y - 3] = True
    tablero[x - 4][y - 4] = True
    tablero[x - 5][y - 3] = True
    tablero[x - 5][y - 2] = True
    tablero[x - 6][y - 2] = True
    tablero[x - 7][y - 2] = True
    tablero[x - 7][y - 1] = True
    tablero[x - 7][y - 3] = True
    tablero[x - 8][y] = True
    tablero[x - 8][y + 2] = True
    tablero[x - 8][y + 3] = True
    tablero[x - 9][y] = True
    tablero[x - 9][y + 2] = True
    tablero[x - 9][y - 1] = True
    tablero[x - 9][y - 2] = True
    tablero[x - 9][y - 3] = True
    tablero[x - 10][y - 3] = True
    tablero[x - 11][y - 2] = True
    tablero[x - 11][y + 1] = True
    tablero[x - 11][y + 2] = True
    tablero[x - 12][y - 2] = True
    tablero[x - 12][y + 1] = True
    tablero[x - 12][y + 2] = True
    tablero[x - 13][y - 1] = True
    tablero[x - 13][y - 2] = True
    # der
    tablero[x + 2][y - 3] = True
    tablero[x + 3][y - 3] = True
    tablero[x + 4][y - 4] = True
    tablero[x + 5][y - 3] = True
    tablero[x + 5][y - 2] = True
    tablero[x + 6][y - 2] = True
    tablero[x + 7][y - 2] = True
    tablero[x + 7][y - 1] = True
    tablero[x + 7][y - 3] = True
    tablero[x + 8][y] = True
    tablero[x + 8][y + 2] = True
    tablero[x + 8][y + 3] = True
    tablero[x + 9][y] = True
    tablero[x + 9][y + 2] = True
    tablero[x + 9][y - 1] = True
    tablero[x + 9][y - 2] = True
    tablero[x + 9][y - 3] = True
    tablero[x + 10][y - 3] = True
    tablero[x + 11][y - 2] = True
    tablero[x + 11][y + 1] = True
    tablero[x + 11][y + 2] = True
    tablero[x + 12][y - 2] = True
    tablero[x + 12][y + 1] = True
    tablero[x + 12][y + 2] = True
    tablero[x + 13][y - 1] = True
    tablero[x + 13][y - 2] = True

    return tablero

def crearGliderGun(x, y):
    # izq
    tablero[x][y] = True
    tablero[x + 1][y - 2] = True
    tablero[x + 1][y + 2] = True
    tablero[x + 2][y] = True
    tablero[x + 2][y - 1] = True
    tablero[x + 2][y + 1] = True
    tablero[x + 3][y] = True
    tablero[x - 1][y + 3] = True
    tablero[x - 1][y - 3] = True
    tablero[x - 2][y + 3] = True
    tablero[x - 2][y - 3] = True
    tablero[x - 3][y - 2] = True
    tablero[x - 3][y + 2] = True
    tablero[x - 4][y] = True
    tablero[x - 4][y - 1] = True
    tablero[x - 4][y + 1] = True
    tablero[x - 13][y] = True
    tablero[x - 13][y - 1] = True
    tablero[x - 14][y] = True
    tablero[x - 14][y - 1] = True
    # der
    tablero[x + 6][y - 1] = True
    tablero[x + 6][y - 2] = True
    tablero[x + 6][y - 3] = True
    tablero[x + 7][y - 1] = True
    tablero[x + 7][y - 2] = True
    tablero[x + 7][y - 3] = True
    tablero[x + 8][y - 4] = True
    tablero[x + 8][y] = True
    tablero[x + 10][y - 4] = True
    tablero[x + 10][y - 5] = True
    tablero[x + 10][y] = True
    tablero[x + 10][y + 1] = True
    tablero[x + 20][y - 2] = True
    tablero[x + 20][y - 3] = True
    tablero[x + 21][y - 2] = True
    tablero[x + 21][y - 3] = True

    return tablero

def crearPulsar(x, y):
    # izq
    tablero[x - 1][y - 2] = True
    tablero[x - 1][y - 3] = True
    tablero[x - 1][y + 2] = True
    tablero[x - 1][y + 3] = True
    tablero[x - 2][y - 1] = True
    tablero[x - 2][y - 3] = True
    tablero[x - 2][y - 5] = True
    tablero[x - 2][y + 1] = True
    tablero[x - 2][y + 3] = True
    tablero[x - 2][y + 5] = True
    tablero[x - 3][y - 1] = True
    tablero[x - 3][y - 2] = True
    tablero[x - 3][y - 5] = True
    tablero[x - 3][y - 6] = True
    tablero[x - 3][y - 7] = True
    tablero[x - 3][y + 1] = True
    tablero[x - 3][y + 2] = True
    tablero[x - 3][y + 5] = True
    tablero[x - 3][y + 6] = True
    tablero[x - 3][y + 7] = True
    tablero[x - 5][y - 2] = True
    tablero[x - 5][y - 3] = True
    tablero[x - 5][y + 2] = True
    tablero[x - 5][y + 3] = True
    tablero[x - 6][y - 3] = True
    tablero[x - 6][y + 3] = True
    tablero[x - 7][y - 3] = True
    tablero[x - 7][y + 3] = True
    # der
    tablero[x + 1][y - 2] = True
    tablero[x + 1][y - 3] = True
    tablero[x + 1][y + 2] = True
    tablero[x + 1][y + 3] = True
    tablero[x + 2][y - 1] = True
    tablero[x + 2][y - 3] = True
    tablero[x + 2][y - 5] = True
    tablero[x + 2][y + 1] = True
    tablero[x + 2][y + 3] = True
    tablero[x + 2][y + 5] = True
    tablero[x + 3][y - 1] = True
    tablero[x + 3][y - 2] = True
    tablero[x + 3][y - 5] = True
    tablero[x + 3][y - 6] = True
    tablero[x + 3][y - 7] = True
    tablero[x + 3][y + 1] = True
    tablero[x + 3][y + 2] = True
    tablero[x + 3][y + 5] = True
    tablero[x + 3][y + 6] = True
    tablero[x + 3][y + 7] = True
    tablero[x + 5][y - 2] = True
    tablero[x + 5][y - 3] = True
    tablero[x + 5][y + 2] = True
    tablero[x + 5][y + 3] = True
    tablero[x + 6][y - 3] = True
    tablero[x + 6][y + 3] = True
    tablero[x + 7][y - 3] = True
    tablero[x + 7][y + 3] = True

    return tablero

# -------------------------------------------------------------



# -------------------------- BUCLE PRINCIPAL DEL PROGRAMA -----------------------------
while not done:
    listener(tablero)  # Está a la escucha de los clicks
    # Color del fondo
    screen.fill(BLACK)
    # ------------------  DIBUJADO -------------------------------
    screen.blit(TEXT_CABECERA, (100 + WINDOW_CTE * DIMENSION, 25))
    screen.blit(INFO_TEXT1, (50 + WINDOW_CTE * DIMENSION, 100))
    screen.blit(INFO_TEXT3, (50 + WINDOW_CTE * DIMENSION, 110))
    screen.blit(INFO_TEXT4, (50 + WINDOW_CTE * DIMENSION, 120))
    screen.blit(INFO_TEXT2, (50 + WINDOW_CTE * DIMENSION, 140))
    screen.blit(BLINKER_TEXT, (50 + WINDOW_CTE * DIMENSION, 160))
    screen.blit(BACON_TEXT, (50 + WINDOW_CTE * DIMENSION, 170))
    screen.blit(TOAD_TEXT, (50 + WINDOW_CTE * DIMENSION, 180))
    screen.blit(DIRTYPUFFER_TEXT, (50 + WINDOW_CTE * DIMENSION, 190))
    screen.blit(GLIDER_TEXT, (50 + WINDOW_CTE * DIMENSION, 200))
    screen.blit(LWSS_TEXT, (50 + WINDOW_CTE * DIMENSION, 210))
    screen.blit(CLEANPUFFER_TEXT, (50 + WINDOW_CTE * DIMENSION, 220))
    screen.blit(C5SPACESHIP_TEXT, (50 + WINDOW_CTE * DIMENSION, 230))
    screen.blit(GLIDERGUN_TEXT, (50 + WINDOW_CTE * DIMENSION, 240))
    screen.blit(PULSAR_TEXT, (50 + WINDOW_CTE * DIMENSION, 250))
    screen.blit(PAUSA_TEXT, (50 + WINDOW_CTE * DIMENSION, 280))
    screen.blit(ITERA_TEXT, (50 + WINDOW_CTE * DIMENSION, 290))
    screen.blit(POBLACION_TEXT, (50 + WINDOW_CTE * DIMENSION, 300))
    screen.blit(AUTORES_TEXT, (50 + WINDOW_CTE * DIMENSION, 340))
    screen.blit(AUTORES_TEXT2, (50 + WINDOW_CTE * DIMENSION, 350))
    screen.blit(AUTORES_TEXT4, (50 + WINDOW_CTE * DIMENSION, 360))
    screen.blit(AUTORES_TEXT3, (50 + WINDOW_CTE * DIMENSION, 370))
    screen.blit(AUTORES_TEXT5, (50 + WINDOW_CTE * DIMENSION, 380))


    # ------------------------------------------------------------

    # ----------------------- JUEGO DE LA VIDA ------------------------
    if PAUSE == 0 :
        ITERACIONES += 1
        ITERA_TEXT = FONT_START.render("Número de iteraciones: " + str(ITERACIONES), True, WHITE)
        siguiente_gen = tablero_vacio() #Creamos un tablero vacio
        generar_siguiente_generacion = iteracion(tablero, siguiente_gen) #En el tablero vacio generamos la siguiente generacion.
        dibujado(generar_siguiente_generacion) #Dibujamos la pantalla según el nuevo tablero
        tablero = generar_siguiente_generacion #Ponemos el tablero base como la nueva generación
        POBLACION = contador_poblacion(tablero)
        POBLACION_TEXT = FONT_START.render("Población: " + str(POBLACION), True, WHITE)

    if PAUSE == 1:
        POBLACION = contador_poblacion(tablero)
        POBLACION_TEXT = FONT_START.render("Población: " + str(POBLACION), True, WHITE)
        if BORRAR:
            ITERACIONES = 0
            ITERA_TEXT = FONT_START.render("Número de iteraciones: " + str(ITERACIONES), True, WHITE)
            tablero = tablero_vacio()
            dibujado(tablero)
            BORRAR = False
        if UNA_ITERACION:
            ITERACIONES += 1
            ITERA_TEXT = FONT_START.render("Número de iteraciones: " +str(ITERACIONES), True, WHITE)
            siguiente_gen = tablero_vacio()  # Creamos un tablero vacio
            generar_siguiente_generacion = iteracion(tablero, siguiente_gen)  # En el tablero vacio generamos la siguiente generacion.
            dibujado(generar_siguiente_generacion)  # Dibujamos la pantalla según el nuevo tablero
            tablero = generar_siguiente_generacion  # Ponemos el tablero base como la nueva generación
            UNA_ITERACION = False

        dibujado(tablero)
    # -----------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

    clock.tick(60) #fps
    pygame.display.flip()  # actualizamos con lo que hemos dibujado
pygame.quit()