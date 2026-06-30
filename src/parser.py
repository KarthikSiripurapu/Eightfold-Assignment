import json
import pandas as pd
from src.models import Candidate


class Parser:

    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        candidates = []

        for _, row in df.iterrows():
            candidate = Candidate()

            candidate.candidate_id = str(row["candidate_id"])
            candidate.full_name = row["name"]

            candidate.emails.append(row["email"])
            candidate.phones.append(str(row["phone"]))

            candidate.headline = row["title"]

            candidates.append(candidate)

        return candidates

    def read_github_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        candidates = []

        for item in data:

            candidate = Candidate()

            candidate.full_name = item["name"]
            candidate.headline = item["bio"]

            candidate.location["country"] = "India"

            candidate.skills = item["languages"]

            candidates.append(candidate)

        return candidates