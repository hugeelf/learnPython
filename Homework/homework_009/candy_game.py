import random
from random import randint


def gen_bot_candy (candy):
    bot_candy = randint(1, 28)
    if candy <= 28 and candy > 0:
        bot_candy = candy
        return bot_candy
    elif candy <= 56 and candy > 28:
        bot_candy = candy-29
        if bot_candy == 0:
            return bot_candy
    return bot_candy