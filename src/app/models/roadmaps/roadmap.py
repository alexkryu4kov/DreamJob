import random
from dataclasses import asdict, dataclass


@dataclass
class Roadmap:
    courses: list
    name: str = None
    url: str = None
    priority: str = None

    def choose_course(self):
        self.name = self.courses[0]['name']
        self.url = self.courses[0]['url']

    def generate_priority(self):
        self.priority = random.randint(1, 6)

    def get(self):
        self.choose_course()
        self.generate_priority()
        roadmap = asdict(self)
        del roadmap['courses']
        return roadmap
