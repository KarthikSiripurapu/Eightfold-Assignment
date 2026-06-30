from src.models import Candidate


class Merger:

    def merge(self, recruiter, github):

        candidate = Candidate()

        candidate.candidate_id = recruiter.candidate_id
        candidate.full_name = recruiter.full_name

        candidate.emails = recruiter.emails
        candidate.phones = recruiter.phones

        candidate.headline = recruiter.headline

        candidate.skills = github.skills

        candidate.location = github.location

        return candidate