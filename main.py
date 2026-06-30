from src.parser import Parser
from src.merger import Merger
from src.confidence import Confidence
from src.projector import Projector
from src.validator import Validator


def print_candidate(candidate):

    print("Candidate ID :", candidate.candidate_id)
    print("Name         :", candidate.full_name)
    print("Emails       :", candidate.emails)
    print("Phones       :", candidate.phones)
    print("Headline     :", candidate.headline)
    print("Skills       :", candidate.skills)
    print("Location     :", candidate.location)
    print("Confidence   :", candidate.overall_confidence)
    print("-" * 50)


def main():

    parser = Parser()
    merger = Merger()
    confidence = Confidence()
    validator = Validator()
    projector = Projector()

    csv_candidates = parser.read_csv("input/recruiter.csv")
    github_candidates = parser.read_github_json("input/github.json")

    merged_candidate = merger.merge(
        csv_candidates[0],
        github_candidates[0]
    )

    merged_candidate = confidence.calculate(merged_candidate)

    errors = validator.validate(merged_candidate)

    if errors:
        print("Validation Errors:")
        for error in errors:
            print("-", error)
        return

    projector.save(
        merged_candidate,
        "output/output.json"
    )

    print_candidate(merged_candidate)

    print("\nOutput saved to output/output.json")


if __name__ == "__main__":
    main()