#PONER PYTHON 3.12
#TENER LA CARPETA QUE CONTIENE EL JUEGO.PY ABIERTO EN VSC
#CORRER POR TERMINAL
from random import randint
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Lib'))
import pgzrun# type: ignore
import pygame# type: ignore
from Enemigos_clase import Monstruo
# py -m pip install pygame
# py -m pip install pgzero
import pgzero.game as pgzero_game  # type: ignore
dificultad = 3

os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
TITLE = "FIVE NIGHTS AT E-45"
reloj = pygame.time.Clock()
#Esta variables definen el tamaño de la ventana del juego.
RESOLUCION = 720

ANCHO = round(RESOLUCION*1.77777777778)
ALTO = RESOLUCION
WIDTH = ANCHO
HEIGHT = ALTO
CENTRO_X = ANCHO / 2 # Coordenada X del centro de la pantalla
CENTRO_Y = ALTO / 2  # Coordenada Y del centro de la pantalla
#-------------------------DIFICULTAD
Switch_timer = 0
switchs_encendidos = 0

Enemigo_Switch1 = Monstruo(1, 0, "switch/off", "switch/on")
Switch1 = Actor(Enemigo_Switch1.get_sprite())

Enemigo_Switch2 = Monstruo(1, 0, "switch/off", "switch/on")
Switch2 = Actor(Enemigo_Switch2.get_sprite())# type: ignore

Enemigo_Switch3 = Monstruo(1, 0, "switch/off", "switch/on")
Switch3 = Actor(Enemigo_Switch3.get_sprite())# type: ignore

Enemigo_Switch4 = Monstruo(1, 0, "switch/off", "switch/on")
Switch4 = Actor(Enemigo_Switch4.get_sprite())# type: ignore

Enemigo_Switch5 = Monstruo(1, 0, "switch/off", "switch/on")
Switch5 = Actor(Enemigo_Switch5.get_sprite())# type: ignore
Enemigo_Switch6 = Monstruo(1, 0, "switch/off", "switch/on")
Switch6 = Actor(Enemigo_Switch6.get_sprite())# type: ignore
#-------------------------
Easter_egg1 = Actor("enemigos/cara")# type: ignore
Easter_egg1.pos = 0, 300
#-----------------
Easter_egg2 = Actor("enemigos/freddy")# type: ignore
freddy = False
#-----------------
Easter_egg_chance = 0
Easter_egg_chance1 = 0
#-------------------------
anchoBoton = 150
altoBoton = 70
posBotonY = ALTO - anchoBoton/1.5
posBotonX = ANCHO - ANCHO/2
boton_jugar = Rect((posBotonX, posBotonY), (anchoBoton, altoBoton))
boton_opc = Rect((posBotonX+anchoBoton*1.5, posBotonY), (anchoBoton, altoBoton))
boton_salir = Rect((posBotonX+anchoBoton*3, posBotonY), (anchoBoton, altoBoton))

botonRegresar = Rect((20, ALTO-altoBoton-20), (anchoBoton, altoBoton))

color_button_jugar = "grey"
color_button_opc = "grey"
color_button_salir = "grey"
color_button_regresar = "grey"
#-------------------------RE ESCALAR IMAGENES
imagen = pygame.image.load("images/instrucciones.jpg")
#imagen = pygame.image.load("metal")
metal = pygame.transform.scale(imagen, (1280,720))

imagen = pygame.image.load("images/menu.png")
menu = pygame.transform.scale(imagen, (1280,720))

imagen = pygame.image.load("images/ventana.png")
ventana = pygame.transform.scale(imagen, (1280,720))

imagen = pygame.image.load("images/titulo.png")
titulo = pygame.transform.scale(imagen, (1024/2,471/2))
#-------------------------------
tamanioCuadro = 150
izquierda = pygame.Rect(0, 0, tamanioCuadro, ALTO)
derecha = pygame.Rect(ANCHO-tamanioCuadro, 0, tamanioCuadro, ALTO)
#-------------------------HITBOX
#Los atributos van Pos: X, Y Tamaño: Ancho, Alto
hitbox_view = False

hitbox_puerta1_atributos = (-180, 30, 50, 90)
hitbox_puerta2_atributos = (-130, 50, 60, 90)
hitbox_puerta3_atributos = (-70, 65, 65, 80)
hitbox_puerta4_atributos = (-5, 80, 60, 80)
hitbox_puerta5_atributos = (55, 100, 90, 80)

hitbox_ventana_atributos = (ANCHO - 150, 100, 400, 250)
hitbox_ventana = pygame.Rect(hitbox_ventana_atributos[0], hitbox_ventana_atributos[1], hitbox_ventana_atributos[2], hitbox_ventana_atributos[3])

hitbox_mesa_atributos = (ANCHO/2 - (500/2), 425, 500, 100)
hitbox_mesa = pygame.Rect(hitbox_mesa_atributos[0], hitbox_mesa_atributos[1], hitbox_mesa_atributos[2], hitbox_mesa_atributos[3])

hitbox_proyector_atributos = (ANCHO/2 - (100/2), 0, 100, 100)
hitbox_proyector = pygame.Rect(hitbox_proyector_atributos[0], hitbox_proyector_atributos[1], hitbox_proyector_atributos[2], hitbox_proyector_atributos[3])

