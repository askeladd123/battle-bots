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
    def __init__(self, image_sequence, position=(0, 0), size=(1, 1), rotation=0, speed=1):
        #polymorphic
        self.current_frame = 0.0
        self.speed = speed
        self.is_done = False

        self.image_sequence = [pygame.transform.scale(image, size) for image in image_sequence]
        self.position = position
        self.rotation = rotation

    def draw(self, display):
        i = int(self.current_frame)
        if self.is_done or len(self.image_sequence) - 1 < i:
            i = len(self.image_sequence) - 1
            self.is_done = True

        image = self.image_sequence[i]
        image = pygame.transform.rotate(image, self.rotation)
        display.blit(image, self.position)


class AnimationTrail:
    def __init__(self, base=(0, 0), tip=(4, 4), speed=1):
        #polymorphic
        self.current_frame = 0.0
        self.speed = speed
        self.is_done = False

        self.base = base
        self.tip = tip
        self.frames = 100

    def draw(self, display):
        i = int(self.current_frame)
        if self.is_done or self.frames < i:
            i = self.frames
            self.is_done = True

        v = 140 / (i * 0.25 + 1)
        pygame.draw.line(display, (v, v, v), self.base, self.tip, int(8 / (i * 0.25 + 1)))
        i = int(self.current_frame)


