import pygame
import random

def get_unit_vector(angle):
    if angle == 0:
        return 0, -1

    if angle == 180:
        return 0, 1

    if angle == 90:
        return -1, 0

    if angle == 270:
        return 1, 0

def get_neighbours(vector):
    neighbours = []
    neighbours.append([vector[0] + 1, vector[1]])
    neighbours.append([vector[0] - 1, vector[1]])
    neighbours.append([vector[0], vector[1] + 1])
    neighbours.append([vector[0], vector[1] - 1])
    return neighbours


def random_legal_position(tiles):
    position = [random.randint(1, tiles.WIDTH - 1), random.randint(1, tiles.HEIGHT - 1)]
    while not tiles.is_empty(position[0], position[1]):
        position = [random.randint(1, tiles.WIDTH - 1), random.randint(1, tiles.HEIGHT - 1)]
    return position


class Animation:
    def __init__(self, size=(100, 100)):
        self.size = size
        self.frames = []
        self.speed = 1
        self.current_frame = 0.0
        self.position = (0, 0)
        self.rotation = 0
        self.rotation_offset = 0
        self.is_done = False

    def add_frame(self, image_path):
        self.frames.append(pygame.transform.scale(pygame.image.load(image_path), self.size))

    def draw_frame(self, display):
        image = self.frames[int(self.current_frame)]
        image = pygame.transform.rotate(image, self.rotation + self.rotation_offset)
        display.blit(image, self.position)

    def move(self, step=None):
        if len(self.frames) - 1 <= self.current_frame:
            self.is_done = True
        elif step == None:
            self.current_frame += self.speed
        else:
            self.current_frame += step

    def reset(self):
        self.is_done = False
        self.current_frame = 0

    def cycle(self, step):
        self.current_frame += step
        self.current_frame = self.current_frame % len(self.frames)