hitbox_nariz_atributos = (110, 25, 75, 75)
nariz_award = False
hitbox_nariz = pygame.Rect(hitbox_nariz_atributos[0], hitbox_nariz_atributos[1], hitbox_nariz_atributos[2], hitbox_nariz_atributos[3])
#-------------------------
#-------------------------
#ESTO ES MUY IMPORTANTE. NO BORRAR: HACE QUE SE MUEVA EL ESCENEARIO JUNTO A HITBOX Y FONDO
movi = 0.0
move_max = 175.0
cam_velocidad = 11
#-------------------------
fade = False
negativo = False
transicion_velocidad = 1
transicion_timer = 0
escenarios = 0
parpadeo = 0.0
#-------------------------
fondo = Actor('fondo')
fondo.pos = ANCHO/2, ALTO/2
mostrar_cuenta_regresiva = False   # Bandera booleana para controlar si se muestra la cuenta regresiva
#-------------------------
bajo_Mesa = Monstruo(1, 0,"bajo_mesa","bajo_mesa_1","bajo_mesa_2")
puerta = Monstruo(1, 0,"ventanilla", "enemigos/naked_2")
mesa = Monstruo(1, 0,"mesa_off")
luz_proyector = Monstruo(1,0, "brillo/brillo_mesa","brillo/brillo_proyector","brillo/brillo_ventana","brillo/brillo_ventanilla","brillo/brillo_abajo","brillo/brillo_salon")
#-------------------MARIO NETA
puppet = Monstruo(1,0,"enemigos/nada","enemigos/nada","enemigos/puppet_face","enemigos/puppet_end", "enemigos/puppet_jump")
puppet_posiciones = ([188,250],[300,50],[1170,20],[734,300],[25,70])
hitbox_puppet = pygame.Rect(50, 50, 0, 0)
puppet_pos = 0
puppet_timer = 0
puppet_sound =  0
puppet_cooldown = 3
#-------------------MARIO NETA
#naked = Monstruo(1,0, "enemigos/nada", "enemigos/nada", "enemigos/nada", "enemigos/nada")
naked_screamer_actor = Actor("enemigos/naked_screamer/naker1")
naked = Monstruo(1,0, "enemigos/nada", "enemigos/naked_1", "enemigos/nada","puerta_abierta", "enemigos/naked_screamer/naker1")
naked_timer = 0
naked_sound = 0
naked_cooldown = 30

naked_tiempo_espera = 0
naked_tiempo_escondido = 0
#------------------------
juego_iniciar = False #cambiar
juego_menu = True #cambiar
juego_instrucciones = False
juego_perder = False
juego_screamer = False
#------------------------
juego_salon = False #cambiar
juego_puerta = False
juego_ventana = False
juego_mesa = False
juego_proyector = False
juego_compu = False
juego_pantalla_perder = False
juego_pantalla_ganar_horas = False
#-------------------------TIEMPO
timer = 0.0  
minutos = 0
horas = 0
#---------------------------- COMPUTADORA
compu = Monstruo(1,0,"pc/pc4","pc/pc3","pc/pc2","pc/pc1","pc/pc0","enemigos/nada")
pcs = 1 + dificultad
cantidad_ram = pcs * 4
dificultad_ram = 4 + dificultad*2
contador_ram = 0
switch_ram = 1
cambio_pc = False
cambio_pc_volver = False
pos_pc_x = 0
#----------------------------
juego_extras = False
extras = Actor("extra.jpg")
#----------------------------
interferencia = ['interferencia/inter1.png','interferencia/inter2.png',
                'interferencia/inter3.png','interferencia/inter4.png',
                'interferencia/inter5.png','interferencia/inter6.png',
                'interferencia/inter7.png','interferencia/inter8.png',
                'interferencia/inter9.png','interferencia/inter10.png']
Inter = Actor(interferencia[0])
inter_frame = 0
#--------------------
GameOverTime = 4
archivo_binario = "datos.bin"
star = Actor("starts/estrella.png")
Estrellas = 0
if os.path.exists(archivo_binario):
    with open(archivo_binario, "rb") as f:
        dato = f.read(1)
        if dato:
            Estrellas = int.from_bytes(dato, byteorder="big")
else:
    with open(archivo_binario, "wb") as f:
        f.write(Estrellas.to_bytes(1, byteorder="big"))
print(Estrellas)
#-------------------------
linterna = False
bateria = 100 + (Estrellas * 2)
#--------------------SONIDOS
sounds.fnaf_luces.set_volume(0.4)
sounds.fnaf_nariz.set_volume(0.1)
if juego_menu:
    music.play("musica_menu.wav")
music.set_volume(0.5)
sounds.click.set_volume(0.25)
sounds.light.set_volume(0.8)

sounds.interaccion.set_volume(0.8)
sounds.glich.set_volume(0.05)

sounds.ventana_abrir.set_volume(0.2)
sounds.ventana_cerrar.set_volume(0.2)
sounds.movimiento_de_ropa_en_cesta.set_volume(0.25)

sounds.subir_mesa.set_volume(0.3)
sounds.bajar_mesa.set_volume(0.3)

sounds.naked_screamer.set_volume(0.5)
sounds.naked_pasos.set_volume(0.75)
sounds.naked_puerta.set_volume(0.7)
sounds.naked_puerta_cerrar.set_volume(0.4)
sounds.naked_suspiro.set_volume(0.5)

sounds.puppet_grito1.set_volume(0.3)
sounds.puppet_grito2.set_volume(0.3)
sounds.puppet_grito3.set_volume(0.3)
sounds.puppet_screamer.set_volume(0.3)
sounds.ventana1.set_volume(0.3)
sounds.ventana2.set_volume(0.3)

sounds.ram_down.set_volume(0.5)
sounds.ram_up.set_volume(0.5)

sounds.ganar.set_volume(0.5)

