# Clue Game (refer to clueGame.txt for explanation of the game)

"""
Propositional Symbols :
---------------------
mustard   ballroom   knife
plum      kitchen    revolver
scarlet   library    wrench
===========================================================================

(mustart V plum V scarlet)
(ballroon V kitchen V library)
(knife V revolver V wrench)

"""

import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),
)

# Initial cards { I have my initial cards so i am sure that it is not mustard , kitchen and revolver }
knowledge.add(And(Not(mustard), Not(kitchen), Not(revolver)))

# Unknown card
knowledge.add(Or(Not(scarlet), Not(library), Not(wrench)))

# Known cards
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

check_knowledge(knowledge)
