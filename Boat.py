import Juego
import pygame
#Variables no tan variables
#Control
Victoria = 1

#Imagenes
RutaNivel1 = "Images\BG_Pista1_Mask.PNG"
RutaNivel2 = "Images\BG_Pista2_Mask.PNG"
RutaNivel3 = "Images\BG_Pista3_Mask.PNG"
#Caracteristicas del nivel
#Tiempo 
TiempoNivel1 = 30
TiempoNivel2 = 45
TiempoNivel3 = 30
#Posicion del bote
PosicionInicialBoteLv1 = (167,113)
PosicionInicialBoteLv2 = (240,72)
PosicionInicialBoteLv3 = (109,115)
AnguloInicialLv1 = 90
AnguloInicialLv2 = 90
AnguloInicialLv3 = 0
#Metas
PosicionMetasLv1 =[(530,221),(310,308),(120,55)]
TamanoMetasLv1 = [(128,16),(34,152),(32,119)]

PosicionMetasLv2 = [(381,183),(107,326),(508,537)]
TamanoMetasLv2 = [(36,113),(99,36),(65,36)]

PosicionMetasLv3 = [(61,427),(368,66),(627,518)]
TamanoMetasLv3 = [(113,36),(36,127),(36,138)]
#Rocas
RangodeaparicionRocasLv1 = [(270,657),(55,168)]
RangodeaparicionPUTiempoLv1 = [(270,657),(55,168)]
RangodeaparicionPUvelocudadLv1 = [(270,657),(55,168)]

RangodeaparicionRocasLv2 = [(193,526),(196,287)]
RangodeaparicionPUTiempoLv2 = [(543,613),(239,446)]
RangodeaparicionPUvelocudadLv2 = [(800,810),(55,168)]

RangodeaparicionRocasLv3 = [(456,542),(79,616)]
RangodeaparicionPUTiempoLv3 = [(78,153),(170,581)]
RangodeaparicionPUvelocudadLv3 = [(248,325),(226,565)]

#General(RutaPista,  PosicionInicial,Tiempo, PosicionMetas, TamanoMetas, RangodeaparicionRocas. RangodeaparicionPUTiempo, RangodeaparicionPUvelocudad)
while Victoria != 2: 
    Victoria = Juego.Nivel(RutaNivel1, PosicionInicialBoteLv1, AnguloInicialLv1, TiempoNivel1, PosicionMetasLv1, TamanoMetasLv1, RangodeaparicionRocasLv1, RangodeaparicionPUTiempoLv1, RangodeaparicionPUvelocudadLv1)
Victoria = 0
while Victoria != 2:
    Victoria = Juego.Nivel(RutaNivel2, PosicionInicialBoteLv2, AnguloInicialLv2, TiempoNivel2, PosicionMetasLv2, TamanoMetasLv2, RangodeaparicionRocasLv2, RangodeaparicionPUTiempoLv2, RangodeaparicionPUvelocudadLv2)
Victoria = 0
while Victoria != 2:
    Victoria = Juego.Nivel(RutaNivel3, PosicionInicialBoteLv3, AnguloInicialLv3, TiempoNivel3, PosicionMetasLv3, TamanoMetasLv3, RangodeaparicionRocasLv3, RangodeaparicionPUTiempoLv3, RangodeaparicionPUvelocudadLv3)

