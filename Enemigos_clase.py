import pygame
class Monstruo:
    def __init__(self, dificultad, nivel, *sprites):
        self.nivel = nivel
        self.dificultad = dificultad
        self.sprites = list(sprites)

    def get_dificultad(self):
        return self.dificultad
    def get_nivel(self):
        return self.nivel
    def get_sprite(self):
        return self.sprites[self.nivel]
    
    def set_dificultad(self, nueva):
        self.dificultad = nueva
    def set_nivel(self, nueva):
        self.nivel = nueva