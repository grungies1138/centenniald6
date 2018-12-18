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
    pass

# Attributes and Skills #######
# Attributes: Might, Agility, Wit, Charm

# Might Skills: Brawling, Athletics, Melee, Throwing, Swimming, Lift, Climb
# Agility Skills: Dodge, Stealth, Firearms, Pilot, Quickdraw, Pickpocket, Acrobatics
# Wit Skills: Medicine, Navigation, Mechanics, Languages, Science, Security, Survival, Perception, Law
# Charm Skills: Command, Persuasion, Streetwise, Business, Politics, Intimidate, Gambling, Deception, Force

# Perks ########################
# Racial Perks

# Custom(0)
# Human(0)
# Twi'lek(0)
# Devaronian(0)
# Arcona(0)
# Wookie(2) - Claws, +1 to Might skills
#


# Racial Perks
# Darkvision(1) - Can see in low light situations.  No penalties to Perception checks.
# Natural Armor(1) - +2 Armor value from Scales, cybernetic enhancements or other means integrated into the physical form.
# Claws(1) - Unarmed attacks gain +2 to damage. +2 to Climb checks
# Flight(3) - Character can fly.  Movement is the same as standard (see help Movement).  Ignore rough terrain penalties.  Can fly up to ten feet off the ground.
# Breath Underwater(2) - Character can breath underwater.  No penalties or Athletics checks to hold breath.
# Big(1) - Max Might set to 5D, Max Agility set to 3D
# Small(1) - Max Agility set to 5D, Max Might set to 3D

# General Perks
# Force Sensitivity(5) - A connection with the Force is possible.  This unlocks the Force Skill.
