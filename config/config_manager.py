import json
from pathlib import Path


class ConfigManager:

    @classmethod
    def read_json_data(cls, path):
        file_path = Path(__file__).parent.joinpath(path)

        with open(file_path) as json_file:
            json_data = json.load(json_file)

        return json_data

    @classmethod
    def get_artifact_path(cls, path):
        return Path(__file__).parent.parent.joinpath("artifacts") / path
