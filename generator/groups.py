from model.group import Group
import fixture.common as common
from sys import maxsize
import os.path as op
import jsonpickle


def generate_group_data():
    new_name = common.clear_data(common.rnd_string(30))
    new_head = common.clear_data(common.rnd_string(40))
    new_foot = common.clear_data(common.rnd_string(30))
    new_id = maxsize
    return Group(id=new_id, name=new_name, header=new_head, footer=new_foot)


test_data = [
    generate_group_data()
    for i in range(5)
]

file = op.join(op.dirname(op.abspath(__file__)), "../test_data/groups.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