def draw():
    global juego_menu, juego_iniciar, juego_instrucciones
    global fade, escenarios, hitbox_view
    global metal, menu, parpadeo, movi, star
    global juego_salon, juego_puerta, juego_ventana, juego_mesa, juego_proyector, juego_compu
    global hitbox_puerta1, hitbox_puerta2, hitbox_puerta3, hitbox_puerta4, hitbox_puerta5, hitbox_puppet
    global puppet_pos, inter_frame, Estrellas
    global GameOverTime,juego_pantalla_perder,juego_pantalla_ganar_horas,naked
    global pcs, cantidad_ram, contador_ram, cambio_pc, pos_pc_x, cambio_pc_volver, freddy, juego_extras, dificultad
    """
    Función principal encargada de dibujar todos los elementos del juego en la pantalla.
    """
    if juego_menu:

            screen.clear()
            screen.fill((255,255,255))
            screen.blit(menu, (0, 0))

            #screen.draw.text("Jugador 1: " + str("hola"), color="black", topleft=(10, 10))
            #screen.draw.text("Jugador 2: " + str("adio"), color="black", topleft=(10, 40))
            #screen.draw.text("FIVE NIGHTS\n\nAT E-45", color="white", topleft=(75,ALTO/3), fontsize=80)
            screen.blit(titulo, (25,25))
            
            if mostrar_cuenta_regresiva:
                screen.draw.text(str("contador"), color="black", topleft=(CENTRO_X - 8, 150), fontsize=60)
            
            #screen.blit(Inter, (0,0))
            #----------------------------
            #boton_jugar----------------------------
            #screen.draw.rect(boton_jugar,(255,0,0))
            #boton_opc----------------------------
            #screen.draw.rect(boton_opc,(255,0,0))
            #boton_salir----------------------------
            #screen.draw.rect(boton_salir,(255,0,0))
            #----------------------------
            #----------------------------
            screen.draw.text("JUGAR", color=color_button_jugar,center=boton_jugar.center, fontsize=40)
            screen.draw.text("INSTRUCCIONES", color=color_button_opc, center=boton_opc.center, fontsize=40)
            screen.draw.text("SALIR", color=color_button_salir, center=boton_salir.center, fontsize=40)
            
            i = 0
            for i in range(0, Estrellas):
                star.pos = 640.0 + (i*70), 360.0
                star.draw()
            if juego_extras:
                extras.draw()
    
    elif juego_iniciar:
        #print(Enemigo_Fantasma.get_sprite())
        #Fantasma.image = Enemigo_Fantasma.get_sprite()
        if juego_salon:
            sounds.puppet_noise.set_volume(0.05)                        #type: ignore
            #print(juego_salon, juego_puerta, juego_ventana, juego_mesa, juego_proyector)
            screen.clear()                        #type: ignore
            #screen.blit("prueba", (0,0))
            luz_proyector.set_nivel(5)
            fondo.draw()
            fondo.pos = ANCHO/2 + movi, ALTO/2
            #-------------------------------------------
            if horas < 1:
                screen.draw.text("12 PM", color="white", topleft=(ANCHO - 150, 15), fontsize=40)                        #type: ignore
            else:
                screen.draw.text(str(horas)+"AM", color="white", topleft=(ANCHO - 150, 15), fontsize=40)                #type: ignore
            #----------------------------VER HITBOX
            if hitbox_view:
                screen.draw.rect(izquierda, (255,0,0))
                screen.draw.rect(derecha, (255,0,0))
                screen.draw.rect(hitbox_puerta1, (255,0,0))
                screen.draw.rect(hitbox_puerta2, (255,0,0))
                screen.draw.rect(hitbox_puerta3, (255,0,0))
                screen.draw.rect(hitbox_puerta4, (255,0,0))
                screen.draw.rect(hitbox_puerta5, (255,0,0))
                screen.draw.rect(hitbox_ventana, (0,255,0))
                screen.draw.rect(hitbox_mesa, (0,0,255))
                screen.draw.rect(hitbox_proyector, (255,255,0))
                screen.draw.rect(hitbox_nariz, (255,0,255))
            #----------------------------       
            screen.draw.text(str(round(bateria))+"%", color="white", topleft=(15, ALTO-40), fontsize=40)                #type: ignore
            #screen.draw.text("Dificultad: "+str(round(dificultad)), color="white", topleft=(ANCHO/2, 40), fontsize=40)
            
            if naked.get_nivel() == 3:
                screen.blit(naked.get_sprite(), (movi-185,-116))                                                        #type: ignore
            if puppet.get_nivel() == 3:
                screen.blit(puppet.get_sprite(), (1000 + randint(-2,2), 75 + randint(-2,2)))                            #type: ignore

            if Easter_egg_chance1 == 1 and not juego_perder:
                freddy = True
                Easter_egg2.pos = movi+1090,320
                Easter_egg2.angle = -5
                Easter_egg2.draw()
            else:
                freddy = False
     
        elif juego_puerta:
            sounds.puppet_noise.set_volume(0.01) #type: ignore
            screen.clear()#type: ignore
            match naked.get_nivel():
                case 0:
                    puerta.set_nivel(0)
                case 1:
                    puerta.set_nivel(0)
                case 2:
                    puerta.set_nivel(1)
            screen.blit(puerta.get_sprite(), (0,0))#type: ignore
            screen.blit(naked.get_sprite(), (0, 0))#type: ignore
            if Easter_egg_chance == 1:
                Easter_egg1.angle = 10
                Easter_egg1.draw()

            luz_proyector.set_nivel(3)
        #-------------------------------------------
        elif juego_ventana:
            sounds.puppet_noise.set_volume(0.1)
            screen.clear()
            screen.blit(ventana, (0, 0))
        #-------------------------------------------
            if puppet.get_nivel() == 2:
                hitbox_puppet = pygame.Rect(puppet_posiciones[puppet_pos][0],puppet_posiciones[puppet_pos][1],50,50) 
                screen.blit(puppet.get_sprite(), (puppet_posiciones[puppet_pos][0] + randint(-12,12), puppet_posiciones[puppet_pos][1]  + randint(-12,12)))
                if hitbox_view:                
                    screen.draw.rect(hitbox_puppet, (255,0,0))
        #-------------------------------------------
            luz_proyector.set_nivel(2)
        
        elif juego_mesa:
            sounds.puppet_noise.set_volume(0.04)
            screen.clear()
            screen.blit(bajo_Mesa.get_sprite(), (0,0))
            luz_proyector.set_nivel(4)
            
        elif juego_proyector:
            sounds.puppet_noise.set_volume(0.04)
            screen.clear()
            screen.blit("proyector", (0,0))
            luz_proyector.set_nivel(1)
            
            Switch1.image = Enemigo_Switch1.get_sprite()                
            Switch1.pos = 780, 315
            Switch1.draw()

            Switch2.image = Enemigo_Switch2.get_sprite()
            Switch2.pos = 855, 313
            Switch2.draw()

            Switch3.image = Enemigo_Switch3.get_sprite()
            Switch3.pos = 930, 311
            Switch3.draw()

            Switch4.image = Enemigo_Switch4.get_sprite()
            Switch4.pos = 780, 400
            Switch4.draw()

            Switch5.image = Enemigo_Switch5.get_sprite()
            Switch5.pos = 855, 398
            Switch5.draw()

            Switch6.image = Enemigo_Switch6.get_sprite() 
            Switch6.pos = 930, 396
            Switch6.draw()   
            #screen.blit("proyector", (0,0))

        elif juego_compu:
            #print(pos_pc_x)

            sounds.puppet_noise.set_volume(0.04) #type: ignore
            global cantidad_ram, dificultad_ram, contador_ram
            screen.clear() #type: ignore
            screen.blit(mesa.get_sprite(), (0,0)) #type: ignore
            screen.blit(compu.get_sprite(), (pos_pc_x,0)) #type: ignore
            if cambio_pc:
                if not cambio_pc_volver:
                    pos_pc_x -= 5
                    if pos_pc_x <= -50:
                        pos_pc_x -= 15
                    if pos_pc_x <= -150:
                        pos_pc_x -= 30
                    if pos_pc_x <= -1000:
                        compu.set_nivel(0)
                        pos_pc_x = 800
                        cambio_pc_volver = True
                        if pcs == 0:
                            compu.set_nivel(5)
                else:
                    pos_pc_x -= 20
                    if pos_pc_x <= 0:
                        cambio_pc = False
            luz_proyector.set_nivel(0)
            screen.draw.text("PCs Faltantes: " + str(pcs), color="white", topleft=(ANCHO-175, 15)) #type: ignore
        
        #-------------------------------------------
        light = pygame.Surface((ANCHO,ALTO), pygame.SRCALPHA)
        Cuadro_alpha = pygame.Surface((ANCHO,ALTO))
        Cuadro_alpha.fill((0,0,0))
        Cuadro_alpha.set_alpha(75)
        #-------------------------------------------

        if naked.get_nivel() == 4:
            screen.blit(naked.get_sprite(), (0 + randint(-24,24), 0 + randint(-24,24)))
        
        if puppet.get_nivel() == 4:
            screen.blit(puppet.get_sprite(), (0 + randint(-24,24), 0 + randint(-24,24)))                            #type: ignore
        
        if linterna:
            pos_mouse = pygame.mouse.get_pos()
            pygame.draw.circle(light, (255, 255, 255, 5), pos_mouse, ANCHO/7)
            pygame.draw.circle(light, (255, 255, 255, 10), pos_mouse, ANCHO/8)
            pygame.draw.circle(light, (255, 255, 255, 15), pos_mouse, ANCHO/8.5)
            pygame.draw.circle(light, (255, 255, 255, 17), pos_mouse, ANCHO/9)
            pygame.draw.circle(light, (255, 255, 255, 19), pos_mouse, ANCHO/9.5)
            pygame.draw.circle(light, (255, 255, 255, 10), pos_mouse, ANCHO/9.9)
            pygame.draw.circle(light, (255, 255, 255, 1), pos_mouse, ANCHO/10)
            pygame.draw.circle(light, (255, 255, 255, 10), pos_mouse, ANCHO/10.1)
            pygame.draw.circle(light, (255, 255, 255, 25), pos_mouse, ANCHO/11)
            pygame.draw.circle(light, (255, 255, 255, 30), pos_mouse, ANCHO/12)
            Cuadro_alpha.set_alpha(10)
        
        screen.blit(light, (0, 0))
        if juego_perder:
            Cuadro_alpha.set_alpha(25)
        else:
            if switchs_encendidos >=3:
                if parpadeo <= 50:
                    luz_proyector.pos =  0, 0
                    fondo.image = "fondo_bajo"
                    screen.blit(luz_proyector.get_sprite(), (0,0))

                    if not juego_ventana:
                        Cuadro_alpha.set_alpha(0)
                else:
                    fondo.image = "fondo"
                    if parpadeo >= 80:
                        parpadeo = 0
            else:
                screen.blit("brillo/brillo_salon", (0,0))
                fondo.image = "fondo"
            #SE TIENE QUE BAJAR EL ALFA CUANDO PRESENTEMOS
            #ES POSIBLE QUE NO SE MIRE SI MUCHA LUZ XD
            if juego_ventana:
                Cuadro_alpha.set_alpha(225)
                if linterna:
                    Cuadro_alpha.set_alpha(80)
            
        screen.blit(Cuadro_alpha, (0, 0))

    elif juego_instrucciones:
        screen.clear()
        screen.fill((255,255,255))
        screen.blit(metal, (0, 0))

        #screen.draw.rect(botonRegresar,(255,0,0))
        screen.draw.text("REGRESAR", color=color_button_regresar,center=botonRegresar.center, fontsize=40)

    if juego_perder:
        dibujar_interferencia(15)
    if juego_menu or juego_instrucciones:
        dibujar_interferencia(25)

    if juego_salon and freddy and Easter_egg_chance1 == 1:
        dibujar_interferencia(50)

    if fade:
        global negativo, transicion_timer, transicion_velocidad
        Cuadro_alpha = pygame.Surface((ANCHO,ALTO))
        opacidad = transicion_timer * transicion_velocidad
            #print(opacidad)
            #print(juego_menu, juego_instrucciones, juego_iniciar)
        if not negativo:
            Cuadro_alpha.set_alpha(opacidad)
        else:
            Cuadro_alpha.set_alpha(255 - (opacidad))
            if opacidad >= 255:
                fade = False
                negativo = False
                transicion_timer = 0
                    
        if (opacidad) >= 500 or juego_perder:
            negativo = True
            transicion_timer = 0
            if juego_iniciar:
                match escenarios:
                    case 4:
                        juego_salon = False
                        juego_puerta = True
                    case 5:
                        juego_salon = False
                        juego_ventana = True
                        puppet_pos = randint(0,4)
                    case 6:
                        juego_salon = False
                        juego_mesa = True
                    case 7:
                        juego_salon = False
                        juego_proyector = True
                    case 8:
                        juego_puerta = False
                        juego_ventana = False
                        juego_mesa = False
                        juego_proyector = False
                        juego_compu = False
                        juego_salon = True
                    case 9:
                        juego_salon = False
                        juego_compu = True
                    case 10:
                        reset()
                        
            else:
                match escenarios:
                    case 0: 
                        juego_menu = False
                        juego_salon = True
                        juego_iniciar = True
                    case 1:
                        juego_menu = False
                        juego_instrucciones = True
                    case 2:
                        juego_menu = True
                        juego_instrucciones = False
                    case 3:
                        quit()

        Cuadro_alpha.fill((0,0,0))
        screen.blit(Cuadro_alpha, (0, 0))

    if juego_pantalla_perder:
        screen.clear()
        screen.fill((0,0,0))
        screen.draw.text("TE ATRAPARON", color="white", topleft=((ANCHO/2)-120, ALTO/2-60), fontsize=80)

    if juego_pantalla_ganar_horas:
        screen.clear()
        screen.fill((0,0,0))
        screen.draw.text("6AM", color="white", topleft=((ANCHO/2)-50, ALTO/2-45), fontsize=80)

    return

