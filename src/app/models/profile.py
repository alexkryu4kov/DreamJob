class ProfilePredictor:
    def get_profile(self, email):
        return {
            'known': ['Python', 'Web'],
            'unknown': ['Java'],
            'courses': ['How to be Java developer'],
        }
