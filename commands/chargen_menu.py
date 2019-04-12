from evennia import default_cmds
from evennia.utils.evmenu import EvMenu
from commands.library import node_formatter, options_formatter, titlecase
from world.perks import SPECIES, RACIAL_PERKS

class ChargenMenuCommand(default_cmds.MuxCommand):
    """
    Start the Character Generation Process

    Usage:
        +chargen
    """

    key = "+chargen"
    locks = "cmd:perm(Player)"
    help_category = "Chargen"

    def func(self):
        EvMenu(self.caller,
               "commands.chargen_menu",
               startnode="menu_start_node",
               cmdset_mergetype="Replace",
               node_formatter=node_formatter,
               auto_help=False,
               options_formatter=options_formatter,
               cmd_on_exit=exit_message)


def menu_start_node(caller):
    reset_chargen(caller)
    if caller.db.chargencomplete == 1:
        text = "Initial Character Generation has been completed.  There is no further action to take with this " \
               "command.  You may exit."
        options = ()

        return text, options

    text = """
        Welcome to Character Generation!
        Please select an item to modify.  When an item has been set, it will be darkened.  You can still change it 
        (with some exceptions), but it will help you track where you have already been.
    """

    options = ({"desc": "Personals",
                "goto": "ask_personal"},
               {"desc": "Stats",
                "goto": "ask_stats"},
               {"desc": "Perks",
                "goto": "ask_perks"},
               {"desc": "Finalize",
                "goto": "ask_finalize"})

    return text, options


def ask_personal(caller):
    text = "Please select the item you wish to set.  Darkened items have already been completed.  However, you can " \
           "change them afterwards, unless otherwise specified."

    options = ()

    if caller.db.fullname:
        options += ({"desc": "|xFull Name|n",
                     "goto": "ask_fullname"},)
    else:
        options += ({"desc": "Full Name",
                     "goto": "ask_fullname"},)

    if caller.db.age:
        options += ({"desc": "|xAge|n",
                     "goto": "ask_age"},)
    else:
        options += ({"desc": "Age",
                     "goto": "ask_age"},)

    if caller.db.height:
        options += ({"desc": "|xHeight|n",
                     "goto": "ask_height"},)
    else:
        options += ({"desc": "Height",
                     "goto": "ask_height"},)

    if caller.db.weight:
        options += ({"desc": "|xWeight|n",
                     "goto": "ask_weight"},)
    else:
        options += ({"desc": "Weight",
                     "goto": "ask_weight"},)

    if caller.db.species:
        options += ({"desc": "|nSpecies|n",
                     "goto": "ask_species"},)
    else:
        options += ({"desc": "Species",
                     "goto": "ask_species"},)

    if caller.db.description:
        options += ({"desc": "|xDescription|n",
                     "goto": "ask_description"},)
    else:
        options += ({"desc": "Description",
                     "goto": "ask_description"},)

    if caller.db.background:
        options += ({"desc": "|xBackground|n",
                     "goto": "ask_background"},)
    else:
        options += ({"desc": "Background",
                     "goto": "ask_background"},)

    options += ({"desc": "Go Back",
                 "goto": "menu_start_node"},)

    return text, options


def ask_fullname(caller):
    text = ""

    fullname = caller.db.fullname

    if fullname:
        text += "Current Full Name: {}\n\n".format(titlecase(fullname))

    text += "Please enter your character's full name as you wish it to appear on your Character Sheet."

    options = ({"key": "_default",
                "goto": set_fullname},
               {"desc": "Go Back",
                "goto": "ask_personal"})

    return text, options


def set_fullname(caller, caller_input, **kwargs):
    caller.msg("Set Fullname")
    inp = caller_input.strip().lower()
    caller.ndb._menutree.fullname = inp

    return None


def ask_age(caller):
    text = ""
    age = caller.db.age
    if age:
        text += "Current Age: {}\n\n".format(age)

    text += "Please enter the age you wish to be."

    options = ({"key": "_default",
                "goto": set_age},
               {"desc": "Go Back",
                "goto": "ask_personal"})

    return text, options


def set_age(caller, caller_input, **kwargs):
    inp = caller_input.strip()
    age = 0
    try:
        age = int(inp)
        caller.ndb._menutree.age = age
        return None
    except ValueError as e:
        caller.msg("Error: That is not a number.")
        return None


def ask_height(caller):
    text = ""

    height = caller.db.height

    if height:
        text += "Current Height: {}\n\n".format(height)

    text += "Please enter the height you wish to have in meters.  (Ex: 1.8 or 1.2)\n\nDon't know how to convert?  Google it!"

    options = ({"key": "_default",
                "goto": set_height},
               {"desc": "Go Back",
                "goto": "ask_personal"})

    return text, options


