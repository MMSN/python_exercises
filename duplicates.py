
letters = []
lettersQuantity = []
lettersPositions = []

def catalogLetter(letter, position):
  for i in range(len(letters)):
    if letters[i] == letter:
      lettersQuantity[i] += 1
      lettersPositions[i].append(position)
      return

  letters.append(letter)
  lettersQuantity.append(1)
  lettersPositions.append([position])

def solution(list):
  for i in range(len(list)):
    catalogLetter(list[i], i)

  for i in range(len(lettersQuantity)):
    if lettersQuantity[i] > 1:
      print('Letter ',str(letters[i]),' appears ',str(lettersQuantity[i]),' times. Positions ',str(lettersPositions[i]))

def menu():
  print('Press 1 to input a string.')
  print('Press 2 to run with default string (abcdegakfolcmao).')
  print('Press 0 to stop.')
  userInput = int(input())
  return userInput


loop = True

while loop:
  decision = menu()

  if decision == 1:
    userInput = str(input())
    listInputFormat = list(userInput)
    solution(listInputFormat)
    print('\n')
  elif decision == 2:
    userInput = 'abcdegakfolcmao'
    listInputFormat = list(userInput)
    solution(listInputFormat)
    print('\n')
  elif decision == 0:
    loop = False
  letters = []
  lettersQuantity = []
  lettersPositions = []
