## Perks ########################
## Racial Perks

# Custom(0)
# Human(0)
# Twi'lek(0)
# Devaronian(0)
# Arcona(0)
# Wookie(2) - Claws, Big
# Toydarian(4) - Flight, Small
# Trandoshan(5) - Claws, Darkvision, Natural Armor
# Gungan(2) - Breath Underwater
# Falleen(2) - Pheromones
# Mon Calamari(2) - Breath Underwater
# Hutt(1) - Big
# Ugnaught(1) - Small
# Weequay(2) - Natural Armor

SPECIES = {'human': {'perks': [], 'cost': 0, 'description': ''},
           'twi\'lek': {'perks': [], 'cost': 0, 'description': ''},
           'devaronian': {'perks': [], 'cost': 0, 'description': ''},
           'arcona': {'perks': [], 'cost': 0, 'description': ''},
           'wookiee': {'perks': ['claws', 'big'], 'cost': 5, 'description': ''},
           'toydarian': {'perks': ['flight', 'small'], 'cost': 7, 'description': ''},
           'trandoshan': {'perks': ['claws', 'darkvision', 'natural armor'], 'cost': 5, 'description': ''},
           'gungan': {'perks': ['breath underwater'], 'cost': 2, 'description': ''},
           'falleen': {'perks': ['pheromones'], 'cost': 2, 'description': ''},
           'mon calamari': {'perks': ['breath underwater'], 'cost': 2, 'description': ''},
           'hutt': {'perks': ['big'], 'cost': 4, 'description': ''},
           'ugnaught': {'perks': ['small'], 'cost': 4, 'description': ''},
           'weequay': {'perks': ['natural armor'], 'cost': 2, 'description': ''}}

## Racial Perks ##
# Darkvision(1) - Can see in low light situations.  No penalties to Perception checks.
# Natural Armor(2) - +2 Armor value from Scales, cybernetic enhancements or other means integrated into the physical form.
# Claws(2) - Unarmed attacks gain +2 to damage. +2 to Climb checks
# Flight(3) - Character can fly.  Movement is the same as standard (see help Movement).  Ignore rough terrain penalties.  Can fly up to ten feet off the ground.
# Breath Underwater(2) - Character can breath underwater.  No penalties or Athletics checks to hold breath.
# Big(4) - Max Might set to 5D, Max Agility set to 3D
# Small(4) - Max Agility set to 5D, Max Might set to 3D
# Pheromones(2) - +2 to Charm skills
# Echo Location(3) - User can 'see' objects even in total darkness and can ignore all concealment but they are essentially
#   colorblind when using this perk.  But Sonic weapons are highly effective and do an additional +2D damage

RACIAL_PERKS = {'darkvision': {'cost': 1, 'bonus': {}, 'description': 'User can see in low or zero light conditions.  '
                    'They suffer no penalties to perception in these circumstances.'},
                'natural armor': {'cost': 2, 'bonus': {'armor': 2}, 'description': 'Natural scales, thickened skin or '
                    'other evolutionary mechanism that makes you a little harder to kill.'},
                'claws': {'cost': 2, 'bonus': {}, 'description': '+1D to unarmed combat damage.'},
                'flight': {'cost': 3, 'bonus': {}, 'description': 'Character can fly.  Movement is the same as '
                    'standard (see help Movement).  Ignore rough terrain penalties.  Can fly up to ten feet off the '
                    'ground.'},
                'breath underwater': {'cost': 2, 'bonus': {}, 'description': 'Character can breath underwater.  No '
                    'penalties or Athletics checks to hold breath.'},
                'big': {'cost': 4, 'bonus': {'max_might': 5, 'max_agility': 3}, 'description': 'Max Might set to 5D, '
                    'Max Agility set to 3D'},
                'small': {'cost': 4, 'bonus': {'max_agility': 5, 'max_might': 3}, 'description': 'Max Agility set to '
                    '5D, Max Might set to 3D'},
                'pheromones': {'cost': 2, 'bonus': {'charm': '+2'}, 'description': 'You have a natural pheromone that '
                    'you excrete.  It has a mild intoxicating effect.  You gain a +2 to all charm skills'},
                'echo location': {'cost': 3, 'bonus': {}, 'description': 'User can "see" objects even in total '
                    'darkness and can ignore all concealment but they are essentially colorblind when using this '
                    'perk.  But Sonic weapons are highly effective and do an additional +2D damage'}}


## General Perks ##
# Force Sensitivity(5) - A connection with the Force is possible.  This unlocks the Force Skill.
# Education(4) - +2 to all Wit skills
# Deft(4) - +2 to all Agility skills
# Charismatic(4) - +2 to all Charm skills
# Tank(4) - +2 to all Might skills

