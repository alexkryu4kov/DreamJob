class Request:
    def __init__(self):
        self._skill = None
        self._email = None

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        try:
            self._skill = skill
        except KeyError:
            self._skill = ''

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        try:
            self._email = email
        except KeyError:
            self._email = ''


class RequestParser(Request):
    def __init__(self):
        super().__init__()

    def parse(self, request):
        self.email = request['email']
        self.skill = request['skill']
