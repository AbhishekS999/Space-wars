import pygame 
pygame.init()
import UFO_Game as main
import tkinter

# get resolution of user pc
r = tkinter.Tk()
w = r.winfo_screenwidth()
h = r.winfo_screenheight()
w -= 5
h -= 5

wn = pygame.display.set_mode((w, h), pygame.FULLSCREEN, 32)

main.menu()