def set_height(caller, caller_input, **kwargs):
    inp = caller_input.strip()
    try:
        height = int(inp)
        caller.ndb._menutree.height = height
        return None
    except ValueError as e:
        caller.msg("Error: That is not a number")
        return None


def ask_weight(caller):
    text = ""

    weight = caller.db.weight

    if weight:
        text += "Current Height: {}\n\n".format(weight)

    text += "Please enter the weight you wish to have in kilograms.  (Ex: 110 or 83)\n\nDon't know how to convert?  Google it!"

    options = ({"key": "_default",
                "goto": set_weight},
               {"desc": "Go Back",
                "goto": "ask_personal"})

    return text, options


def set_weight(caller, caller_input, **kwargs):
    inp = caller_input.strip()
    try:
        weight = int(inp)
        caller.ndb._menutree.weight = weight
        return None
    except ValueError as e:
        caller.msg("Error: That is not a number")
        return None


def ask_species(caller, caller_input, **kwargs):
    selected_species = kwargs.get("selected_species")

    if selected_species:
        caller.db.species = selected_species
    text = ""

    if selected_species:
        text += "Currect Species: {}\n\n".format(selected_species)

    text += "Please select the species you would like to review for possible selection."

    options = ()

    for item in SPECIES.keys():
        node_dict = {"desc": item, "goto": ("confirm_species", {"selected_species": item})}
        options += (node_dict,)


    options += ({"desc": "Custom",
                 "goto": ("confirm_species", {"selected_species": "custom"})},
                {"desc": "Go Back",
                 "goto": "ask_personal"},)

    return text, options


def confirm_species(caller, caller_input, **kwargs):
    text = ""
    options = ()

    if "selected_perk" in kwargs.keys():

        if hasattr(caller.ndb._menutree, 'perks'):
            if kwargs.get("selected_perk") in caller.ndb._menutree.perks:
                caller.msg("You cannot select the same perk twice.  Please try again.")
            else:
                caller.ndb._menutree.perks.append(kwargs.get("selected_perk"))
            text += "Currently selected perks: {}\n\n".format(", ".join(caller.ndb._menutree.perks))
        else:
            caller.ndb._menutree.perks = [kwargs.get("selected_perk")]
            text += "Currently selected perks: {}\n\n".format(", ".join(caller.ndb._menutree.perks))
    if kwargs.get("selected_species") == "custom":
        text += "Creating a custom species can be fun and rewarding for players.  Often, the built-in species do not " \
                "quite satisfy the creative desires of the character customization process.  To create a custom " \
                "species, you simply need to pick one or more (or zero) racial perks.  Each perk has an associated " \
                "cost as well as description.  To view these details, select one of the options below."

        for item in RACIAL_PERKS.keys():
            node_dict = {"desc": item, "goto": ("ask_racial_perks", {"perk": item, "selected_species": "custom"})}
            options += (node_dict,)

        options += ({"desc": "Go Back",
                     "goto": "ask_species"},)
    else:
        species = SPECIES.get(kwargs.get("selected_species"))
        text += "Species: {}\n".format(titlecase(kwargs.get("selected_species")))
        text += "Description: {}\n".format(species.get("description"))
        text += "Perks: {}".format(", ".join(species.get("perks")))
        text += "Cost: {}".format(species.get("cost"))

        options += ({"desc": "Confirm",
                    "goto": (ask_species, {"selected_species": kwargs.get("selected_species")})},
                    {"desc": "Go Back",
                    "goto": "ask_species"},)

    return text, options


def ask_racial_perks(caller, caller_input, **kwargs):
    perk = RACIAL_PERKS.get(kwargs.get("perk"))
    text = ""

    text += "Perk: {}\n".format(kwargs.get("perk"))
    text += "Description: {}\n".format(perk.get("description"))
    text += "Bonus: {}\n".format(perk.get("bonus"))
    text += "Cost: {}\n\n".format(perk.get("cost"))

    options = ({"desc": "Select",
                "goto": ("confirm_species", {"selected_perk": kwargs.get("perk"), "selected_species": "custom"})},
               {"desc": "Go Back",
                "goto": "confirm_species"})

    return text, options



def reset_chargen(caller):
    del caller.db.fullname
    del caller.db.age


def exit_message(caller, menu):
    if caller.db.chargencomplete != 1:
        reset_chargen(caller)
        caller.msg("Exiting chargen before completion.  Clearing Chargen settings.")

    caller.msg("Exiting Chargen.  Goodbye.")

