no_of_doors = 3
door_1 = 'goat'
door_2 = 'prize'
door_3 = 'goat'
no_of_switch = 0
no_of_not_switch = 0
for i in range(2):
    choice = input('''pick a door: (door 1, door 2, door 3): 
    ''')
    choice = choice.lower()
    if choice == 'door 1' or choice == 'door 3':
        print('You picked a goat door')
        print('You have 1 more attempt')
        print('change your choice')
    else:
        print('You got the prize')


