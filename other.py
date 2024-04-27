class ExitNotFoundError(Exception):
    def __init__(self, name, message="Room not found"):
        self.name = name
        self.message = message

    def __str__(self):
        return f"{self.name} -> {self.message}"

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room: 
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = []
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_exits(self):
        return self.exits
    
    def list_exits(self):
        return '\n'.join(self.exits) # makes the list a str that is spread out over new lines

    def list_items(self):
        if self.items:
            return "Items in the room:\n" + "\n".join([item.name for item in self.items])
        else:
            return "No items in the room."
    
    def __str__(self):
        return f"{self.name}: {self.description}\n\nExits:\n{self.list_exits()}\n\n{self.list_items()}"

class AdventureMap:
    def __init__(self):
        self.map = {} # initializes dict
    
    # method that adds a room to the map 
    def add_room(self, room):

        self.map[room.get_name()] = room # room key is set

    def get_room(self, room_name):
        room = self.map.get(room_name.title()) # gets the room and checks if it is in the dict
        if room:
            return room#, room_items
        else:
            raise ExitNotFoundError(room_name)
