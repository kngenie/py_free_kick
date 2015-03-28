import pygame
import imagenes
import sprite
import math
import time





class objetoSprite:
    def __init__(self,imagen,x = 0,y = 0,rects = False):
        self.sprite = sprite.sprite(imagen,0,0,rects)
        self.camX = 0
        self.camY = 0
        self.x = x
        self.y = y
    def actualizar(self,pantalla):
        self.sprite.x = self.x-self.camX
        self.sprite.y = self.y-self.camY
        self.sprite.pintar(pantalla)
    

class arco:
    def __init__(self):
        self.arco = objetoSprite(imagenes.arco)
        self.arco2 = objetoSprite(imagenes.arco2)
        self.arco3 = objetoSprite(imagenes.arco3)
        self.arco.x = 375
        self.arco.y = 180
        self.arco2.x = 375
        self.arco2.y = 180
        self.arco3.x = 375
        self.arco3.y = 180
        self.arcoo = 0
    def actualizar(self,pantalla,camX,camY):
        self.arco.camX = camX
        self.arco.camY = camY
        self.arco2.camX = camX
        self.arco2.camY = camY
        self.arco3.camX = camX
        self.arco3.camY = camY
        if self.arcoo  ==0:
            self.arco.actualizar(pantalla)
        elif self.arcoo < 4:
            self.arco2.actualizar(pantalla)
            self.arcoo+=1
        elif self.arcoo <8:
            self.arco3.actualizar(pantalla)
            self.arcoo+=1
        else:
            self.arcoo =0 
            self.arco3.actualizar(pantalla)
class cancha:
    def __init__(self):
        self.arco = objetoSprite(imagenes.cancha)
        self.arco.x = 750+750/2
        self.arco.y = 750
    def actualizar(self,pantalla,camX,camY):
        self.arco.camX = camX
        self.arco.camY = camY
        self.arco.actualizar(pantalla)
        
class pelota:
    def __init__(self,x = 0,y = 0):
        self.pelota = objetoSprite(imagenes.pelota)
        self.sombra = objetoSprite(imagenes.sombra)
        self.x = x
        self.y = y
        self.altura = 0
        self.subir = 0
        self.adelante = 0
        self.derecha = 0
        self.power = 0
        self.efecto = 0
        self.fuerza = 0
        self.angulo = 0
        self.freeze = True
        self.anguloH = 30
        self.subirr = 0
        self.gol = False
        self.tocada = False
            
    def actualizar(self,pantalla,camX,camY,arco,arquero):
        
        if self.freeze == False:
            self.avanzar(pantalla,camX,camY,arco,arquero)
        else:
            self.sombra.camX = camX-800/2
            self.sombra.camY = camY-600/2
            self.pelota.camX = camX-800/2
            self.pelota.camY = camY-600/2
            self.sombra.x = self.x
            self.sombra.y = self.y+5
            self.pelota.x = self.x
            self.pelota.y = self.y+self.altura
        
            self.sombra.actualizar(pantalla)
            self.pelota.actualizar(pantalla)
    def avanzar(self,pantalla,camX,camY,arco,arquero):
        self.sombra.camX = camX-800/2
        self.sombra.camY = camY-600/2
        self.pelota.camX = camX-800/2
        self.pelota.camY = camY-600/2
        self.sombra.x = self.x
        self.sombra.y = self.y+5
        self.pelota.x = self.x
        self.pelota.y = self.y+self.altura
        if self.y <-10 and self.y >=-80 and self.gol == False and self.tocada == False:
            j = self.y
            self.y = -75
            if arquero.sprite.colicionar(self.pelota.sprite) == True:
                self.angulo-= 180
                self.y = -45
                self.efecto = 0
                self.fuerza = self.fuerza*0.5
 
                self.tocada = True
            else:
                self.y = j
        self.sombra.actualizar(pantalla)
        self.pelota.actualizar(pantalla)
        self.x+= -self.derecha*self.power
        self.y+= -self.adelante*self.power
        self.altura+= -self.subir
        
        if self.power <0:
            self.power = 0
        else:
            self.power -=0.005
        if self.altura >=0:
            
            self.subir = -self.subir*0.25
        
          
        self.adelante = math.sin(math.radians(self.angulo))*self.fuerza
        self.derecha = math.cos(math.radians(self.angulo))*self.fuerza
            
        
        if self.y < -70 and self.y >-160 and self.x >100 and self.x <135   and self.altura >-100:
        
            self.angulo -= (self.x-100)/35*360
         
            self.y = -60
           
            self.fuerza = self.fuerza*0.5
         
            
            self.efecto = 0
        elif self.y < -70 and self.y >-160 and self.x <-160 and self.x >-195  and self.altura >-100:
            self.angulo -=(self.x+195)/35*360
            self.y = -70
            self.efecto = 0
            self.fuerza = self.fuerza*0.5
            self.efecto = 0
        elif self.y < -70 and self.y >-160 and self.x >-195 and self.x<100 and self.altura<=-115 and self.altura >-125:
            self.y = -70  
            self.efecto = 0
           
            
            self.angulo -= 180
            self.fuerza = self.fuerza*0.5
            self.efecto = 0
        elif self.y <=-70 and self.y >=-160 and self.x <=100 and self.x >=-195  and self.altura <=-100 and self.altura > -115 and self.gol == False:
            
            
            self.subir = -20
            self.fuerza = self.fuerza*0.1

            self.y = -60
            
             
        elif self.y <=-80 and self.y >=-160 and self.x <=135 and self.x >=-160  and self.altura >-100:
            
            self.angulo-=180
            self.fuerza = self.fuerza*0.1
            self.y = -77
            self.power = self.power*0.3
            arco.arcoo = 1
            self.efecto = 0
            self.gol = True
            self.subir = 0
            
        
        self.adelante = math.sin(math.radians(self.angulo))*self.fuerza
        self.derecha = math.cos(math.radians(self.angulo))*self.fuerza
        
 
        if self.altura<0:
            self.subir-= 0.5
            
       
        self.angulo+=self.efecto
        
        
