# Rock, Paper, Scissor.
import random
name = ((input('Enter your name: ')).lower()).capitalize()
print('Rock, Paper, Scissor game')
print('\"r\" for Rock.')
print('\"p\" for Paper.')
print('\"s\" for Scissor.')
cs = ['r', 'p', 's']
ply1 = 0
cs1 = 0
i = 0
while i < 9:
    if i > 5:
        print(f'Final {9 - i} chance(s) left.')
    ply2 = (str(input('Enter any key word: '))).lower()
    cs2 = random.choice(cs)
    if ply2 in cs:
        if ply2 == 'r' and cs2 == 's':
            print(f'{name} won!\n')
            ply1 = ply1 + 1
            i = i + 1
        elif ply2 == 'p' and cs2 == 'r':
            print(f'{name} won!\n')
            ply1 = ply1 + 1
            i = i + 1
        elif ply2 == 's' and cs2 == 'p':
            print(f'{name} won!\n')
            ply1 = ply1 + 1
            i = i + 1
        elif ply2 == 's' and cs2 == 'r':
            print('The Computer won.\n')
            cs1 = cs1 + 1
            i = i + 1
        elif ply2 == 'p' and cs2 == 's':
            print('The Computer won.\n')
            cs1 = cs1 + 1
            i = i + 1
        elif ply2 == 'r' and cs2 == 'p':
            print('The Computer won.\n')
            cs1 = cs1 + 1
            i = i + 1
        else:
            print('Draw.\n')
            i = i + 1
    else:
        print('Please enter a valid input.\n')
        cs1 = cs1 + 1
        i = i + 1
if ply1 > cs1:
    print('Congratulations! you won.')
    print(f'You won by {ply1 - cs1} points.')
elif cs1 > ply1:
    print('Better luck next time.')
    print(f'You lost by {cs1 - ply1} points.')
else:
    print('It\'s a Draw.')