GENERAL_PERKS = {'force sensitivity': {'cost': 5, 'bonus': {'force_sensitive': True}, 'description': 'You possess a '
                    'latent connection with the mystical energy field that surrounds all life.  You gain the ability '
                    'to learn Force skills and powers.'},
                 'education': {'cost': 4, 'bonus': {'wit': '+2'}, 'description': 'You have received a formal education '
                    'and has a trained mind. +2 to all Wit skills.'},
                 'deft': {'cost': 4, 'bonus': {'agility': '+2'}, 'description': 'You have natural dexterity.  +2 on all '
                    'Agility skills'},
                 'charismatic': {'cost': 4, 'bonus': {'charm': '+2'}, 'description': 'You have a natural affinity for '
                    'charm and interaction with other sentient beings. +s to all Charm skills'},
                 'tank': {'cost': 4, 'bonus': {'might': '+2'}, 'description': 'You are naturally tough.  Either through '
                    'conditioning or some natural means, you are a bit stronger and harder than others.  +2 to all '
                    'Might skills'}}


## Force Powers ##
# Force Jump(1) - Force assisted jump that adds height or length to the jump based on need and Force Skill check. (TN 10) +2D to Acrobatics check
# Force Speed(1) - Force assisted speed.  Can be used to evade (doubles dodge roll for 1 round) (TN 10) +2D to Running check
# Telepathy(1) - Ability to send(TN 15) and receive(TN 10) telepathic messages. Resist=Wit
# Telekinesis(1) - Ability to lift 10kg x Force die with only the Force. (TN 15)  To use as a thrown weapon, check Throwing vs dodge, as per normal rules) Resist=Might
# Force Parry(2) - Ability to use the force to guide your hand when attempting to Parry an incoming attack.  Adds +2 to Parry TN=15
# Force Grip(3) - Causes target to drop held weapon at their own feet.  Can be picked up on next turn if not otherwise prevented.  Resist=Agility TN=15
# Force Slam(3) - The Force manipulates air molecules to forms a gust of wind that slams into a target. Resist=Might TN=15 +3D to throwing 2D damage
# Force Choke(4) - The Force compresses the air molecules around the targets neck to compress their ability to breath.  Resist=Might TN=20 +2D to brawling 3D damage
# Force Lightning(5) - The Force charges particles in the air forming lightning from the user to the target.  TN=25 +3D to Firearms Resist=Agility 4D Damage
# Mind Trick(3) - The Force enhances the user's ability to influence others. TN=15 +1D to Charm skills Resist=Wit
# Force Sense(2) - The Force guides the user.  TN=10 +2D to Perception

FORCE_PERKS = {'force jump': {'cost': 1, 'tn': 10, 'bonus': {'acrobatics': '+2D'}, 'description': 'Force assisted jump that adds '
                    'height or length to the jump based on need and Force Skill check. (TN 10) +2D to Acrobatics check', 'resist': ''},
               'force speed': {'cost': 1, 'tn': 10, 'bonus': {'dodge': 'x2', 'running': '+2D'}, 'description': 'Force '
                    'assisted speed.  Can be used to evade (doubles dodge roll for 1 round) (TN 10) +2D to Running '
                    'check', 'resist': ''},
               'telepathy': {'cost': 1, 'tn': 10, 'bonus': {}, 'description': 'Ability to send(TN 15) and '
                    'receive(TN 10) telepathic messages. Resist=Wit', 'resist': 'wit'},
               'telekinesis': {'cost': 1, 'tn': 15, 'bonus': {}, 'description': 'Ability to lift 10kg x Force die with '
                    'only the Force. (TN 15)  To use as a thrown weapon, check Throwing vs dodge, as per normal rules) '
                    'Resist=Might', 'resist': 'might'},
               'force parry': {'cost': 2, 'tn': 15, 'bonus': {'parry': '+2'}, 'description': 'Ability to use the force to guide '
                    'your hand when attempting to Parry an incoming attack.  Adds +2 to Parry TN=15', 'resist': ''},
               'force grip': {'cost': 3, 'tn': 15, 'bonus': {}, 'description': 'Causes target to drop held item, '
                    'including weapons, at their own feet.  Can be picked up on next turn if not otherwise prevented.  '
                    'Resist=Agility TN=15', 'resist': 'agility'},
               'force slam': {'cost': 3, 'tn': 15, 'bonus': {'throwing': '+3D', 'damage': '2D'}, 'description': 'The '
                    'Force manipulates air molecules to forms a gust of wind that slams into a target. Resist=Might '
                    'TN=15 +3D to throwing 2D damage'},
               'force choke': {'cost': 4, 'tn': 20, 'bonus': {'brawling': '+2D', 'damage': '3D'}, 'description': 'The '
                    'Force compresses the air molecules around the targets neck to compress their ability to breath.  '
                    'Resist=Might TN=20 +2D to brawling 3D damage', 'resist': 'might'},
               'force lightning': {'cost': 5, 'tn': 25, 'bonus': {'firearms': '+3D', 'damage': '4D'}, 'description':
                   'The Force charges particles in the air forming lightning from the user to the target.  TN=25 +3D '
                   'to Firearms Resist=Agility 4D Damage', 'resist': 'agility'},
               'mind trick': {'cost': 3, 'tn': 15, 'bonus': {'charm': '+1D'}, 'description': 'The Force enhances the '
                    'user\'s ability to influence others. TN=15 +1D to Charm skills Resist=Wit', 'resist': 'wit'},
               'force sense': {'cost': 2, 'tn': 10, 'bonus': {'perception': '+2D'}, 'description': 'The Force guides '
                    'the user.  TN=10 +2D to Perception', 'resist': ''}}
