import json

class User:
    """Defines user objects"""

    def __init__(self, fname: str, lname: str, email: str, mname: str = None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email

    def __iter__(self):
        yield from {
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "mname": self.mname,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return User(json_dct['fname'],
                    json_dct['lname'],
                    json_dct['email'],
                    json_dct['mname'])
