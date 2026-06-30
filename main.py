from src.parser import Parser


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

    csv_candidates = parser.read_csv("input/recruiter.csv")
    github_candidates = parser.read_github_json("input/github.json")

    print("\n========== CSV ==========\n")

    for candidate in csv_candidates:
        print_candidate(candidate)

    print("\n========== GitHub ==========\n")

    for candidate in github_candidates:
        print_candidate(candidate)


if __name__ == "__main__":
    main()