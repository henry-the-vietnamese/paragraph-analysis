#
# File:         main.py
# Author:       Tan Duc Mai
# Email ID:     tan.duc.work@gmail.com
# Date:         22/9/2021
# Description:  Analyse a user input paragraph for sentences and words.
#

# Set the initial values
text = input('Enter some text and I will tell you some details about it: ')
count = ['a', 'e', 'i', 'o', 'u', ' ', '.']
total = []

""" Explain the below for loop.

Convert the str to all in lower case for easier comparison.
Whenever it happens on a vowel, a space, or a full stop in the text,
it is appended to the 'total' list.
"""
for i in text.lower():
    if i in count:          
        total.append(i)     

# The number of words = the number of spaces + 1
print('\nNumber of words =', total.count(' ') + 1) 

# The number of sentences = the number of full stops
print('\nNumber of sentences =', total.count('.')) 

# Count each vowel
print(f'\nCounts of vowels -', end = '')

# Create a list containing the counts of each vowels
vowels = [total.count('a'),
          total.count('e'),
          total.count('i'),
          total.count('o'),
          total.count('u'),
]

for i in range(len(vowels)):
    print()
    print(count[i].upper(), end = '\t')
    for _ in range(vowels[i]):
        print('*', end = '')
