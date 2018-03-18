import pygame
import requests
import sys
import os
MAX = 120
MIN = 0.00025
fps = 5
clock = pygame.time.Clock()
cords = input("��������� 1 � 2 � ����� ������� ").split(',')
mashtab = input('������ ����� ������� ').split(',')
response = None
def map_creat():
    try:
        map_request = "http://static-maps.yandex.ru/1.x/?ll="+cords[0]+","+cords[1]+"&spn="+mashtab[0]+","+mashtab[1]+"&l=map"
        response = requests.get(map_request)

        if not response:
            print("������ ���������� �������:")
            print(map_request)
            print("Http ������:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("������ �� ������� ���������. ��������� ������� ���� ��������.")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("������ ������ ���������� �����:", ex)
        sys.exit(2)
    return map_file
pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if float(mashtab[0])*2 < MAX and float(mashtab[1])*2 < MAX:
                    mashtab[0] = str(float(mashtab[0])*2)
                    mashtab[1] = str(float(mashtab[1])*2)
            if event.key == pygame.K_PAGEDOWN:
                if float(mashtab[0])/2 > MIN and float(mashtab[1])/2 > MIN:
                    mashtab[0] = str(float(mashtab[0])/2)
                    mashtab[1] = str(float(mashtab[1])/2)
            print(mashtab)

    screen.blit(pygame.image.load(map_creat()), (0, 0))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

os.remove(map_creat())