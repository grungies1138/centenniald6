from evennia import default_cmds
from evennia.utils.evmenu import EvMenu
from commands.library import node_formatter, options_formatter, titlecase

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

    return text, options


def ask_fullname(caller):
    text = ""

    if caller.db.fullname:
        text += "Current Full Name: {}".format(titlecase(caller.db.fullname))

    text += "Please enter your character's full name as you wish it to appear on your Character Sheet."

    options = ({"key": "_default",
                "goto": "set_fullname"},
               {"desc": "Go Back",
                "goto": "ask_personal"})

    return text, options


def set_fullname(caller, caller_input, **kwargs):
    inp = caller_input.strip().lower()
    caller.db.fullname = inp

    return "ask_fullname"


def reset_chargen(caller):
    del caller.db.fullname


def exit_message(caller, menu):
    if caller.db.chargencomplete != 1:
        reset_chargen(caller)
        caller.msg("Exiting chargen before completion.  Clearing Chargen settings.")

    caller.msg("Exiting Chargen.  Goodbye.")

