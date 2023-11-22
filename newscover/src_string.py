
from pathlib import Path
import json


def get_sources():
    uspath = Path(__file__).parent.parent / "sources_us.json"
    capath = Path(__file__).parent.parent / "sources_ca.json"
    with open (uspath, "r") as json_data:
        content = json.load(json_data)
        id_list = [item["id"] for item in content]
        comma_separated_ids = ",".join(id_list)
        us_sources = comma_separated_ids
    print(us_sources)

    with open (capath, "r") as json_data:
        content = json.load(json_data)
        id_list = [item["id"] for item in content]
        comma_separated_ids = ",".join(id_list)
        ca_sources = comma_separated_ids
    tgt = f"{us_sources},{ca_sources}"

    return tgt