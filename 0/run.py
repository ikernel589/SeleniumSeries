from hermes import Hermes
from constants import Const

with Hermes() as bot:
    bot.checkdrops('ca')

""" const=Const()
for key in const.country:
    with Hermes() as bot:
        bot.checkdrops(key.lower()) """
    