import random
import re
import string

from model.contact import Contact
from model.group import Group


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


def generate_contact(c_id=None, c_type=True):
    if c_type:
        new_f_name = clear_data(rnd_string(20))
        new_l_name = clear_data(rnd_string(30))
        new_m_name = clear_data(rnd_string(20))
        new_id = c_id
        new_addr = rnd_big_text_field()
        phone_numbers = []
        e_mails = []
        for i in range(1, 5):
            gen_phone_num = '+7' + str(random.randint(1111111111, 9999999999))
            phone_numbers.append(random.choice([gen_phone_num, ""]))

        for i in range(1, 5):
            gen_e_mail = clear_data(rnd_string(10) + '@'
                                    + rnd_string(10) + '.' + rnd_string(3))
            e_mails.append(random.choice([gen_e_mail, ""]))
    else:
        new_f_name = 'Andrey'
        new_l_name = 'Romanov'
        new_id = c_id
        new_m_name = 'S'
        new_addr = 'Default City'
        phone_numbers = ['+79874561234', '79874565678']
        e_mails = ['and.romanov@gmail.com']
    return Contact(id=new_id, f_name=new_f_name, l_name=new_l_name, m_name=new_m_name, addr=new_addr,
                   h_phone=phone_numbers[0],
                   m_phone=phone_numbers[1], w_phone=phone_numbers[2], s_phone=phone_numbers[3],
                   e_mail1=e_mails[0], e_mail2=e_mails[1], e_mail3=e_mails[2])


def generate_group(g_id=None, c_type=True):
    if c_type:
        new_name = clear_data(rnd_string(30))
        new_head = clear_data(rnd_string(40))
        new_foot = clear_data(rnd_string(40))
        new_id = g_id
    else:
        new_name = 'New Custom Group'
        new_head = 'New head'
        new_foot = 'New foot'
        new_id = g_id
    return Group(id=new_id, name=new_name, header=new_head, footer=new_foot)


def clean_db_contacts(cont):
    return Contact(id=cont.id, f_name=clear_data(cont.f_name), l_name=clear_data(cont.l_name))


def clean_db_groups(group):
    return Group(id=group.id, name=clear_data(group.name))
