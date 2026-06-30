from src.parser import Parser
from src.merger import Merger


def print_candidate(candidate):

    print("Candidate ID :", candidate.candidate_id)
    print("Name         :", candidate.full_name)
    print("Emails       :", candidate.emails)
    print("Phones       :", candidate.phones)
    print("Headline     :", candidate.headline)
    print("Skills       :", candidate.skills)
    print("Location     :", candidate.location)
    print("-" * 50)


def main():

    parser = Parser()
    merger = Merger()

    # Read input files
    csv_candidates = parser.read_csv("input/recruiter.csv")
    github_candidates = parser.read_github_json("input/github.json")

    # Merge the first CSV candidate with the first GitHub profile
    merged_candidate = merger.merge(
        csv_candidates[0],
        github_candidates[0]
    )

    print("\n========== MERGED CANDIDATE ==========\n")
    print_candidate(merged_candidate)


if __name__ == "__main__":
    main()