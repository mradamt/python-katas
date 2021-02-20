'''
Create an app that has a password stored in a variable. When the application runs, ask the user to input the password. If they input it correctly, print a message telling them that they're in. If they input it incorrectly, tell them that they got it wrong.
'''

password = input('Set your password: ')

confirm = input('Confirm your password: ')

while confirm != password:
  if confirm == 'q':
    print('(quit)')
    break
  confirm = input("No match. Confirm your password (or 'q' to quit): ")

if confirm == password:
  print('Both passwords match')

# print('(end of program)')

