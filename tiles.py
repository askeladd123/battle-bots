import pygame
import random


class Tiles:
    def __init__(self, width, height):
        self.TILE_WIDTH = width / self.WIDTH
        self.TILE_HEIGHT = height / self.HEIGHT
        self.image = pygame.transform.scale(pygame.image.load("res/mur.png"), \
                                            (self.TILE_WIDTH + 2, self.TILE_HEIGHT + 2))

        # DEKLARERE ARRAY
        self.array = []
        value = 0
        for i in range(self.WIDTH):
            temp = []
            for j in range(self.HEIGHT):
                temp.append(value)
            self.array.append(temp)

        # KANTENE
        for i in range(self.WIDTH):
            self.array[i][0] = 1
        for i in range(self.WIDTH):
            self.array[i][self.HEIGHT - 1] = 1
        for i in range(self.HEIGHT):
            self.array[0][i] = 1
        for i in range(self.HEIGHT):
            self.array[self.WIDTH - 1][i] = 1

        # GENERER LABYRINT
        roots = random.randint(10, 18)
        for i in range(roots):
            current = [random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)]
            root_length = random.randint(0, 20)
            while self.inbounds(current) and 0 < root_length:
                root_length -= 1
                self.array[current[0]][current[1]] = 1
                direction = random.choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
                current[0] += direction[0]
                current[1] += direction[1]

    def inbounds(self, position):
        return 0 <= position[0] < self.WIDTH and \
               0 <= position[1] < self.HEIGHT

    def draw(self, display):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if self.array[i][j] == 1:
                    display.blit(self.image, self.world_position((i, j)))

    def world_position_x(self, x):
        return self.X + x * self.TILE_WIDTH

    def world_position_y(self, y):
        return self.Y + y * self.TILE_HEIGHT

    def world_position(self, indexes):
        return self.world_position_x(indexes[0]), self.world_position_y(indexes[1])

    def is_empty(self, x, y):
        return self.array[x][y] == 0

    def register(self, position):
        #array(self.player_ids[player_reference]
        self.array[position[0]][position[1]] = 2

    def unregister(self, position):
        #array(self.player_ids[player_reference]
        self.array[position[0]][position[1]] = 0

    def random_direction(self):
        r = random.randint(1, 4)
        if r == 1:
            return (0, -1)
        if r == 2:
            return (1, 0)
        if r == 3:
            return (0, 1)
        if r == 4:
            return (-1, 0)


    #player_ids = {}

    X = 0
    Y = 0
    WIDTH = 24
    HEIGHT = 12
