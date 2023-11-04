import pygame
class Metas(pygame.sprite.Sprite):
  def __init__(self,Imagen,Posicion,Dimension):
    super().__init__()
    self.image = pygame.transform.scale(Imagen,Dimension)
    self.rect = self.image.get_rect()
    self.rect.x = Posicion[0]
    self.rect.y = Posicion[1]
    