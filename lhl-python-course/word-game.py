'''
Create a python version of madlibs
Use the phrase: 'Just as I arrived at [place], I realized I had forgotten my [object]'
'''

base_phrase = '''
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
'''

words = ['OCCUPATION', 'COUNTRY', 'PLURAL_NOUN', 'VERB', 'ADJECTIVE', 'PERSONAL_ITEM', 'HOLIDAY', 'NAME']
# words = ['OCCUPATION', 'COUNTRY']

for word in words:
  base_phrase = base_phrase.replace(word, input(f'{word.title()}: '))

print(base_phrase)



# place = input('Tell me a place: ')
# obj = input('Tell me an object: ')

# print(f'Just as I arrived at {place}, I realized I had forgotten my {obj}')
