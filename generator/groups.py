import model.group as group
import fixture.common as common
from sys import maxsize
import os.path as op
import jsonpickle
import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["groups quantity", "file path"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

n = 5
f = "test_data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def generate_group_data():
    new_name = common.clear_data(common.rnd_string(30))
    new_head = common.clear_data(common.rnd_string(40))
    new_foot = common.clear_data(common.rnd_string(30))
    new_id = maxsize
    return group.Group(id=new_id, name=new_name, header=new_head, footer=new_foot)


test_data = [
    generate_group_data()
    for i in range(n)
]

file = op.join(op.dirname(op.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
