from logic import *

rain = Symbol("rain")  # it is raining
hagrid = Symbol("hagrid")  # harry visited hagrid
dumbledore = Symbol("dumbledore")  # harry visited dumbledore

# knowledge is an and of multiple sentences
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore,
)

print(model_check(knowledge, rain)) # True
