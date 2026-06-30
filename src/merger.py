from src.models import Candidate
from src.normalizer import Normalizer


class Merger:

    def merge(self, recruiter, github):

        normalizer = Normalizer()
        candidate = Candidate()

        # Basic Information
        candidate.candidate_id = recruiter.candidate_id
        candidate.full_name = recruiter.full_name

        # Emails
        candidate.emails = recruiter.emails

        # Normalize Phone Numbers
        candidate.phones = [
            normalizer.normalize_phone(phone)
            for phone in recruiter.phones
        ]

        # Headline
        candidate.headline = recruiter.headline

        # Normalize Skills
        candidate.skills = normalizer.normalize_skills(github.skills)

        # Location
        candidate.location = github.location

        return candidate