def dibujar_interferencia(opacidad):
    global Inter, interferencia, inter_frame
    Inter._surf.set_alpha(opacidad)
    Inter.draw()
    Inter.image = interferencia[inter_frame]
    if inter_frame <= 8:
        inter_frame += 1
    else:
        inter_frame = 0
#SI EL MOUSE DA UN CLICK EN LA POSICION CORRESPONDIENTE
def on_mouse_down(pos, button):
    global juego_menu, juego_iniciar, juego_instrucciones
    global hitbox_ventana, hitbox_mesa, hitbox_proyector, botonRegresar, hitbox_nariz
    global juego_salon, juego_puerta, juego_ventana, juego_mesa, juego_proyector, juego_compu
    global switchs_encendidos, puppet_pos, puppet_sound, puppet, hitbox_puppet
    global Easter_egg_chance, nariz_award

    if button == mouse.LEFT and not fade:
        #------------EN MENU
        if juego_menu:
            if boton_jugar.collidepoint(pos):
                sounds.interaccion.play()
                fade_out(0, 75)
                #CAMBIAR ESTO PARA QUE SEA MAS LENTO, AHORITA LO TENGO RAPIDO PARA LAS PRUEBAS
                music.play("musica_ambiente.wav")
                music.set_volume(0.4)
            if boton_opc.collidepoint(pos):
                sounds.interaccion.play()
                fade_out(1, 10)
            if boton_salir.collidepoint(pos):
                sounds.interaccion.play()
                quit()
        #------------EN JUEGO
        velocidad = 8
        if juego_iniciar:
            if juego_salon and not juego_perder:
                if hitbox_puerta1.collidepoint(pos):
                    Easter_egg_chance = randint(1,20)
                    sounds.ventana_abrir.play()
                    fade_out(4, velocidad)
                if hitbox_puerta2.collidepoint(pos):
                    Easter_egg_chance = randint(1,20)
                    sounds.ventana_abrir.play()
                    fade_out(4, velocidad)
                if hitbox_puerta3.collidepoint(pos):
                    Easter_egg_chance = randint(1,20)
                    sounds.ventana_abrir.play()
                    fade_out(4, velocidad)
                if hitbox_puerta4.collidepoint(pos):
                    Easter_egg_chance = randint(1,20)
                    sounds.ventana_abrir.play()
                    fade_out(4, velocidad)
                if hitbox_puerta5.collidepoint(pos):
                    Easter_egg_chance = randint(1,20)
                    sounds.ventana_abrir.play()
                    fade_out(4, velocidad)
                #---------------------------------
                if hitbox_ventana.collidepoint(pos):
                    sounds.ventana_abrir.play()
                    music.stop()
                    fade_out(5, velocidad)
                if hitbox_mesa.collidepoint(pos):
                    sounds.movimiento_de_ropa_en_cesta.play()
                    bajo_Mesa.set_nivel(randint(0,2))
                    fade_out(6, 7)
                if hitbox_proyector.collidepoint(pos):
                    sounds.subir_mesa.play()
                    fade_out(7, velocidad)
                if hitbox_nariz.collidepoint(pos):
                    nariz_award = True
                    sounds.fnaf_nariz.play()
                    
            if juego_proyector:
                if Switch1.collidepoint(pos):
                    if Enemigo_Switch1.get_nivel() == 1:
                        Enemigo_Switch1.set_nivel(0)
                        sounds.click.play()
                        switchs_encendidos -= 1
                if Switch2.collidepoint(pos):
                    if Enemigo_Switch2.get_nivel() == 1:
                        Enemigo_Switch2.set_nivel(0)
                        switchs_encendidos -= 1
                        sounds.click.play()
                if Switch3.collidepoint(pos):
                    if Enemigo_Switch3.get_nivel() == 1:
                        Enemigo_Switch3.set_nivel(0)
                        switchs_encendidos -= 1
                        sounds.click.play()
                if Switch4.collidepoint(pos):
                    if Enemigo_Switch4.get_nivel() == 1:
                        Enemigo_Switch4.set_nivel(0)
                        switchs_encendidos -= 1
                        sounds.click.play()
                if Switch5.collidepoint(pos):
                    if Enemigo_Switch5.get_nivel() == 1:
                        Enemigo_Switch5.set_nivel(0)
                        switchs_encendidos -= 1
                        sounds.click.play()
                if Switch6.collidepoint(pos):
                    if Enemigo_Switch6.get_nivel() == 1:
                        Enemigo_Switch6.set_nivel(0)
                        switchs_encendidos -= 1
                        sounds.click.play()
        #----------EN Instrucciones
        if juego_instrucciones:
            if botonRegresar.collidepoint(pos):
                sounds.interaccion.play()
                fade_out(2,10)
        
        if juego_ventana:
            if linterna and hitbox_puppet.collidepoint(pos):
                puppet_gritos(randint(1,3))
                hitbox_puppet = pygame.Rect(50, 50, -50, -50)
                puppet_pos = randint(0,4)
                puppet_sound = 0
                puppet.set_nivel(0)

