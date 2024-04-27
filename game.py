"""
Author:  Federico Sainz
Date: 4/23/2024
Assignment:  Project 2
Course: CPSC1050
Lab Section:  002

CODE DESCRIPTION: RPG game
"""

import other
from other import Room, ExitNotFoundError, Item, CollectedItems
import random
import logging

logging.basicConfig(filename='game.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Game Started")
    game_map = other.AdventureMap()

    print("\nWelcome to the Adkins house! Entering the study room. To leave the house, please type exit to jump out of the nearest window.\n")

    collected_items = other.CollectedItems()

    items = [
        Item("Key", "A Key"),
        Item("Red Key", "A red key")
    ]

    rooms = [
        Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen']),
        Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study", "Living Room"]),
        Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room", "Game Room"]),
        Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]),
        Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library", "Game Room"]),
        Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library", "Living Room"]),
        Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom.", ["Study", "Trophy Room"]),
        Room("Game Room", "A crazy state of the art game room with LED lighting.", ['Kitchen', "Bedroom"]),
        Room("Living Room", "A giant living room with couches everywhere that you can rest on.", ["Library","Holodeck"])
    ]
    
    for item in items:
        
        room = random.choice(rooms)
        
        if room.name != "Holodeck" or item.name != "Red Key":
        
            room.items.append(item)
    
    for room in rooms:
        
        game_map.add_room(room)

    dec = ''

    current_room = 'Study'
    
    room = game_map.get_room(current_room) # gets study as the first room and outputs it for the user

    print(room)


    while True:

        if room.items:
            
            for item in room.items:
            
                dec = input(f"Do you want to pick up the {item.name}? (yes/no): ").lower().strip()
            
                if dec == 'yes':
                    
                    logging.info(f'{item.name} picked up')
                    collected_items.append(item)
            
                    print(f"You have picked up the {item.name}.")

                    if item.name == "Key":
                        
                        print("You can now escape just type 'exit'.")
            
                    room.items.remove(item)

        exit_dec = input('Please choose an exit:\n').lower().strip() # gets the input
        
        logging.info(f'{exit_dec} is the user decision')

        try:    

            if exit_dec.title() in room.exits: # if the input is in the exits of that room then room is set and printed out

                if exit_dec.title() == "Holodeck":
            
                    red_key = False

                    for item in collected_items:
            
                        if item.name == "Red Key":
            
                            red_key = True
                    
                            break

                    if red_key:
                
                        print("Entering Holodeck using the Red Key...\n")

                        room = game_map.get_room(exit_dec)

                        print(room)

                    else:

                        print("You need the red key to enter the Holodeck!\n")

                        print(room)
                        
                else:
                    
                    room = game_map.get_room(exit_dec)
                    
                    print(room)
            
            elif exit_dec == 'exit': # if exit is inputted then exits

                found_key = False
            
                for item in collected_items:
            
                    if item.name == 'Key':
            
                        found_key = True
            
                        break
            
                if found_key:
            
                    print("Exiting the house with the Key... Congratulations on escaping!")
                    logging.info("Game ended")
                    exit()
            
                else:
            
                    print("You need to find the Key before you can exit!")         
            
            else:
            
                raise ExitNotFoundError(exit_dec) # if the input is not in the room exits then it raises an error
        
        except ExitNotFoundError as e:
            
            logging.exception('An exception occurred: %s', e)
            print(e) # prints out the raised error


        


if __name__ == "__main__":
    main()

