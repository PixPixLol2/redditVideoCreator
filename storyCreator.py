import pygame
import time
import random

pygame.init()

# Youtube shorts width and height
SCREEN_W = 1080
SCREEN_H = 1920
# Background color
SCREEN_COLOR = (52, 235, 113)

# Image dementions
IMAGE_X = 287
IMAGE_Y = 856
IMAGE_W = 557
IMAGE_H = 312
# Loading images
IMAGE_1 = pygame.image.load("story1.png")
IMAGE_2 = pygame.image.load("story2.png")
IMAGE_3 = pygame.image.load("story3.png")
# List of the images
IMAGES_LIST = [IMAGE_1, IMAGE_2, IMAGE_3]


# Canvas
canvas = pygame.display.set_mode((SCREEN_W, SCREEN_H))
canvas.fill(SCREEN_COLOR)
pygame.display.flip()

# Title
pygame.display.set_caption("Reddit Story")
exit = False


# Picking random images from the given list
def pickNewImage(t):
    image = random.choice(IMAGES_LIST)
    rect = image.get_rect(center=(IMAGE_X, IMAGE_Y))
    canvas.fill(SCREEN_COLOR)
    canvas.blit(image, rect)
    pygame.display.flip()

exit = False

# Exit stuff
lastTime = time.time()
interval = 15

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            
    currentTime = time.time()
    
    if currentTime - lastTime >= interval:
        pickNewImage()
        lastTime = currentTime
        
    pygame.display.update()