class arquero:
    def __init__(self):
        self.arqueros = []
        self.arqueros.append(objetoSprite(imagenes.arqueros[0],350,200,[[75,10,25,110],[60,60,20,40],[100,60,20,40]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[1],350,200,[[60,10,35,110],[35,45,25,25]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[2],350,200,[[60,10,35,110],[95,45,25,25]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[3],350,200,[[20,80,110,30],[20,60,50,20]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[4],350,200,[[30,80,110,30],[90,60,50,20]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[5],350,200,[[55,0,30,110],[85,0,25,50]]))
        self.arqueros.append(objetoSprite(imagenes.arqueros[6],350,200,[[75,0,30,110],[50,0,25,50]]))
        self.altura = 0
        self.xPos = 0
        self.saltando = [0,0]
        self.actual = 0
        self.mov = 0
        self.wait =0 
        self.tirando = False
        self.moviendose = 0
        self.subir = 0
        self.wa = 0
        self.sumX = 0
    def actualizar(self,pantalla,camX,camY):
        for x in range(len(self.arqueros)):
            self.arqueros[x].camX = camX
            self.arqueros[x].camY = camY
            self.arqueros[x].x = 350+self.xPos
            self.arqueros[x].y = 200-self.altura
        self.arqueros[self.actual].actualizar(pantalla)
        
        if self.subir >0 or self.sumX > 0:
            self.altura+=self.subir
            self.xPos+=self.sumX
            self.subir = int(self.subir/2)
            self.sumX = int(self.sumX/2)
            
        else:
            
            if self.altura >0:
                self.altura-=5
                self.wa = 100
            if self.altura <=0:
                self.wa-=1
                if self.wa == 0:
                    self.actual = 0 
       

    def saltar(self,lado,altura,cantX):
        if altura > 200 and lado == 0:
            self.subir = altura/2
            self.actual = 5
            self.sumX = cantX/2
        elif lado == 1:
            self.actual = 3
            self.subir = altura/2
            self.sumX = cantX/2
        elif lado == 2:
            self.actual = 4
            self.subir = altura/2
            self.sumX = cantX/2
            
    def moverse(self,lado):
        
        if self.wait == 0 and self.mov == 0 and self.moviendose == 0:
            self.mov = lado*5
        self.xPos+=self.mov
    def tirarse(self,lado):
        self.tirando = True
        
        if lado == 1:
            self.actual = 4
                
        else:
            self.actual = 3
         
class IADA:
    def __init__(self,arquero,ball):
        self.arquero = arquero
        self.num = 0
        self.saltado = False
        self.ball = ball
        self.xPoint = []
    def actualizar(self):
        """
        if self.ball.y <0:
            if self.arquero.xPos -25-350 > self.ball.y:
                self.arquero.tirarse(1, -self.ball.altura)
            if self.arquero.xPos+25-350 < self.ball.y:
                self.arquero.tirarse(-1,-self.ball.altura)
        """
        if self.ball.angulo != 0:
           
            distance = self.ball.y+75
            
            angle = self.ball.angulo-90
            
            CM = math.tan(math.radians(angle))*distance
            
            posD = int(self.ball.x+CM)+30
           
            if posD > self.arquero.xPos+10 and  posD >-200 and posD <150:
                self.arquero.moverse(1)
    
            elif posD < self.arquero.xPos-10 and  posD >-200 and posD <150:
                self.arquero.moverse(-1)
            #print self.xPoint[len(self.xPoint)-1]
            #print self.xPoint[0]
        if self.ball.y < 0  and self.saltado == False:
            
            self.arquero.saltar(1,70,-50)

            self.saltado = True
class flecha:
    def __init__(self,pelotaX,pelotaY):
        self.flecha = sprite.sprite(imagenes.flecha,400,370)
        self.jugadores = []
        
        for x in range(3):
            self.jugadores.append(objetoSprite(imagenes.jugadores[x],pelotaX+370,pelotaY+250))
        self.angulo = 0
        self.de = False
        self.iz = False
        self.num = 0
        self.flecha.generarRotados()
        self.disparado = False
        self.remate = False
        self.imagesBarra = []
        for x in range(110):
            self.imagesBarra.append(pygame.transform.scale(imagenes.barra,(x*3,3)))
        self.barra = sprite.sprite(self.imagesBarra[0],50,500)
        self.cargando = False
        self.imageBarra = 0
        self.efecto = 0
        self.press = False
        self.subir = 1
    def actualizar(self,pantalla,key,camX,camY):  
        """    
        if key[1] != None:
            if key[1] == True:
                
                if key[0] == pygame.K_LEFT:
                    self.iz = True
                if key[0] == pygame.K_RIGHT:
                    self.de = True
                if key[0] == pygame.K_SPACE:
                    self.cargando = True
            if key[1] == False and key[0] != None:
               
                if key[0] == pygame.K_LEFT:
                    self.iz = False
                if key[0] == pygame.K_RIGHT:
                    self.de = False
                if key[0] == pygame.K_SPACE:
                    self.cargando = False
                    self.disparado = True
        """
        self.iz = False
        self.de = False  
        space = False
        for x in range(len(key[2])):
            if key[2][x] == pygame.K_LEFT:
                self.iz = True
            if key[2][x] == pygame.K_RIGHT:
                self.de = True
            if key[2][x] == pygame.K_SPACE:
                space = True
                
        if space == True:
            self.cargando = True
        elif self.cargando == True:
            self.cargando = False
            self.disparado = True
            self.press = True
        if self.de == True and self.cargando == False:
            self.flecha.x+=1
            self.angulo+=1
            for x in range(len(key[2])):
                if key[2][x] == pygame.K_LSHIFT or key[2][x] == pygame.K_RSHIFT:
                    self.flecha.x+=5
                    self.angulo+=5
        if self.iz == True and self.cargando == False:
            for x in range(len(key[2])):
                if key[2][x] == pygame.K_LSHIFT or key[2][x] == pygame.K_RSHIFT:
                    self.flecha.x-=5
                    self.angulo-=5
            self.flecha.x-=1
            self.angulo-=1
        if self.remate == False and self.imageBarra == 0:
            self.flecha.pintar(pantalla)
        if self.cargando == True and self.imageBarra <90:
            self.barra.imagen = self.imagesBarra[int(self.imageBarra)]
            self.imageBarra +=3
            
        self.actualizarJ(pantalla, key, camX, camY)
       
        self.barra.pintar(pantalla)
    def actualizarJ(self,pantalla,key,camX,camY):   
        
        self.jugadores[int(self.num)].camX = camX
        self.jugadores[int(self.num)].camY = camY
        self.jugadores[int(self.num)].actualizar(pantalla)
        
        
        if self.disparado == True and self.num < 2:
            for x in range(len(key[2])):
                if key[2][x] == pygame.K_LEFT:
                    self.efecto-=0.1
                elif key[2][x] == pygame.K_RIGHT:
                    self.efecto+=0.1
                if key[2][x] == pygame.K_UP:
                    self.subir +=0.5
                elif key[2][x] == pygame.K_DOWN:
                    self.subir -=1
            
                    
            
            self.num+=0.05
        
        
         
            
        if self.num >1 and self.num <2:
            self.num+=0.25  
            
    
        if self.num >= 1 and self.num <1.5:
            self.remate = True                
class practica:
    def __init__(self,x = 100,y = 1000):
        self.cancha = cancha()
        self.arco = arco()
        self.pelota = pelota(x,y)
        self.camX = 0
        self.camY = 0
        self.start = False
        self.seconds = 50
        self.x = x
        self.y = y
        self.j = False
        self.flecha = flecha(x,y)
        self.arquero = arquero()
        self.IA = IADA(self.arquero,self.pelota)
    def mov(self):
        if self.seconds >0:
            self.seconds-=1
        else:
            end = True
            if self.camX > self.x:
                self.camX-=10
                end = False
            if self.camX < self.x:
                self.camX+=10
                end = False
            if self.camY > self.y-100:
                self.camY-=10
                end = False
            if self.camY < self.y-100:
                self.camY+=10
                end = False
            
            
            if end == True:
                self.start = True
                self.j = True
    def actualizar(self,pantalla,key):
        
        self.cancha.actualizar(pantalla,self.camX,self.camY)
        
        
        if self.pelota.y <=-80:
            
            
            
            self.arco.actualizar(pantalla, self.camX, self.camY)
            self.arquero.actualizar(pantalla, self.camX, self.camY)
            self.pelota.actualizar(pantalla,self.camX,self.camY,self.arco,self.arquero.arqueros[self.arquero.actual])
        else:
            
            self.arco.actualizar(pantalla, self.camX, self.camY)
            
            self.pelota.actualizar(pantalla,self.camX,self.camY,self.arco,self.arquero.arqueros[self.arquero.actual])
            self.arquero.actualizar(pantalla, self.camX, self.camY)
        self.IA.actualizar()
        
        if self.start == True:
            if self.pelota.sombra.sprite.y<400 and self.camY >0:
                self.camY-=self.pelota.fuerza+4
            
            if self.pelota.sombra.sprite.x > 600 and self.camX <300:
                self.camX+=self.pelota.fuerza+4
            if self.pelota.sombra.sprite.x <200 and self.camX >-300:
                self.camX-=self.pelota.fuerza+4
        
        
        
        if self.start == False:
            self.mov()
            self.flecha.actualizarJ(pantalla, key, self.camX, self.camY)
        
        else:
            if self.j == True:
                """
                self.pelota.fuerza = 2
                self.pelota.power = 10
                self.pelota.angulo = 100
                self.pelota.efecto = -3
                self.pelota.subir = 29
                """
                self.flecha.actualizar(pantalla, key,self.camX,self.camY)
                
                
                if self.flecha.remate == True:
                    self.pelota.angulo = self.flecha.angulo/2+90
                    self.pelota.freeze = False
                    self.pelota.power = 3
                    
                    self.pelota.subir = 10
                    self.pelota.efecto = self.flecha.efecto
                    
                    self.pelota.fuerza = self.flecha.imageBarra/4*math.sin(math.radians(30))
                    
                    self.pelota.subir = self.flecha.subir+self.flecha.imageBarra/4
                    
                    if self.pelota.subir <0:
                        self.pelota.subir = 0
                   
                    self.flecha.remate = False
        
        
            
             
