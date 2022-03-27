import random

floor = random.randrange(1, 101)
print(floor)

def worstSolution():
  maxFloor = 10000
  isRunning = True
  localFloor = 0
  while isRunning:
    if (floor > localFloor):
      localFloor += 1
    if (floor == localFloor):
      maxFloor = localFloor
      isRunning = False
  return maxFloor

def mediumSolution():
  maxFloor = 10
  minFloor = 0
  localFloor = 10
  totalEggs = 2
  jumpFloor = 10
  while (totalEggs > 0):
    if (floor == localFloor):
      return int(localFloor)
    elif (floor > localFloor):
      localFloor += jumpFloor
      minFloor = localFloor
    elif (floor < localFloor):
      if minFloor > 0:
        minFloor -= jumpFloor
      maxFloor = localFloor
      localFloor -= jumpFloor
      totalEggs -= 1
      jumpFloor = jumpFloor / 2
      localFloor += jumpFloor
  return [int(minFloor), int(maxFloor)]

def bestSolution():
  maxFloor = 50
  minFloor = 0
  localFloor = 50
  totalEggs = 2
  jumpFloor = 50 / 2
  while (totalEggs > 0):
    if (floor == localFloor):
      return int(localFloor)
    elif (floor > localFloor):
      if (localFloor > minFloor):
        minFloor = localFloor
      localFloor += jumpFloor
      maxFloor += jumpFloor
    elif (floor < localFloor):
      maxFloor = localFloor
      localFloor -= jumpFloor
      totalEggs -= 1
      jumpFloor = round(jumpFloor / 2)
  return [int(minFloor), int(maxFloor)]

print('Brute force solution: ',str(worstSolution()))

secondSolution = mediumSolution()
if type(secondSolution) == list:
  print('Jumping 10 floors solution: between ',str(secondSolution[0]),' and ',str(secondSolution[1]))
else:
  print('Jumping 10 floors solution: ',str(secondSolution))

thirdSolution = bestSolution()
if type(thirdSolution) == list:
  print('Cutting in half solution: between ',str(thirdSolution[0]),' and ',str(thirdSolution[1]))
else:
  print('Cutting in half solution: ',str(thirdSolution))

