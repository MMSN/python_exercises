import time

def solution(list):
  for i in range(len(list)):
    print(list[i])
    time.sleep(2**(i))

print('Using string: abcdefgh')
userInput = 'abcdefgh'
listInputFormat = list(userInput)
solution(listInputFormat)
