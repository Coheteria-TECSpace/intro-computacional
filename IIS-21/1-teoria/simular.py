from vuelo import cohete
import pygame, sys, time       # OJO TIENEN QUE INSTALAR PYGAME !!!!!!!!!

cuete = cohete(peso=1000,pprop=500)
cuete.setNprop("Candy")
#cuete.printInfo()
# pedir al cohete que simule 1/30s de vuelo
#    cuete.iterarVuelo(1/30.0)
#    cuete.printInfo()
#    time.sleep(1/30.0)

resolucion = w,h = 800,600
size_cuete = 100,100
pos = [resolucion[0]/2-size_cuete[0]/2,resolucion[1]-size_cuete[1]]
pantalla = pygame.display.set_mode(resolucion)

cueteimg = pygame.image.load("cohete.png")
cueteimg = pygame.transform.scale(cueteimg, size_cuete)
cueteRotado = cueteimg
cueterec = pygame.Rect(pos[0], pos[1] ,100,100)
angulo = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # aumenta la velocidad del cohete
    if cuete.getPprop() > 0: cuete.iterarVuelo(1)

    if cueterec[0] < resolucion[0] and cueterec[1] > 0:
        cueterec = cueterec.move(cuete.getVel()[0],-1*cuete.getVel()[1])
        cueteRotado = pygame.transform.rotate(cueteimg, angulo)
        if angulo > -80: angulo -= 1
    else:
        #cueterec.move_ip(0,resolucion[1])
        cueterec.update(0,resolucion[1],100,100)

    pantalla.fill((0,0,0))
    pantalla.blit(cueteRotado,cueterec)
    pygame.display.flip()
    time.sleep(0.1)
