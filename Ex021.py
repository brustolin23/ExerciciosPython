# Faça um programa em Python que abra e reproduza um áudio de arquivo mp3
# A biblioteca externa selecionada foi o Pygame
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music/exe021.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
input("Pressione enter para encerrar")
pygame.mixer.music.stop()
