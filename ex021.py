# Exercicio - Curso em vídeo - Exercício 021
# Função: Abrir e reproduzir um áudio de um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()