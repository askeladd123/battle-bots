# BattleBots
Dokumentasjon for BattleBots av Ask Sødal

# ------------------------------
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  return "right"

BattleBots.start()
# ------------------------------


# ------------------------------
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  return "right"
  
@BattleBots.register_ai
def super_ai(input):
  return "left"

BattleBots.start()
# ------------------------------


# ------------------------------
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  return

@BattleBots.register_ai
def super_ai(input):
  return "left"

BattleBots.start(1)
# ------------------------------


# ------------------------------
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  return

@BattleBots.register_ai
def super_ai(input):
  print(input.bullet_positions)

BattleBots.start(1)
# ------------------------------


# ------------------------------
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  return

@BattleBots.register_ai
def super_ai(input):
  if 0 < len(input.bullet_positions):
    if input.position[0] < input.bullet_positions[0]:
      return "right"
    else:
      return "left"

BattleBots.start(1)
# ------------------------------

