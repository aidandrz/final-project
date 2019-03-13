# Aidan Drzewicki
# 3.7.19
# Final Project

# Mad libs generator
# There will be multiple sentences with different areas the user can input
# a word of their choice to make their own mini story.

# the initial statement printed for the user
question = int(input('Hello, would you like to do madlib 1 or 2? '))

# The if statements for if the user doesn't enter 1 or 2
if question > 2:
    print("Enter 1 or 2")

if question < 0:
    print('Enter 1 or 2')

def madlib1(str: object) -> object:
    print('Roses are ' + adj1 + '.')
    print(n1 + 'are blue.')
    print(n2 + ' are ' + adj2)
    print('And so are you!')
    return madlib1()

# the inputs from the user that they will put the different nouns or adjectives
adj1 = input(str('Tell me an adjective and press enter: '))
n1 = input(str('Tell me a noun and press enter: '))
n2 = input(str('Tell me another noun and press enter: '))
adj2 = input(str('Tell me another adjective and press enter: '))
adj3 = input(str('Tell me another adjective and press enter: '))


# the program that will run and print the madlib
try:
    def madlib1(str):
        print('Roses are ' + adj1 + '.')
        print(n1 + 'are blue.')
        print(n2 + ' are ' + adj2)
        print('And so are you!')
        return object


    def madlib2(str: object) -> object:
        print('The ' + adj1 + ' ' + n1 + ' fox jumped over a fence.')
        print('Then he saw a ' + adj2 + ' ' + n2 + ' coming towards him.')
        print('He then decided to ' + adj3)
        return object

    if question == (1):
        madlib1(str)

    if question == (2):
        madlib2(str)

    else:
        print('Enter 1 or 2')


# what happens if you don't put 1 or 2
except ValueError:
    print('Please enter 1 or 2')


