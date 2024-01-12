# DESAFIO 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3

import pygame

pygame.init()
pygame.mixer.music.load('clamojesus.mp3')
pygame.mixer.music.play()
pygame.event.wait()