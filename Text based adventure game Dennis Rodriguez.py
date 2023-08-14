# Dennis Rodriguez

def endgame():
    print('---------------------------------------------------------------------')
    print("you Won!! and have defeated the mighty horde\n thank you so much for playing the game!!")


def show_instructions():
    # print a main menu and the commands
    print("The Defense of Castle Mercer")
    print("Collect 6 siege defense weapons to win the game, or succumb to the horde.")
    print("Your are Move commands: go South, go North, go East, go West")
    print('You can quit at any time just by saying the command quit')
    print('to check current inventory just type inventory')
    print("-----------------------------------------------------------------------------------")


# data setup
rooms = {'castle courtyard': {'name': 'Castle Courtyard', 'go east': 'blacksmith', 'go south': 'armory',
                              'go north': 'stables', 'go west': 'orchard',
                              'text 1': 'You hear the alarm bells sync with your heartbeat',
                              'text 2': 'You hear the alarm bells sync with your heartbeat',
                              'contents': ['nothing but fields and fountains']},
         'orchard': {'name': 'Lord Mercers apple orchard', 'go south': 'castle fields', 'go east': 'castle courtyard',
                     'contents': ['apples'],
                     'text 1': 'You walk into the orchard and you see 2 hectares of apple trees \n you think it will be just what you need for the horses',
                     'text 2': 'You collected the necessary apples for the horses'
                     },

         'blacksmith': {'name': 'The Blacksmiths forge', 'go north': 'castle walls', 'go west': 'castle courtyard',
                        'contents': ['armor'],
                        'text 1': 'You arrive in the Blacksmith Forge and you see the armor the blacksmith has been crafting for you',
                        'text 2': 'You are well protected'},
         'armory': {'name': 'The Royal Armory', 'go north': 'castle courtyard', 'contents': ['sword'],
                    'text 1': 'You enter the Armory where your Generals Sabre is there waiting for you',
                    'text 2': 'You now have the means to fight'},
         'castle walls': {'name': 'The Castle Walls', 'go north': 'castle gates', 'go south': 'blacksmith',
                          'contents': ['catapult'],
                          'text 1': 'You arrive at the castle gates where you see that you men have set the catapult defenses ready for your word',
                          'text 2': 'Your men have readied the catapults and await your word'},
         'castle fields': {'name': 'The Castle Fields', 'go north': 'orchard', 'contents': ['bow'],
                           'text 1': 'The Kings archers prepare for the attack and offer a bow of your own if you choose to take it',
                           'text 2': 'The Kings archers bid you good fortune and a keen eye'},
         'stables': {'name': 'The Royal Stables', 'go south': 'castle courtyard', 'go east': 'castle gates',
                     'contents': ['horse'],
                     'text 1': 'Your men have readied your horse so you can quickly give commands to the defending troops',
                     'text 2': 'With your horse now returned the calvary make their way to the castle gates'},
         'castle gates': {'name': 'The Castle Gates', 'go south': 'castle walls', 'go west': 'stables',
                          'contents': ['horde'],
                          'text 1': '',
                          'text 2': ''}
         }

directions = ['go north', 'go south', 'go east', 'go west']
current_room = rooms['castle courtyard']
inventory = []

horde = True

show_instructions()
while True:
    # checks for if all items have been found
    if current_room == rooms['castle gates'] and len(inventory) == 6:
        print("You enter look out to the horde finally prepared to take on the hoard\ngood luck general")
        horde = False
        break
    # you can still enter boss room but you will die without all the items
    if current_room == rooms['castle gates'] and len(['inventory']) != 6:
        decision = input('you are unprepared\ndo you want to proceed anyways? ')
        if decision == "yes":
            print('You have succumb to the horde please try again')
            break
        else:
            current_room = rooms['castle courtyard']
    # display current location
    print()
    print('You are in {}.'.format(current_room['name']))
    # Display different dialogues
    if current_room['contents'] != []:
        print(current_room['text 1'])

    if current_room['contents'] == []:
        print(current_room['text 2'])

    elif current_room['contents']:
        print('In the room are: {}'.format(', '.join(current_room['contents'])))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
            continue
    # quit game
    elif command.lower() in ('q', 'quit'):
        break

    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            inventory.append(item)
            print('got', item)
            continue
        else:
            print("I don't see that here.")
            continue

    # check inventory
    if command.lower() == 'inventory':
        print(inventory)
    # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in inventory:
            current_room['contents'].append(item)
            inventory.remove(item)
            print(item, 'dropped')
        else:
            print("You aren't carrying that.")
    # trigger death sequence
    if current_room == rooms['castle gates']:
        continue
    # bad command
    if command not in directions or inventory:
        print("I don't understand that command.")

if horde == False:
    endgame()
