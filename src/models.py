class Candidate:

    def __init__(self):
        self.candidate_id = None
        self.full_name = None

        self.emails = []
        self.phones = []

        self.location = {
            "city": None,
            "region": None,
            "country": None
        }

        self.links = {
            "github": None,
            "linkedin": None,
            "portfolio": None,
            "other": []
        }

        self.headline = None
        self.years_experience = None

        self.skills = []

        self.experience = []

        self.education = []

        self.provenance = []

        self.overall_confidence = 0.0