def puppet_gritos(valor):
    global puppet_cooldown, puppet_timer
    puppet_cooldown = 5
    puppet_timer = 0
    sounds.puppet_noise.stop()
    match valor:
        case 1:
            sounds.puppet_grito1.play()
            #print("audio1")
        case 2:
            sounds.puppet_grito2.play()
            #print("audio2")
        case 3:
            sounds.puppet_grito3.play()
            #print("audio3")

def on_key_down(key):
    global movi, minutos, horas, hitbox_view
    global juego_iniciar, juego_menu, juego_instrucciones
    global juego_mesa, juego_ventana, juego_salon, juego_proyector, juego_puerta, juego_perder
    global linterna, bateria, fondo, switchs_encendidos
    global Enemigo_Switch1, Enemigo_Switch2, Enemigo_Switch3, Enemigo_Switch4, Enemigo_Switch5, Enemigo_Switch6
    global puppet_timer, Switch_timer, GameOverTime, Easter_egg_chance1, dificultad

    global juego_compu, contador_ram, dificultad_ram, cantidad_ram, switch_ram, compu, cambio_pc, cambio_pc_volver, pcs
    
    if juego_iniciar:
        if not juego_perder:
            if key == keys.SPACE:
                if not fade:
                    if not juego_salon:
                        if juego_mesa:
                            sounds.movimiento_de_ropa_en_cesta.play()
                        if juego_ventana:
                            sounds.ventana_cerrar.play()
                            music.play("musica_ambiente.wav")
                            music.set_volume(0.4)
                        if juego_proyector:
                            sounds.bajar_mesa.play()
                        if juego_puerta:                        
                            sounds.ventana_cerrar.play()
                        Easter_egg_chance1 = randint(1,50)
                        fade_out(8, 10)
                    else:
                        fade_out(9, 12)

            if key == keys.F:
                sounds.light.play()
                if bateria > 0:
                    linterna = not linterna
                    if linterna:
                        sounds.fnaf_luces.play(-1)
                    else:            
                        sounds.fnaf_luces.stop()

        if key == keys.H:
            hitbox_view = not hitbox_view
        if key == keys.P:
            pygame.display.toggle_fullscreen()
        """
        if juego_salon:
            if key == keys.UP:
                dificultad+=1
            if key == keys.DOWN:
                dificultad-=1
                """

    else:
        if key == keys.F:
            pygame.display.toggle_fullscreen()
            print(pygame.display.get_window_size())

    if key == keys.ESCAPE:
        if juego_iniciar and not fade:
            fade_out(10,7)


    if juego_compu:
        if not cambio_pc and pcs != 0:
            if key == keys.W or key == keys.UP:
                if (switch_ram % 2) == 1:
                    contador_ram += 1
                    switch_ram = 2
                    sounds.ram_up.play()
            if key == keys.S or key == keys.DOWN:
                if (switch_ram % 2) == 0:
                    switch_ram = 1
                    sounds.ram_down.play()
                if contador_ram == dificultad_ram:
                    compu.set_nivel(compu.get_nivel()+1)
                    cantidad_ram -= 1
                    contador_ram = 0

                    if compu.get_nivel() == 4:
                        cantidad_ram = 4
                        pcs -= 1
                        cambio_pc_volver = False
                        cambio_pc = True
                
