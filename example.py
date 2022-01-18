import BattleBots
import random


b = (0, 0)


@BattleBots.register_ai
def super_ai(input):

    command = ""

    if input.ammo == 0 < len(input.bullet_positions):
        a = input.position
        global b

        if a[0] < b[0]:
            command = "right"

        elif b[0] < a[0]:
            command = "left"

        elif a[1] < b[1]:
            command = "down"

        elif b[1] < a[1]:
            command = "up"

        if not input.is_legal(command):
            b = input.bullet_positions[random.randint(0, len(input.bullet_positions) - 1)]

    else:
        a = input.position
        b = input.enemy_positions[0]

        if a[1] < b[1]:
            command = "down"

        elif b[1] < a[1]:
            command = "up"

        elif a[1] == b[1]:
            if a[0] < b[0]:
                command = "shoot right"

            else:
                command = "shoot left"

    return command


c = (0, 0)


@BattleBots.register_ai
def super_ai(input):

    command = ""

    if input.ammo == 0 < len(input.bullet_positions):
        a = input.position
        global c

        if a[0] < c[0]:
            command = "right"

        elif c[0] < a[0]:
            command = "left"

        elif a[1] < c[1]:
            command = "down"

        elif c[1] < a[1]:
            command = "up"

        if not input.is_legal(command):
            c = input.bullet_positions[random.randint(0, len(input.bullet_positions) - 1)]

    else:
        a = input.position
        b = input.enemy_positions[0]

        if a[1] < b[1]:
            command = "down"

        elif b[1] < a[1]:
            return "up"

        elif a[1] == b[1]:
            if a[0] < b[0]:
                command = "shoot right"

            else:
                command = "shoot left"

    return command


d = (0, 0)


@BattleBots.register_ai
def super_ai(input):

    command = ""

    if input.ammo == 0 < len(input.bullet_positions):
        a = input.position
        global d

        if a[0] < d[0]:
            command = "right"

        elif d[0] < a[0]:
            command = "left"

        elif a[1] < d[1]:
            command = "down"

        elif d[1] < a[1]:
            command = "up"

        if not input.is_legal(command):
            d = input.bullet_positions[random.randint(0, len(input.bullet_positions) - 1)]

    else:
        a = input.position
        d = input.enemy_positions[0]

        if a[1] < d[1]:
            command = "down"

        elif d[1] < a[1]:
            return "up"

        elif a[1] == d[1]:
            if a[0] < d[0]:
                command = "shoot right"

            else:
                command = "shoot left"

    return command


BattleBots.start(2)
