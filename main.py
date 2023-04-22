import json
from calculate import *


def load_params():
    with open("params.json", "r") as f:
        params = json.load(f)
    return params


def write_result(res):
    with open("result.json", "w", encoding="utf8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    data = load_params()
    result = {}
    result = all_liq(data, result)
    result = rent_all(data, result)
    result = active_all(data, result)
    result = lever_all(data, result)
    write_result(result)
