from random import *
players = []
questions = ['what is the capital of Osun state? ',
             'what is the capital of abuja? ',
             'what is the capital of sokoto state? ',
             'what is the capital of Ebonyi state?  ',
             'What is the capital of Edo state? ',
             'What is the capital of Lagos state? '
             ]

answers = ['osogbo',
             'abuja',
             'sokoto',
             'abakaliki',
             'benin',
           'ikeja'
             ]

print('Welcome to Sunmade\'s Quiz!')

no_of_players = 2

for i in range(no_of_players):
    player = input(f'Name of contestant {i+1}: ')
    players.append(player)

print('These are the contestants for this quiz')
print('-'*20)

for player in players:
    if players.index(player) == len(players) - 1:
        print(player, end='.')
    else:
        print(player, end=', ')
print()
print('-'*20)
shuffle(players)



for question in range(len(questions)):
    print(choice(players), 'It is your turn')
    answer = input(questions[question])
    if answer.lower() == answers[question]:
        print('correct!')
    else:
        print('wrong')

print('The quiz has ended')


