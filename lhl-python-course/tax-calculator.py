'''
Ask the user to input a subtotal.
Calculate the tax owed using some (hard-coded) tax rate. This can be whatever you want, like 0.25.
Print out a message with the amount of tax owed.
Print out another message with the total owed including tax.
'''

pre_tax = input('Enter an amount: ')
tax_rate = input('Enter a tax rate: ')
print(f'Tax rate: {tax_rate}%')
print (f'With tax, amount is: {float(pre_tax) * 1.25}')
