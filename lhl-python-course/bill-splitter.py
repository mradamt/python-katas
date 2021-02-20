'''
Ask for a total dollar amount
Ask for the percentage tip
Ask for the number of people splitting the bill
Use those numbers to calculate the amount that each person owes, printing it out to the terminal, along with the overall total
'''

bill_total = int(input('Bill total: '))
tip = int(input('Tip percent: '))
ppl = int(input('Number of people: '))

print(f'Each person pays: {(bill_total + bill_total * tip / 100) / ppl}')
