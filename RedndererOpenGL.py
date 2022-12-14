from pickle import TRUE
import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(negative_vertex_shader, negative_fragment_shader)

rend.target.z = -5

face = Model("model.obj", "model.bmp")

face.position.z -= 5
face.scale.x = 2
face.scale.y = 2
face.scale.z = 2


rend.scene.append( face )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            elif event.key == pygame.K_y:
                rend.filledMode()
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_c:
                rend.filledMode()
                rend.setShaders(glow_vertex_shader, glow_fragment_shader)
            elif event.key == pygame.K_v:
                rend.filledMode()
                rend.setShaders(toon_r_glow_vertex_shader, toon_r_glow_fragment_shader)
            elif event.key == pygame.K_b:
                rend.filledMode()
                rend.setShaders(toon_vertex_shader, toon_fragment_shader)




    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_e]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime


    if keys[K_w]:
        if rend.camPosition.y < 2:
            rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        if rend.camPosition.y > -2:
            rend.camPosition.y -= 5 * deltaTime


    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
