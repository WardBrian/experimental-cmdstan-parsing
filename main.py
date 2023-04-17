from typing import Mapping
from cmdstanconfig import Config


def flatten(data, lst, eq=False):
    for k, v in data.items():
        if isinstance(v, Mapping):
            if eq:
                lst.append(f"={k}")
            else:
                lst.append(str(k))
            flatten(v, lst, not eq)
        elif v:
            if isinstance(v, bool):
                lst.append(f"{k}={int(v)}")
            else:
                lst.append(f"{k}={v}")


def compose_cmd(model):
    data = model.dict(
        exclude={
            "filename",
            "stan_version_major",
            "stan_version_minor",
            "stan_version_patch",
            "model",
            "start_datetime",
            "stanc_version",
            "stancflags",
        }
    )
    l = []
    flatten(data, l)
    return " ".join(l).replace(" =", "=")


if __name__ == "__main__":
    from parse import read_csv_header
    import json

    data = read_csv_header("examples/output2.txt")
    raw = json.dumps(data, indent=2)
    print(raw)

    c = Config.parse_obj(data)
    print(c.json(indent=2))

    print(compose_cmd(c))
    # with open("cmdstan.schema.json", "w") as f:
    #     f.write(c.schema_json(indent=2))
