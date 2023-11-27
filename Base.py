import pygame
pygame.init()

#Colores
negro=(0,0,0)
azul=(0,0,255)
verde=(0,255,0)
rojo=(255,0,0)
blanco=(255,255,255)

ancho_ven=720
largo_ven=720
size=(ancho_ven,largo_ven) #Dimensiones de la ventana
ventana=pygame.display.set_mode(size)
clock=pygame.time.Clock() #Permite controlar los FPS

game_over=False

fondo=pygame.image.load("Fondo.png").convert() #Pixeles de la imagen deben coincidir con la ventana

while not game_over:                 #Bucle del juego
    for event in pygame.event.get(): #Eventos del juego
        #print(event)                #Muestra el evento en la consola
        if event.type==pygame.QUIT:  #Cerrar la ventana
            game_over=True
    
    ventana.blit(fondo, [0,0]) #Fondo
        
    pygame.display.flip() #Actualiza la ventana
    clock.tick(60) #FPS

pygame.quit()