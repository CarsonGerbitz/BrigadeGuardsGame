def Evade():
  from CharSetup import Char_agl
  import random
  Evd_chance = 50 + Char_agl
  Evd_target = random.randint(1,100)
  if Evd_chance < Evd_target:
    print("You have successfully evaded the enemy attack!")
  elif Evd_chance > Evd_target:
    print("Your dodge failed and the enemy attack has hit you!")
  else:
    print("You manage to catch their attack and counter it!")
