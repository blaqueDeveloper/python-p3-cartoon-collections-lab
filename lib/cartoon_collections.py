def roll_call_dwarves(names):
  index = 1
  for name in names:
    print(f'{index}. {name}')
    index += 1

def summon_captain_planet(planeteer_calls):
  newCall = [call.title() + "!" for call in planeteer_calls]
  return newCall

def long_planeteer_calls(call):
  for name in call:
    if len(name) > 4:
      return True
  return False  



def find_the_cheese(meals):
  cheese = ['cheddar', 'gouda', 'camembert']
  for name in cheese:
    if name in meals:
      return name
    else:
      return None

