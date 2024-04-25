"""
Author:  Federico Sainz
Date: 4/23/2024
Assignment:  Project 2
Course: CPSC1050
Lab Section:  002

CODE DESCRIPTION: RPG game
"""

import other
from other import Room
from other import ExitNotFoundError
from other import Item
import random

def main():
    game_map = other.AdventureMap()
    print("\nWelcome to the Adkins house! Entering the study room. To leave the house, please type exit to jump out of the nearest window.\n")

    items = [
        Item("Key", "A Key"),
        Item("Red Key", "A red key")
    ]

    rooms = [
        Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen']),
        Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"]),
        Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"]),
        Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]),
        Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"]),
        Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"]),
        Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom.", ["Study", "Trophy Room"]),
        Room("Game Room", "A crazy state of the art game room with LED lighting.", ['Kitchen', "Bedroom"]),
        Room("Living Room", "A giant living room with couches everywhere that you can rest on.", ["Library","Holodeck"])
    ]
    
    for item in items:
        room = random.choice(rooms)
        room.items.append(item)
    
    for room in rooms:
        game_map.add_room(room)

    current_room = 'Study'
    
    room = game_map.get_room(current_room) # gets study as the first room and outputs it for the user
    
    print(room)

    while True:
        
        exit_dec = input('Please choose an exit:\n').lower().strip() # gets the input
        
        try:     
            if exit_dec.title() in room.exits: # if the input is in the exits of that room then room is set and printed out
                
                room = game_map.get_room(exit_dec)

                print(room)
            
            elif exit_dec == 'exit': # if exit is inputted then exits
            
                print("Exiting the house out of the nearest window... thanks for the tour!")
            
                exit()
            
            else:
            
                raise ExitNotFoundError(exit_dec) # if the input is not in the room exits then it raises an error
        
        except ExitNotFoundError as e:
        
            print(e) # prints out the raised error

if __name__ == "__main__":
    main()

# import logging

# logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger('my_logger')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logging.shutdown()