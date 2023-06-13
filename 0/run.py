from hermes import Hermes
from constants import Const

#with Hermes(country="us") as bot:
bot=Hermes("us")
bot.checkdrops()

""" const=Const()
for key in const.country:
    with Hermes() as bot:
        bot.checkdrops(key.lower()) """
    