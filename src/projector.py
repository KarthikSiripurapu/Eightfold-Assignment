import json


class Projector:

    def project(self, candidate):

        return {
            "candidate_id": candidate.candidate_id,
            "full_name": candidate.full_name,
            "emails": candidate.emails,
            "phones": candidate.phones,
            "location": candidate.location,
            "headline": candidate.headline,
            "skills": candidate.skills,
            "experience": candidate.experience,
            "education": candidate.education,
            "links": candidate.links,
            "overall_confidence": candidate.overall_confidence
        }

    def save(self, candidate, output_path):

        data = self.project(candidate)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return data