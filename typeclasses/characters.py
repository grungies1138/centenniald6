"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        self.db.stats = {'might': {'value': 6, 'brawling': 0, 'athletics': 0, 'melee': 0, 'throwing': 0, 'swimming': 0, 'lift': 0, 'climb': 0},
                         'agility': {'value': 6, 'dodge': 0, 'stealth': 0, 'firearms': 0, 'pilot': 0, 'quickdraw': 0, 'pickpocket': 0, 'acrobatics': 0},
                         'wit': {'value': 6, 'medicine': 0, 'navigation': 0, 'mechanics': 0, 'languages': 0, 'science': 0, 'security': 0, 'survival': 0, 'perception': 0, 'law': 0},
                         'charm': {'value': 6, 'command': 0, 'persuasion': 0, 'streetwise': 0, 'business': 0, 'politics': 0, 'intimidate': 0, 'gambling': 0, 'deception': 0, 'force': 0}}

        self.db.armor = 0
        self.db.body_points = 0
        self.db.dodge = 0
        self.db.soak = 0
        self.db.parry = 0
        self.db.block = 0
        self.db.max_might = 4
        self.db.max_agility = 4
        self.db.max_wit = 4
        self.db.max_charm = 4
        self.db.force_sensitive = False
