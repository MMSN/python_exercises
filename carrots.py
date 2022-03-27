carrots = [[5, 100], [7, 150], [3, 70]]

loop = True

def menu():
  print('Press 1 to add a new carrot type.')
  print('Press 2 to run getMaxValues.')
  print('Press 0 to stop.')
  userInput = int(input())
  return userInput

def addNewCarrot():
  print('Kg?')
  userInputKg = int(input())
  print('Price?')
  userKgInputPrice = int(input())
  carrots.append([userInputKg, userKgInputPrice])

def getMaxValues():
  print('Max Capacity?')
  userInpuMaxCapacity = int(input())
  solution = []  
  for i in range(len(carrots)):
    capacity = 0
    value = 0
    while capacity <= userInpuMaxCapacity:
      if capacity + carrots[i][0] > userInpuMaxCapacity:
        solution.append([capacity, value])
      capacity += carrots[i][0]
      value += carrots[i][1]
  return solution

def solutionToString(list):
  for i in range(len(list)):
    print('Type ',str(i+1),'of carrot, max capacity is ',str(list[i][0]),' and price is ',str(list[i][1]))
  return

while loop:
  decision = menu()

  if decision == 1:
    addNewCarrot()
  elif decision == 2:
    solution = getMaxValues()
    solutionToString(solution)
    print('\n')
  elif decision == 0:
    loop = False