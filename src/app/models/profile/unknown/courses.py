class CourseSelector:

    def find_course(self, courses, skill):
        for course in courses:
            if course['skill'] == skill:
                return {
                    'url': course['url'],
                    'name': course['name'],
                }
