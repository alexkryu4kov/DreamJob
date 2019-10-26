class ProfilePredictor:
    def get_known(self, email):
        return {
            'known': ['Python', 'Web']
        }

    def get_unknown(self, email):
        return [
            {
                'name': 'Java',
                'courses': [{
                    'url': 'http://https://www.udemy.com/course/java-tutorial/',
                    'name': 'How to be Java developer',
                }],
            },
            {
                'name': 'Python',
                'courses': [{
                    'url': 'http://https://www.udemy.com/course/python-tutorial/',
                    'name': 'How to be Python developer',
                }],
            },
            {
                'name': 'Web',
                'courses': [{
                    'url': 'http://https://www.udemy.com/course/web-tutorial/',
                    'name': 'How to be Web developer',
                }],
            }
        ]

    def post_profile(self, data):
        return {
            'status': 'OK',
        }
