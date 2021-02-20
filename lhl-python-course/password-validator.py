'''
User sets their own password, and we want to make sure that a password is secure enough. Ask the user to input a password, and then input it again to confirm it. The application should verify that:
a) Both passwords match
b) The password is at least 8 characters long
If both checks pass, tell the user that they've successfully set the password. If they don't, tell the user what the problem was: Whether the passwords didn't match, or whether it was too short.
'''

password = input('Set a password: ')
confirm = input('Confirm your password: ')
message = ''

if confirm != password:
  message = 'Passwords do not match'

if len(password) < 8:
  if message:
    message += ' & '
  message += 'Password must be 8 characters or longer'
else:
  message = 'Success'

print(message)
