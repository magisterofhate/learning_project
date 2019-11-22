import random
import re
import string


def rnd_string(length):
    symbols = string.ascii_letters + " "*10 + string.digits
    return ''.join(random.choice(symbols) for i in range(random.randrange(length)))


def rnd_big_text_field():
    let = string.ascii_letters
    dig = string.digits
    n = "\n"
    return ''.join(random.choice([random.choice(let), random.choice(dig), n]) for i in range(50))


def clear_data(s):
    return re.sub("\s{2,}", " ", s.strip(' '))

