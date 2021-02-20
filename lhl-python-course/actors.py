
actors = [
  'guy',
  'other guy',
  'third guy',
  'girl',
  'another girl'
]

roles = [
  'guy ROLE',
  'other guy ROLE',
  'third guy ROLE',
  'girl ROLE',
  'another girl ROLE'
]

# match list of actors with their role

for i in range(len(actors)):
  print(f'{actors[i]} : {roles[i]}')

enumerableActors = enumerate(actors)
listy = list(enumerableActors)
print(listy)