def reset():
        global movi, minutos, horas, cam_velocidad
        global juego_menu, juego_iniciar, juego_instrucciones, puppet_sound
        global juego_mesa, juego_ventana, juego_salon, juego_proyector, juego_puerta, juego_compu, juego_perder, juego_pantalla_perder,juego_pantalla_ganar_horas
        global cantidad_ram, bateria, linterna, contador_ram, switchs_encendidos, puppet_timer, Switch_timer, puppet_cooldown, GameOverTime
        global naked_timer, naked, puppet, puerta, naked_sound, naked_tiempo_espera, naked_tiempo_escondido,naked_cooldown
        global Estrellas 
        global pcs, dificultad_ram, freddy, Easter_egg_chance, switch_ram
        global Easter_egg_chance1, nariz_award, puppet_pos, cambio_pc
        global cambio_pc_volver, pos_pc_x, Estrellas, compu

        movi = 0.0
        minutos = 0
        horas = 0
        juego_perder = False
        juego_menu = True
        juego_iniciar = False
        juego_instrucciones = False
        #-----------------------
        juego_mesa = False
        juego_ventana = False
        juego_salon = False
        juego_proyector = False
        juego_puerta = False
        juego_compu = False
        juego_perder = False
        juego_pantalla_perder = False
        juego_pantalla_ganar_horas = False
        #-----------------------
        GameOverTime = 4
        bateria = 100 + (Estrellas * 2)
        linterna = False
        switchs_encendidos = 0
        puppet_timer = 0
        puppet_sound = 0
        puppet_cooldown = 3

        Switch_timer = 0
        cam_velocidad = 11
#-------------------------
        pcs = 6
        cantidad_ram = 6
        dificultad_ram = 14
        freddy = False
        contador_ram = 10
        Easter_egg_chance = 0
        switch_ram = 1
        Easter_egg_chance1 = 0
        nariz_award = False
        puppet_pos = 0
        cambio_pc = False
        cambio_pc_volver = False
        pos_pc_x = 0
        compu.set_nivel(0)
#-------------------------
        naked_timer = 0
        naked_cooldown = 10
        puppet.set_nivel(0)
        puerta.set_nivel(0)
        naked.set_nivel(0)
        naked_sound = 0
        naked_tiempo_espera = 0
        naked_tiempo_escondido = 0
        Enemigo_Switch1.set_nivel(0)
        Enemigo_Switch2.set_nivel(0)
        Enemigo_Switch3.set_nivel(0)
        Enemigo_Switch4.set_nivel(0)
        Enemigo_Switch5.set_nivel(0)
        Enemigo_Switch6.set_nivel(0)
        #---------------------
        music.stop()
        sounds.puppet_noise.stop()
        sounds.glich.stop()
        music.play("musica_menu.wav")
        music.set_volume(0.5)

def fade_out(origen, velocidad):
    global fade, escenarios, transicion_velocidad, transicion_timer
    fade = True
    escenarios = origen
    transicion_velocidad = velocidad
    transicion_timer = 0

