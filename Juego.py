from pdb import run
import pygame, sys, direccion, random
from Clases import Metas
from Clases import Piedras
from Clases import PowerUpTiempo
from Clases import PowerUpVelocidad
from pygame.locals import *


def Nivel(RutaPista,PosicionInicial,AnguloInicial,Tiempo,PosicionMetas,TamanoMetas,RangodeaparicionRocas,RangodeaparicionPUTiempo,RangodeaparicionPUvelocudad):
    

    #Inicializacion del juego
    pygame.init()
    Screen_size = (720, 720)
    screen = pygame.display.set_mode(Screen_size)
    Icono = pygame.image.load("Images\Icon32x32.JPEG")
    pygame.display.set_icon(Icono)
    pygame.display.set_caption("BOAT RACE")
    FPS = pygame.time.Clock()
    FPS.tick(30)
    #Crea un evento personalizado (Para facilitarme el cronometro)
    Timer_event = pygame.USEREVENT + 24
    #Llama el evento creado cada segundo
    pygame.time.set_timer(Timer_event, 1000)
    FuenteTiempo = pygame.font.SysFont("Arial",20) #Establecer fuentes
    FuenteMensaje = pygame.font.SysFont("Terminal",100)
    FuenteIndicaciones = pygame.font.SysFont("Terminal",20)
    #Variables
    #Control
    Running = True
    Derecha = False
    Izquierda = False
    Adelante = False
    InicioJuego = False
    SiguienteNivel = False
    Victoria = 0
    #Listas-Tupas
    Lista_Piedras = pygame.sprite.Group()
    Lista_PuTiempo = pygame.sprite.Group()
    Lista_PuVelocidad = pygame.sprite.Group()
    Lista_Metas = pygame.sprite.Group()
    Lista_Todos_Sprites = pygame.sprite.Group()
    PosicionTemporizador = (0,0)
    #Colores
    Blanco = (255,255,255)
    Negro = (0,0,0)
    Rojo = (255,0,0)
    Verde = (0,255,0)
    Azul = (49, 148, 231 )
    #Imagenes
    Pista = pygame.image.load(RutaPista).convert()
    Pista.set_colorkey(Negro)
    Mascara = pygame.mask.from_surface(Pista) 
    Bote = pygame.image.load("Images\Bote.PNG").convert()
    ImgPowerUpTiempo = pygame.image.load("Images\TiempoPowerUp.PNG").convert()
    ImgPowerUpVelocidad = pygame.image.load("Images\VelocidadPowerUp.PNG").convert()
    ImgPiedra = pygame.image.load("Images\Obstaculo.PNG").convert()
    ImgMeta = pygame.image.load("Images\Meta.PNG").convert()
    #Musica
    pygame.mixer.music.load("Sounds\Gaviotas.mp3")#Carga
    pygame.mixer.music.play(3)
    #Posicion-Moviemiento del bote
    PosX = PosicionInicial[0]
    PosY = PosicionInicial[1]
    Angulo = AnguloInicial
    Velocidad = 0.0
    #Tiempo
    Cronometro = 0
    TiempoRestante = Tiempo
    #Textos
    TextoContador = "Tiempo: {} s "
    TextoVictoriaRender = FuenteMensaje.render("Ganaste", 0, Verde)
    TextoPerdidaRender = FuenteMensaje.render("Y se undio", 0, Rojo)
    TextoIndicacionesVictoriaRender = FuenteIndicaciones.render("press n:Siguiente lvl o Esc:Salir", 0, Verde)
    TextoIndicacionesDerrotaRender = FuenteIndicaciones.render("press r:Restart Lvl o Esc:Salir", 0, Rojo)
    class Boat(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = Bote
            self.image.set_colorkey(Negro)
            self.rect = self.image.get_rect()
            self.bmask = pygame.mask.from_surface(self.image)
    
#Crear cada instmacia, elemento individual 
    for i in range (2): #Piedras
      Obstaculo = Piedras.Obstaculos(ImgPiedra)
      Obstaculo.rect.x = random.randrange(RangodeaparicionRocas[0][0],RangodeaparicionRocas[0][1])
      Obstaculo.rect.y = random.randrange(RangodeaparicionRocas[1][0],RangodeaparicionRocas[1][1])
      Lista_Piedras.add(Obstaculo)
      Lista_Todos_Sprites.add(Obstaculo)
  
    for i in range (2): #TiempoPowerUp
      PUpTiempo = PowerUpTiempo.PowerUpTiempo(ImgPowerUpTiempo)
      PUpTiempo.rect.x = random.randrange(RangodeaparicionPUTiempo[0][0],RangodeaparicionPUTiempo[0][1])
      PUpTiempo.rect.y = random.randrange(RangodeaparicionPUTiempo[1][0],RangodeaparicionPUTiempo[1][1])
      Lista_PuTiempo.add(PUpTiempo)
      Lista_Todos_Sprites.add(PUpTiempo)
  
    for i in range (2): #VelocidadPowerUp
      PUpVelocidad = PowerUpVelocidad.PowerUpVelocidad(ImgPowerUpVelocidad)
      PUpVelocidad.rect.x = random.randrange(RangodeaparicionPUvelocudad[0][0],RangodeaparicionPUvelocudad[0][1])
      PUpVelocidad.rect.y = random.randrange(RangodeaparicionPUvelocudad[1][0],RangodeaparicionPUvelocudad[1][1])
      Lista_PuVelocidad.add(PUpVelocidad)
      Lista_Todos_Sprites.add(PUpVelocidad)
  
    for i in range (len(PosicionMetas)):
      Meta = Metas.Metas(ImgMeta, PosicionMetas[i], TamanoMetas[i])
      Lista_Metas.add(Meta)
      Lista_Todos_Sprites.add(Meta)

    Jugador = Boat() #Barco
    Lista_Todos_Sprites.add(Jugador)


    while Running: #Bucle de Juego

  
      #Texto
      TextoTemporizadorRender = FuenteTiempo.render(TextoContador.format(str(TiempoRestante)), 0, Negro)
  
      #Input 
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #Cerrar ventana
          sys.exit()
    
        if event.type == Timer_event:
          if InicioJuego: #Cuenta los segundos 1*1
            Cronometro += 1
            TiempoRestante -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
             print(pygame.mouse.get_pos()) #Para "desarrollo"

        if event.type == KEYDOWN: #Presiona
      
          if event.key == pygame.K_ESCAPE: #Otra forma de salir
            sys.exit()
        
          if event.key == pygame.K_n: #Siguiente nivel
            SiguienteNivel = True
          if event.key == pygame.K_r: #Siguiente nivel
            SiguienteNivel = True
            
          if event.key == pygame.K_LEFT:#Izquierda
            Izquierda = True
          if event.key == pygame.K_RIGHT:#Derecha
            Derecha = True
          if event.key == pygame.K_UP:#Avanza
            Adelante = True
            if not InicioJuego:
                InicioJuego = True
    
        if event.type == KEYUP: #Suelta
          
          if event.key == pygame.K_n: #Siguiente nivel
            SiguienteNivel = False
          if event.key == pygame.K_r: #Siguiente nivel
            SiguienteNivel = True
      
          if event.key == pygame.K_LEFT:#Izquierda
            Izquierda = False      
          if event.key == pygame.K_RIGHT:#Derecha
            Derecha = False
          if event.key == pygame.K_UP:#Avanza
            Adelante = False
  
      #Calcula el desplazamiento
      if Angulo > 360:
        Angulo -=360
      elif Angulo < 0:
          Angulo +=360
      if Adelante:
        if Velocidad < 0.375:
          Velocidad += 0.0005
      else:
        if Velocidad > 0:
          Velocidad -= 0.000416
      if Izquierda:
        Angulo += 0.5
      if Derecha:
        Angulo -= 0.25
    

      PosX += direccion.Movimiento(Angulo)[0]*Velocidad
      PosY += direccion.Movimiento(Angulo)[1]*Velocidad
      Jugador.rect.x = PosX
      Jugador.rect.y = PosY

      #Dibujar en pantalla
      Jugador.image = pygame.transform.rotate(Bote, Angulo)
  
      screen.fill(Azul) #Awua   
      screen.blit(Pista,(0,0))#Pista
      Lista_Todos_Sprites.draw(screen)#Piedras, Jugador, Tiempo, Ve;ocidad
      screen.blit(TextoTemporizadorRender,PosicionTemporizador)
  

  
     #Colisiones
      #Piedra
      if pygame.sprite.spritecollide(Jugador, Lista_Piedras, False, pygame.sprite.collide_mask):#Rocas
        Velocidad = 0
        PosX = PosicionInicial[0]
        PosY = PosicionInicial[1]
        Angulo = AnguloInicial
        Velocidad = 0
      #PUTiempo
      if pygame.sprite.spritecollide(Jugador, Lista_PuTiempo, True, pygame.sprite.collide_mask):#Tiempo
         TiempoRestante += 5
      #PUVelocidad
      if pygame.sprite.spritecollide(Jugador, Lista_PuVelocidad, True, pygame.sprite.collide_mask):#Tiempo
         Velocidad += 0.3
      #Pista
      if Mascara.overlap (Jugador.bmask, (PosX-0, PosY-0)): #Que no salga de la pista
         PosX = PosicionInicial[0]
         PosY = PosicionInicial[1]
         Angulo = AnguloInicial
      #Metas
      if pygame.sprite.spritecollide(Jugador, Lista_Metas, True, pygame.sprite.collide_mask):
        pass
      #Fin del juego
      if len(Lista_Metas) <= 0: #Victoria
        screen.fill(Blanco)
        screen.blit(TextoVictoriaRender, (187, 360))
        screen.blit(TextoIndicacionesVictoriaRender, (195,440))
        TiempoRestante = 100
        Victoria = 2
        if SiguienteNivel:
          Running = False
          continue
      if TiempoRestante <= 0: #Perdida
        PosX = 146
        PosY = 102
        Velocidad = 0
        screen.fill(Negro)
        screen.blit(TextoPerdidaRender, (187, 360))
        screen.blit(TextoIndicacionesDerrotaRender, (187,330))
        if SiguienteNivel:
          Running = False
          continue
        Victoria = 1

      pygame.display.update()
    return Victoria
