foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

print(len(foosballers))

# median player
median = len(foosballers) // 2
# print(median)

# 5 middle players
five_middle = foosballers[median - 2:median + 3]
# print(five_middle)

# add the average player
foosballers.insert((len(foosballers) + 1) // 2, 'Average player')

# change average player to all caps
foosballers[foosballers.index('Average player')] = 'AVERAGE PLAYER'

# add five more players
players = ['one', 'two', 'three', 'four', 'five']
# for p in players:
#   foosballers.append(p)
foosballers.extend(players)

# move avg player back to new middle
del foosballers[foosballers.index('AVERAGE PLAYER')]
# print(len(foosballers))
# print((len(foosballers) + 1) // 2)
foosballers.insert((len(foosballers) + 1) // 2, 'AVERAGE PLAYER')

# insert into specific position
# lacy one ahead of hubert
foosballers.insert(foosballers.index('Hubert'), 'Lacy')
# omar one behind Rebecca
foosballers.insert(foosballers.index('Rebecca') + 1, 'Omar')
# Otto is 8th best
foosballers.insert(7, 'Otto')
# Guy is 10 spots from bottom
foosballers.insert(-9, 'Guy')


print(foosballers)
