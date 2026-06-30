import json
import pandas as pd


class Parser:

    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")

    def read_github_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)