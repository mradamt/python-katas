from random import *

player_score = 0
num_questions = randint(4, 8)

print(f'Mental math. Game on. You have {num_questions} questions:')

for i in range(num_questions):
  r1 = randint(1, 100)
  r2 = randint(1, 100)
  sum = r1 + r2
  ans = int(input(f'Whats is {r1} + {r2}? '))
  if ans == sum:
    player_score += 1
    print('Correcto')
  else:
    print('Noooope')

print(f'Test completo. You answered {player_score}/{num_questions} correctly => {player_score//num_questions*100}%.')
