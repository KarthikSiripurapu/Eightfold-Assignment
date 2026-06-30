import phonenumbers


class Normalizer:

    def normalize_phone(self, phone):
        try:
            number = phonenumbers.parse(str(phone), "IN")
            return phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )
        except:
            return str(phone)

    def normalize_skills(self, skills):

        skill_map = {
            "python": "Python",
            "c++": "C++",
            "cpp": "C++",
            "javascript": "JavaScript",
            "js": "JavaScript",
            "fastapi": "FastAPI",
            "machine learning": "Machine Learning",
            "ml": "Machine Learning"
        }

        normalized = []

        for skill in skills:
            skill = skill.strip()
            key = skill.lower()

            if key in skill_map:
                normalized.append(skill_map[key])
            else:
                normalized.append(skill)

        return normalized