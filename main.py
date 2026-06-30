from src.parser import Parser


def main():
    parser = Parser()

    recruiter_data = parser.read_csv("input/recruiter.csv")
    github_data = parser.read_github_json("input/github.json")

    print("===== Recruiter CSV =====")
    print(recruiter_data)

    print("\n===== GitHub JSON =====")
    print(github_data)


if __name__ == "__main__":
    main()