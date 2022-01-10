import BattleBots


@BattleBots.register_ai
def super_ai(input, output):
    0

@BattleBots.register_ai
def super_ai(input, output):
    if input.is_legal("down"):
        output.move("down")
    else:
        output.shoot("right")

@BattleBots.register_ai
def super_ai(input, output):
    if input.is_legal("right"):
        output.move("right")
    else:
        output.move("down")


BattleBots.start(2)