def find_course(courses: list, skill: str) -> list:
    return [{
        'url': course['url'],
        'name': course['name'],
    } for course in courses if course['skill'] == skill]
