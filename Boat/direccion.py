import math as m

def cuad_uno(Angulo):
    Mov_x=m.sin(m.radians(Angulo))
    Mov_y=m.sin(m.radians(180-90-Angulo))
    return (Mov_x, Mov_y)

def cuad_cuatro(Angulo):
    Mov_y=m.sin(m.radians(Angulo))*-1
    Mov_x=m.sin(m.radians(180-90-Angulo))
    return (Mov_x, Mov_y)

def cuad_tres(Angulo):
    Mov_x=m.sin(m.radians(Angulo))*-1
    Mov_y=m.sin(m.radians(180-90-Angulo))*-1
    return (Mov_x, Mov_y)

def cuad_dos(Angulo):
    Mov_y=m.sin(m.radians(Angulo))
    Mov_x=m.sin(m.radians(180-90-Angulo))*-1
    return (Mov_x, Mov_y)

def Movimiento(Angulo):
    Desplazamiento = (0,0)
    if Angulo>0 and Angulo<90:
        Desplazamiento = cuad_uno(Angulo)
    elif Angulo>90 and Angulo<180:
        Desplazamiento = cuad_cuatro(Angulo-90)
    elif Angulo>180 and Angulo<270:
        Desplazamiento = cuad_tres(Angulo-180)
    elif Angulo>270 and Angulo<360:
        Desplazamiento = cuad_dos(Angulo-270)
    elif Angulo==0:
        Desplazamiento = (0,1)
    elif Angulo==90:
        Desplazamiento = (1,0)
    elif Angulo==180:
        Desplazamiento = (0,-1)
    elif Angulo==270:
        Desplazamiento = (-1,0)
    elif Angulo==360:
        Desplazamiento = (0,1)
    return Desplazamiento
    
