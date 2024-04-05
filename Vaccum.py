class Room:
    def __init__(self, _vaccum, _garbageLoc):
        self.vaccum = _vaccum
        self.garbageLoc = _garbageLoc
        print("_Room State_")
        for key in self.garbageLoc:
            print(key + " : " + self.garbageLoc[key])

    def setRoomState(self, _key, _value):
        self.garbageLoc.update({_key: _value})

    def startCleaning(self):
        for key in self.garbageLoc:
            self.vaccum.setMove(key)
            tag = self.vaccum.setState("suck", key, self.garbageLoc[key])
            if tag:
                self.setRoomState(key, "clean")
            self.vaccum.setState("off", key, self.garbageLoc[key])
        print("_Room State_")
        for key in self.garbageLoc:
            print(key + " : " + self.garbageLoc[key])


class Vaccum:
    def __init__(self, _location, _state):
        self.location = _location
        self.state = _state
        print("Vaccum at " + self.location + " and is in " + self.state + " state")

    def setMove(self, _direction):
        if self.location == _direction:
            print("Vaccum is already on " + self.location)
        else:
            self.location = _direction
            print("Vaccum moved to " + _direction)

    def setState(self, _action, _roomLoc, _roomState):
        if self.state == _action:
            print("Vaccum is already in " + self.state + " state")
        elif _action == "suck" and _roomState == "clean":
            self.state = "off"
            print("Cannot clean an already clean place . Vaccum switched to " + self.state + " state")
        elif _action == "suck":
            self.state = _action
            print("Vaccum switched to " + self.state + " state")
            _roomState = "clean"
            print("Cleaned " + _roomLoc + " Successfully")
            return True
        else:
            self.state = _action


myVaccum = Vaccum("left", "off")
roomState = {
    "left": "dirty",
    "right": "dirty",
    "up": "clean"
}
myRoom = Room(myVaccum, roomState)
myRoom.startCleaning()
