import pygame
class PowerUpTiempo(pygame.sprite.Sprite):
  def __init__(self,Imagen):
    super().__init__()
    self.image = pygame.transform.scale(Imagen,(28,28))
    self.image.set_colorkey((0,0,0))
    self.rect = self.image.get_rect()



