import pygame, sys, direccion, random
from pygame.locals import *

#Inicializacion del juego
pygame.init()
Screen_size = (720, 720)
screen = pygame.display.set_mode(Screen_size)
Icono = pygame.image.load("Images\Icon32x32.JPEG")
pygame.display.set_icon(Icono)
pygame.display.set_caption("BOAT RACE")
FPS = pygame.time.Clock()
FPS.tick(60)

#Mouse invisible
#pygame.mouse.set_visible(0)

#variables que me salvan la vida
#Listas
Lista_Piedras = pygame.sprite.Group()
Lista_PuTiempo = pygame.sprite.Group()
Lista_Todos_Sprites = pygame.sprite.Group()
#Colores
Blanco = (255,255,255)
Negro = (0,0,0)
Rojo = (255,0,0)
Verde = (0,255,0)
Arena = (233,136,32)
#Imagenes
#BG_lvl_1 = pygame.image.load("Images\BG_Pista1.PNG").convert()
Img_Mask_G_lvl_1 = pygame.image.load("Images\BG_Pista1_Mask.PNG").convert()
Img_Mask_G_lvl_1.set_colorkey(Negro) 
Mascara = pygame.mask.from_surface(Img_Mask_G_lvl_1)
Nascara_img = Mascara.to_surface()
Bote = pygame.image.load("Images\Bote.PNG").convert()
Bote.set_colorkey(Negro)
#Control
Derecha = False
Izquierda = False
Adelante = False
#Posicion del bote
PosX = 167
PosY = 113
#Movimiento
Angulo = 90
Velocidad = 0.0

#OOP
class Obstaculos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("Images\Obstaculo.PNG").convert()
    self.image.set_colorkey(Negro)
    self.rect = self.image.get_rect()
   
class Tiempo(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("Images\TiempoPowerUp.PNG").convert()
    self.image.set_colorkey(Negro)
    self.rect = self.image.get_rect()
    
class Boat(pygame.sprite.Sprite):
   def __init__(self):
    super().__init__()
    self.image = Bote
    self.rect = self.image.get_rect()
    self.bmas = pygame.mask.from_surface(self.image)


#Crear cada instmacia, elemento individual 
for i in range (5): #Piedras
  Obstaculo = Obstaculos()
  Obstaculo.rect.x = random.randrange(270, 657)
  Obstaculo.rect.y = random.randrange(55, 168)
  Lista_Piedras.add(Obstaculo)
  Lista_Todos_Sprites.add(Obstaculo)
for i in range (2): #Tiempo
  PUpTiempo = Tiempo()
  PUpTiempo.rect.x = random.randrange(270, 657)
  PUpTiempo.rect.y = random.randrange(55, 168)
  Lista_PuTiempo.add(PUpTiempo)
  Lista_Todos_Sprites.add(PUpTiempo)
  
Jugador = Boat() #Barco
Lista_Todos_Sprites.add(Jugador)
while True: #Bucle de Juego
  
    #Input 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: #Cerrar ventana
      sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
         print(pygame.mouse.get_pos()) #Para "desarrollo"

    if event.type == KEYDOWN: #Presiona
      
      if event.key == pygame.K_ESCAPE: #Otra forma de salir
        sys.exit()
        
      if event.key == pygame.K_LEFT:#Izquierda
        Izquierda = True
      if event.key == pygame.K_RIGHT:#Derecha
        Derecha = True
      if event.key == pygame.K_UP:#Avanza
        Adelante = True
    
    if event.type == KEYUP: #Suelta
      
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


  #Dibujar en pantalla
  Jugador.rect.x = PosX
  Jugador.rect.y = PosY
  Jugador.image = pygame.transform.rotate(Bote, Angulo)
  #screen.blit(BG_lvl_1, (0,0)) #Fondo
  screen.fill(Arena)
  screen.blit(Img_Mask_G_lvl_1,(0,0))#Pista
  Lista_Todos_Sprites.draw(screen)#Piedras, Jugador, Tiempo
  
  

  
 #Colisiones
  if pygame.sprite.spritecollide(Jugador, Lista_Piedras, False):#Rocas
    Velocidad = 0
    PosX = 146
    PosY = 102
    Angulo = 90
    Velocidad = 0
  if pygame.sprite.spritecollide(Jugador, Lista_PuTiempo, True):#Tiempo
     pass
  if not Mascara.overlap (Jugador.bmas, (PosX-0, PosY-0)): #Que no salga de la pista
     PosX = 146
     PosY = 102
     Angulo = 90
     
  pygame.display.update()
