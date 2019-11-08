from sys import maxsize


class Contact:
    def __init__(self, id=None, f_name='Firstname', l_name='Lastname', addr="Default City", h_phone="+79295341678",
                 m_phone="+78856781256", e_mail="User_test@gh.ty", day_dob="5", month_dob="August", year_dob="1986"):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.addr = addr
        self.h_phone = h_phone
        self.m_phone = m_phone
        self.e_mail = e_mail
        self.day_dob = day_dob
        self.month_dob = month_dob
        self.year_dob = year_dob

    def __repr__(self):
        return "%s; %s; %s" % (self.id, self.f_name, self.l_name)

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return (self.id == other.id or self.id == maxsize or other.id == maxsize) \
               and self.f_name == other.f_name and self.l_name == other.l_name
