from typing import Mapping
from cmdstanconfig import Config


def flatten(data, lst):
    for k, v in data.items():
        if isinstance(v, Mapping):
            lst.append(str(k))
            flatten(v, lst)
        elif v:
            lst.append(f"{k}={v}")


if __name__ == "__main__":
    from parse import parse_csv
    import json

    data = parse_csv("examples/output.txt")
    raw = json.dumps(data, indent=2)

    c = Config.parse_obj(data)
    print(c.json(indent=2))

    # doesn't quite work
    # l = []
    # flatten(data, l)
    # print(" ".join(l))
    with open("cmdstan.schema.json", "w") as f:
        f.write(c.schema_json(indent=2))
