# Aidan Drzewicki
# 3.7.19
# Final Project

# Mad libs generator
# There will be multiple sentences with different areas the user can input
# a word of their choice to make their own mini story.


def madlib1(str: object) -> object:
    print('Roses are ' + adj1 + '.')
    print(n1 + 'are blue.')
    print(n2 + ' are ' + adj2)
    print('And so are you!')
    return madlib1()

def madlib2(str):
    print('The ' + adj1 + n1 + 'fox jumped over a fence.')
    print('Then he saw a ' + adj2 + n2 + ' coming towards him.')
    print('He then decided to ' + adj3)


question = int(input('Hello, would you like to do madlib 1 or 2? '))
try:
    if question == (1):
        madlib1(str)

    if question == (2):
        madlib2(str)


except ValueError:
    print('Please enter 1 or 2')


adj1 = input('Tell me an adjective and press enter: ')
n1 = input('Tell me a noun and press enter: ')
n2 = input('Tell me another noun and press enter: ')
adj2 = input('Tell me another adjective and press enter: ')
adj3 = input('Tell me another adjective and press enter: ')