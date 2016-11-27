def Char_hit():
  '''This is to check if YOU hit the HOSTILE'''
  from HstlSetup import Hstl_agl
  from Damage import Hit_chance
  import random
  random_hit = random.randint(35,65)
  Hit_Check = random_hit * (Hit_chance / Hstl_agl)
  random = random.randint(1,100)
  if Hit_Check > random:
    print("Your Attack appears to have hit!")
  if Hit_Check < random:
    print("Your Attack appears to have missed!")