def switchOn(nivel):
    global Enemigo_Switch1, Enemigo_Switch2, Enemigo_Switch3, Enemigo_Switch4, Enemigo_Switch5, Enemigo_Switch6
    global switchs_encendidos
    #print("\n", nivel, "\n")
    match nivel:
        case 1:
            if Enemigo_Switch1.get_nivel() == 0:
                Enemigo_Switch1.set_nivel(1)
                return
        case 2:
            if Enemigo_Switch2.get_nivel() == 0:
                Enemigo_Switch2.set_nivel(1)
                return
        case 3:
            if Enemigo_Switch3.get_nivel() == 0:
                Enemigo_Switch3.set_nivel(1)
                return
        case 4:
            if Enemigo_Switch4.get_nivel() == 0:
                Enemigo_Switch4.set_nivel(1)
                return
        case 5:
            if Enemigo_Switch5.get_nivel() == 0:
                Enemigo_Switch5.set_nivel(1)
                return
        case 6:
            if Enemigo_Switch6.get_nivel() == 0:
                Enemigo_Switch6.set_nivel(1)
                return
    switchOn(randint(1,6))

def perder():
    global bateria
    global juego_perder, cam_velocidad
    bateria = 0
    juego_perder = True
    cam_velocidad = 0

def update(): # Esta es una función incorporada de Pygame Zero.
    global juego_iniciar, movi, juego_menu, timer, horas, minutos, transicion_timer, juego_perder
    global hitbox_ventana, hitbox_mesa, hitbox_proyector, hitbox_nariz
    global hitbox_ventana_atributos, hitbox_mesa_atributos, hitbox_proyector_atributos, hitbox_nariz_atributos
    global color_button_jugar, color_button_opc, color_button_regresar, color_button_salir
    global linterna, bateria, Switch_timer, switchs_encendidos
    global hitbox_puerta1, hitbox_puerta2, hitbox_puerta3, hitbox_puerta4, hitbox_puerta5, luz_proyector
    global parpadeo, puppet_timer, puppet_sound,puppet_cooldown
    global juego_puerta,juego_ventana, juego_mesa, juego_proyector, juego_compu, juego_salon, juego_pantalla_perder,juego_pantalla_ganar_horas
    global naked, naked_sound, naked_timer, GameOverTime, naked_tiempo_espera, naked_tiempo_escondido, naked_cooldown
    global Estrellas, juego_extras, cam_velocidad, dificultad
    pos_mouse = pygame.mouse.get_pos()
    if juego_menu:
        if keyboard.p:
            juego_extras = True
        else:
            juego_extras =False
    #------------------------------         
    if juego_iniciar and not juego_perder: 
        if izquierda.collidepoint(pos_mouse):
            #print(move_max)
            if movi <= move_max:
                movi += cam_velocidad
        if derecha.collidepoint(pos_mouse):
            #print(-move_max)
            if movi >= -move_max:
                movi -= cam_velocidad
        #-------------------------
        hitbox_puerta1 = pygame.Rect(movi + hitbox_puerta1_atributos[0], hitbox_puerta1_atributos[1], hitbox_puerta1_atributos[2], hitbox_puerta1_atributos[3])
        hitbox_puerta2 = pygame.Rect(movi + hitbox_puerta2_atributos[0], hitbox_puerta2_atributos[1], hitbox_puerta2_atributos[2], hitbox_puerta2_atributos[3])
        hitbox_puerta3 = pygame.Rect(movi + hitbox_puerta3_atributos[0], hitbox_puerta3_atributos[1], hitbox_puerta3_atributos[2], hitbox_puerta3_atributos[3])
        hitbox_puerta4 = pygame.Rect(movi + hitbox_puerta4_atributos[0], hitbox_puerta4_atributos[1], hitbox_puerta4_atributos[2], hitbox_puerta4_atributos[3])
        hitbox_puerta5 = pygame.Rect(movi + hitbox_puerta5_atributos[0], hitbox_puerta5_atributos[1], hitbox_puerta5_atributos[2], hitbox_puerta5_atributos[3]) 
        #-------------------------
        hitbox_ventana = pygame.Rect(movi + hitbox_ventana_atributos[0], hitbox_ventana_atributos[1], hitbox_ventana_atributos[2], hitbox_ventana_atributos[3])
        hitbox_mesa = pygame.Rect(movi + hitbox_mesa_atributos[0], hitbox_mesa_atributos[1], hitbox_mesa_atributos[2], hitbox_mesa_atributos[3])
        hitbox_proyector = pygame.Rect(movi + hitbox_proyector_atributos[0], hitbox_proyector_atributos[1], hitbox_proyector_atributos[2], hitbox_proyector_atributos[3])
        hitbox_nariz = pygame.Rect(movi + hitbox_nariz_atributos[0], hitbox_nariz_atributos[1], hitbox_nariz_atributos[2], hitbox_nariz_atributos[3])

        """
        if puerta.collidepoint(pos_mouse):
            print("no nada")"""
    #------------------------------    
    if juego_menu:
        if boton_jugar.collidepoint(pos_mouse):
            color_button_jugar = "white"
        else:
            color_button_jugar = 128,128,128

        if boton_opc.collidepoint(pos_mouse):
            color_button_opc = "white"
        else:
            color_button_opc = 128,128,128

        if boton_salir.collidepoint(pos_mouse):
            color_button_salir = "white"
        else:
            color_button_salir = 128,128,128
    if juego_instrucciones:
        if botonRegresar.collidepoint(pos_mouse):
            color_button_regresar = "white"
        else:
            color_button_regresar = 128,128,128
        
    timer += 1
    #print(timer)
    #Cuenta cada segundo
    if juego_iniciar:                
        if linterna:
            if bateria > 0:
                bateria -= (0.0166666667 * (dificultad))/2
            if bateria <= 0:
                bateria = 0
                linterna = False
                sounds.fnaf_luces.stop()
        if switchs_encendidos <= 2:
            sounds.glich.stop()
        if switchs_encendidos >= 3 and bateria >= 1:
            bateria -= 0.01 * switchs_encendidos

    if timer >= 60:
        #print(transicion_timer)
        if juego_iniciar:
            #print(horas, ":", minutos)
            if not juego_perder:
                minutos += 1
                #--------ESTO DEFINE LA DURACIÓN DE LA PARTIDA
                if minutos >= 30:#CAMBIAR A 50
                    horas += 1
                    minutos = 0
            #-------------------------------------------------
            if not juego_perder and horas < 6:
                Switch_timer += 1
                if Switch_timer == 9 - dificultad:#Cada 10 segundos chance de prender un switch
                    Switch_timer = 0
                    if switchs_encendidos < 6:
                        moneda_switch = randint(0,3) #De 25% de chanche que se active un switch
                        if moneda_switch == 0:
                            switchs_encendidos += 1
                            switchOn(randint(1,6))
                            if switchs_encendidos == 3:
                                sounds.glich.play(-1)
                        #print(moneda_switch, switchs_encendidos)
                #---------------PUPPET----------------------------------
                if puppet.get_nivel() != 3:
                    if puppet_cooldown == 0:
                        puppet_timer +=1
                        #------------------------------------------------
                        if puppet_timer == 8 - round(dificultad/2,0):#mover para hacer pruebas
                            puppet_timer = 0
                            moneda_puppet = randint(0,1)
                            if moneda_puppet == 0:
                                puppet.set_nivel(puppet.get_nivel()+1)
                                if(juego_ventana and puppet.get_nivel() == 2):
                                    puppet.set_nivel(1)
                                #--------IMPORTANTE
                            print("PUPPET----",puppet.get_nivel(), moneda_puppet)
                        #print(puppet_timer)

                        if not juego_ventana:
                            if puppet_sound == 0 and puppet.get_nivel() == 1:
                                sounds.ventana1.play()
                                puppet_sound += 1
                            if puppet_sound == 1 and puppet.get_nivel() == 2:
                                sounds.ventana2.play()
                                sounds.puppet_noise.play(-1)
                                puppet_sound += 1
                    else:
                        puppet_cooldown -= 1
                #----------------------------------NAKED MAN
                if naked.get_nivel() != 3:
                    if naked_cooldown == 0:
                        naked_timer +=1
                        if naked_timer == 12 - round(dificultad,0):
                            naked_timer = 0
                            moneda_naked = randint(0,3)
                            if moneda_naked == 0:
                                naked.set_nivel(naked.get_nivel()+1)
                                if(juego_puerta):
                                    match naked.get_nivel():
                                        case 1:
                                            naked.set_nivel(0)
                                        case 3:
                                            naked.set_nivel(2)
                                #--------IMPORTANTE
                            print("Naked----",naked.get_nivel(), moneda_naked)
                        #print(naked_timer)
                    else:
                        naked_cooldown-=1

                    if not juego_puerta:
                        if naked_sound == 0 and naked.get_nivel() == 1:
                            sounds.naked_pasos.play()
                            naked_sound += 1
                    if naked_sound == 1 and naked.get_nivel() == 2:
                        sounds.naked_suspiro.play()
                        naked_sound += 1
                    if naked_sound == 2 and naked.get_nivel() == 3:
                        sounds.naked_puerta.play()
                        naked_sound += 1

                elif naked.get_nivel() == 3:
                    naked_tiempo_espera += 1
                    #print("5 SEGUNDOS PARA ESCONDERTE")
                    if naked_tiempo_espera >= 5:
                        if not juego_mesa:
                            naked.set_nivel(4)
                        else:
                            naked_tiempo_escondido += 1

                if naked_tiempo_escondido >= 4:
                    naked_cooldown = 15
                    naked_sound = 0
                    sounds.naked_puerta_cerrar.play()
                    #print("ya puedes salir")
                    naked_tiempo_escondido = 0
                    naked_tiempo_espera = 0
                    naked.set_nivel(0)

                    
            if horas >= 6 and not juego_pantalla_ganar_horas and not juego_perder:
                juego_perder = True
                juego_pantalla_ganar_horas = True
                ganar = 1
                if pcs == 0:
                    ganar += 1
                if bateria >= 50:
                    ganar += 1
                if bateria >= 75:
                    ganar += 1
                if nariz_award == True:
                    ganar += 1
                
                if ganar >= Estrellas:
                    Estrellas = ganar
                    if os.path.exists("datos.bin"):
                        with open("datos.bin", "wb") as f:
                            f.write(ganar.to_bytes(1, byteorder="big"))
                
                sounds.ganar.play()
            else:
                #-------------------------PANTALLA Y TIEMPO A LA HORA DE PERDER
                if juego_pantalla_ganar_horas:
                    GameOverTime -= 1
                    naked.set_nivel(0)
                    puppet.set_nivel(0)
                    sounds.naked_pasos.stop()
                    sounds.puppet_screamer.stop()
                    sounds.puppet_noise.stop()

                    if GameOverTime <= 0:
                        GameOverTime = 4
                        fade_out(10,5)
                        
                if juego_pantalla_perder:
                    GameOverTime -= 1
                    if GameOverTime <= 0:
                        GameOverTime = 4
                        fade_out(10,5)

                if naked.get_nivel() >= 4:
                    perder()
                    puppet.set_nivel(0)

                    naked_timer += 1
                    if naked_timer <= 3:
                        naked.set_nivel(4)
                        sounds.naked_screamer.play()
                    if naked_timer >= 5:
                        juego_pantalla_perder = True
                        
                if puppet.get_nivel() >= 3:
                    perder()
                    naked.set_nivel(0)
                    puerta.set_nivel(0)

                    puppet_timer += 1
                    if puppet_timer <= 3:
                        puppet.set_nivel(4)
                        sounds.puppet_screamer.play()
                    if puppet_timer >= 5:
                        juego_pantalla_perder = True


            #-------------------------------------------------
            #-------------------------------------------------
        timer = 0
    #Cuenta cada 1/12 de segundo
    if timer >= 5:
        transicion_timer += 1
    parpadeo += 1   

    #if not juego_iniciar: # Si 'juego_iniciar' (el juego no ha terminado) es False (es decir, el juego todavía está en curso):
      #print("Acho: ", ANCHO, "Alto: ", ALTO)
      #print(mouse.get_position())
    #else:
     #   music.stop()

pgzrun.go()