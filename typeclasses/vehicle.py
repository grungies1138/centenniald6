from typeclasses.objects import Object

class Vehicle(Object):
    def at_object_creation(self):
        self.db.skill = ''
        self.db.scale = ''
        self.db.body = 0
        self.db.maneuverability = 0
        self.db.move = 0
        self.db.crew = 0
        self.db.passengers = 0
        self.db.weapons = []
        self.db.cargo = 0