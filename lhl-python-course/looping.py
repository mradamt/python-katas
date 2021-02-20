import time

exp_feelings = "💋"
generations = 10

for gen in range(0, generations):
  exp_feelings = exp_feelings * 2
  print(exp_feelings)
  time.sleep(0.5)


