class Confidence:

    def calculate(self, candidate):

        score = 0.0

        # Name
        if candidate.full_name:
            score += 0.20

        # Email
        if len(candidate.emails) > 0:
            score += 0.20

        # Phone
        if len(candidate.phones) > 0:
            score += 0.20

        # Skills
        if len(candidate.skills) > 0:
            score += 0.20

        # Country
        if candidate.location["country"] is not None:
            score += 0.20

        candidate.overall_confidence = round(score, 2)

        return candidate