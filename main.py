import pygame
import sys
import classJuego

pygame.init()

class eventosPygame:
    def __init__(self):
        self.exit = False
    def devolver(self):
        while True:
            mouse = [False, 0, 0]
            key = False
            Down = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    yield "exit", 0
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse[0] = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse[0] = False
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    Down = True
                elif event.type == pygame.KEYUP:
                    key = event.key
                    Down = False

            mouse[1], mouse[2] = pygame.mouse.get_pos()

            keyss = pygame.key.get_pressed()
            keys = []
            for x in range(len(keyss)):
                if keyss[x] == 1:
                    keys.append(x)

            yield mouse, [key, Down, keys]

def main():
    print "Welcome to this free kick game"
    print "Press space to shoot"
    print "Press the keys to select the initial direction and then the effect"
    print "Press 'R' to restart the shot"
    print "Press shift while pressing a key to change the direction faster"
    print "Enjoy!"

    pantalla = pygame.display.set_mode((800,600), pygame.HWSURFACE)
    
    pygame.display.set_caption("penalty soccer")
    reloj = pygame.time.Clock()
    eventos = eventosPygame()
    juego = classJuego.practica(-200, 200)
    ticks = False
    full = False
    for events in eventos.devolver():
        if events[0] == "exit":
            break
        if events[1][0] == pygame.K_r and events[1][1] == True:
            juego.__init__(-200,200)
        if events[1][1] == True and events[1][0] == pygame.K_F11:
            if full == False:
                pantalla = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                full = True
            else:
                pantalla = pygame.display.set_mode((800,600))
                full = False
        pantalla.fill((0, 255, 0))
       
        reloj.tick(40)
      
        juego.actualizar(pantalla, events[1])
        pygame.display.update()
    
    sys.exit()
    
main()
