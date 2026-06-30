class Validator:

    def validate(self, candidate):

        errors = []

        if not candidate.full_name:
            errors.append("Missing full name")

        if len(candidate.emails) == 0:
            errors.append("Missing email")

        if len(candidate.phones) == 0:
            errors.append("Missing phone")

        return errors