from model.contact import Contact
import fixture.common as common
from sys import maxsize
import os.path as op
import jsonpickle
import getopt
import sys
import random

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["contacts quantity", "file path"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

n = 5
f = "test_data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def generate_contact_data():
    new_f_name = common.clear_data(common.rnd_string(20))
    new_l_name = common.clear_data(common.rnd_string(30))
    new_m_name = common.clear_data(common.rnd_string(20))
    new_id = maxsize
    new_addr = common.rnd_big_text_field()
    phone_numbers = []
    e_mails = []
    for i in range(1, 5):
        gen_phone_num = '+7' + str(random.randint(1111111111, 9999999999))
        phone_numbers.append(random.choice([gen_phone_num, ""]))

    for i in range(1, 5):
        gen_e_mail = common.clear_data(common.rnd_string(10) + '@'
                                       + common.rnd_string(10) + '.' + common.rnd_string(3))
        e_mails.append(random.choice([gen_e_mail, ""]))
    return Contact(id=new_id, f_name=new_f_name, l_name=new_l_name, m_name=new_m_name, addr=new_addr,
                   h_phone=phone_numbers[0], m_phone=phone_numbers[1], w_phone=phone_numbers[2],
                   s_phone=phone_numbers[3],
                   e_mail1=e_mails[0], e_mail2=e_mails[1], e_mail3=e_mails[2])


test_data = [
    generate_contact_data()
    for i in range(n)
]

file = op.join(op.dirname(op.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
