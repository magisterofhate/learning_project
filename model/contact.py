from sys import maxsize


class Contact:
    def __init__(self, id=None, f_name='Firstname', l_name='Lastname', m_name='Middle',
                 addr="Default City", h_phone="+79295341678",
                 m_phone="+78856781256", w_phone="+7(885)6784556", s_phone="+7(885)678-12-56",
                 e_mail1="User_test@gh.ty", e_mail2="User_test222@gh.ty", e_mail3="User333_test333@gh.ty",
                 day_dob="5", month_dob="August", year_dob="1986"):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.m_name = m_name
        self.addr = addr
        self.h_phone = h_phone
        self.m_phone = m_phone
        self.w_phone = w_phone
        self.s_phone = s_phone
        self.e_mail1 = e_mail1
        self.e_mail2 = e_mail2
        self.e_mail3 = e_mail3
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
