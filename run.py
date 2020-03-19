import os
import datetime
import json
import requests


DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data"
)

URL = "https://coronavirus-19-api.herokuapp.com/countries"


def main():
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries").json()
    file_path = os.path.join(
        DATA_DIR, datetime.datetime.now().strftime("%Y%b%d%H%M%S") + ".json"
    )
    with open(file_path, "w+") as f1:
        json.dump(data, f1)


if __name__ == "__main__":
    main()
