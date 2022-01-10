import pygame
from common import get_unit_vector


class Player:
    def __init__(self, function, tiles):
        self.function = function
        self.image = pygame.transform.scale(pygame.image.load("res/tank.png"), (tiles.TILE_WIDTH, tiles.TILE_HEIGHT))
        self.position = [1, 1]
        self.tiles = tiles
        self.rotation = 0
        self.impact_location = (0, 0)
        self.has_shot = False
        self.font = None
        self.ammo = 0
        self.ammo_max = 1

    def draw(self, display):
        self.image = pygame.transform.rotate(self.image, self.rotation)
        display.blit(self.image, self.tiles.world_position(self.position))
        display.blit(self.font, self.tiles.world_position(self.position))
        self.image = pygame.transform.rotate(self.image, -self.rotation)

    def move(self, string):
        self.tiles.unregister(self.position)
        if string == "up":
            if self.tiles.is_empty(self.position[0], self.position[1] - 1):
                self.position[1] -= 1
            self.rotation = 0
        if string == "down":
            if self.tiles.is_empty(self.position[0], self.position[1] + 1):
                self.position[1] += 1
            self.rotation = 180
        if string == "left":
            if self.tiles.is_empty(self.position[0] - 1, self.position[1]):
                self.position[0] -= 1
            self.rotation = 90
        if string == "right":
            if self.tiles.is_empty(self.position[0] + 1, self.position[1]):
                self.position[0] += 1
            self.rotation = 270
        self.tiles.register(self.position)

    def extract_impact_location(self):
        self.has_shot = False
        return self.impact_location

    def extract_impact_world_location(self):
        location = self.extract_impact_location()
        return location[0] * self.tiles.TILE_WIDTH, location[1] * self.tiles.TILE_HEIGHT

    def shoot(self, string=None):
        if self.ammo == 0:
            print("I'm sorry, but you're out of ammo. ")
            return
        self.ammo -= 1
        if string is not None:
            self.rotate(string)

        direction = get_unit_vector(self.rotation)
        x = self.position[0]
        y = self.position[1]

        x += direction[0]
        y += direction[1]
        while self.tiles.is_empty(x, y):
            x += direction[0]
            y += direction[1]
        x -= direction[0]
        y -= direction[1]

        self.impact_location = (x, y)
        self.has_shot = True

    def rotate(self, string):
        if string == "up":
            self.rotation = 0

        if string == "down":
            self.rotation = 180

        if string == "left":
            self.rotation = 90

        if string == "right":
            self.rotation = 270
