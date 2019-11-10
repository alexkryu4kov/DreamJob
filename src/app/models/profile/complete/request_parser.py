class Request:
    def __init__(self) -> None:
        self._skill = None
        self._email = None

    @property
    def skill(self) -> str:
        return self._skill

    @skill.setter
    def skill(self, skill: str) -> None:
        try:
            self._skill = skill
        except KeyError:
            self._skill = ''

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        try:
            self._email = email
        except KeyError:
            self._email = ''


class RequestParser(Request):
    def __init__(self) -> None:
        super().__init__()

    def parse(self, request: dict) -> None:
        self.email = request['email']
        self.skill = request['skill']
