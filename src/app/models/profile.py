class ProfilePredictor:
    def get_profile(self, email):
        return {
            'known': ['Python', 'Web'],
            'unknown': ['Java'],
            'courses': [{
                'url': 'http://https://www.udemy.com/course/java-tutorial/',
                'name': 'How to be Java developer',
            }],
        }
