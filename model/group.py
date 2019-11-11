from sys import maxsize


class Group:

    def __init__(self, id=None, name='Name', header='Header', footer='Footer'):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "%s; %s" % (self.id, self.name)

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return (self.id == other.id or self.id == maxsize or other.id == maxsize) \
               and self.name == other.name
