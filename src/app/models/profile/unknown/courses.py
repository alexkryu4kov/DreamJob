class CourseSelector:

    def find_course(self, courses: list, skill: str) -> dict:
        for course in courses:
            if course['skill'] == skill:
                return {
                    'url': course['url'],
                    'name': course['name'],
                }
