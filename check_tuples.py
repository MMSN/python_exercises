possibleTuples = [['{','}'],['[',']'],['(',')']]


def generateAuxList(list):
  return [None]*len(list)

def shouldContinue(auxList):
  for i in range(len(auxList)):
      if auxList[i] == None:
        return True
  return False

def characterToSeek(letter):
  for i in range(len(possibleTuples)):
    if possibleTuples[i][0] == letter:
      return possibleTuples[i][1]
  return False

def solution(list):
  auxList = generateAuxList(list)
  isWorking = True
  fromBeginning = 0
  fromEnd = len(list) - 1
  lastFound = None
  while isWorking:
    if (fromBeginning >= len(list)):
      return False
    if (auxList[fromBeginning]) == 'X':
      fromBeginning += 1
      continue
    characterBeginning = list[fromBeginning]
    characterToLookFor = characterToSeek(characterBeginning)
    if (characterToLookFor == False):
      auxList[fromBeginning] = 'X'
      fromBeginning += 1
      continue
    found = False
    for i in range(fromEnd, fromBeginning, -1):
      if list[i] == characterToLookFor and auxList[i] == None:
        if lastFound != None:
          if lastFound[0] > fromBeginning or lastFound[1] < i:
            return False
        found = True
        auxList[fromBeginning] = 'X'
        auxList[i] = 'X'
        fromBeginning += 1
        lastFound = [fromBeginning, i]
    if found == False:
      return False
    
    isWorking = shouldContinue(auxList)
  return True
      

def menu():
  print('Press 1 to input a string.')
  print('Press 2 to run with default string ({(])}).')
  print('Press 0 to stop.')
  userInput = int(input())
  return userInput


loop = True

while loop:
  decision = menu()

  if decision == 1:
    userInput = str(input())
    listInputFormat = list(userInput)
    print(solution(listInputFormat))
    print('\n')
  elif decision == 2:
    userInput = '{(])}'
    listInputFormat = list(userInput)
    print(solution(listInputFormat))
    print('\n')
  elif decision == 0:
    loop = False
