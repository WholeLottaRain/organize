def a_liq1(code_1240, code_1250, code_1500):
    return (code_1240 + code_1250) / code_1500


def a_liq2(code_1240, code_1250, code_1510, code_1520, code_1550):
    return (code_1240 + code_1250) / (code_1510 + code_1520 + code_1550)


def n_liq(code_1200, code_1500):
    return code_1200 / code_1500


def p_liq(code_1230, code_1240, code_1250, code_1500):
    return (code_1230 + code_1240 + code_1250) / code_1500


def all_liq(data, result):
    a_liq1_list = []
    a_liq2_list = []
    n_liq_list = []
    p_liq_list = []
    for year in data.get("years"):
        a_liq1_list.append(round(a_liq1(year["1240"], year["1250"], year["1500"]), 4))
        a_liq2_list.append(round(a_liq2(year["1240"], year["1250"], year["1510"], year["1520"], year["1550"]), 4))
        n_liq_list.append(round(n_liq(year["1200"], year["1500"]), 4))
        p_liq_list.append(round(p_liq(year["1230"], year["1240"], year["1250"], year["1500"]), 4))
    result.update({"Абсолютная ликвидность v1": a_liq1_list})
    result.update({"Абсолютная ликвидность v2": a_liq2_list})
    result.update({"Текущая ликвидность": n_liq_list})
    result.update({"Промежуточная ликвидность": p_liq_list})
    return result


def rent_roe(code_2400, code_1300):
    return code_2400 / code_1300


def rent_roa(code_2400, code_1600_1, code_1600_2):
    return code_2400 / ((code_1600_1 + code_1600_2) / 2) * 100


def rent_all(data, result):
    roe_list = []
    roa_list = []
    for i in range(len(data.get("years")) - 1):
        roe_list.append(round(rent_roe(data["years"][i]["2400"], data["years"][i]["1300"]), 4))
    for i in range(len(data.get("years")) - 1):
        roa_list.append(
            round(rent_roa(data["years"][i]["2400"], data["years"][i]["1600"], data["years"][i + 1]["1600"]), 4))
    result.update({"Рентабельность собственного капитала": roe_list})
    result.update({"Рентабельность активов": roa_list})
    return result


def active(code_1600_1, code_1600_2):
    return (code_1600_1 + code_1600_2) / 2


def active_all(data, result):
    active_list = []
    for i in range(len(data.get("years")) - 1):
        active_list.append(round(active(data["years"][i]["1600"], data["years"][i + 1]["1600"]), 4))
    result.update({"Средние активы": active_list})
    return result


def lever(code_1300, code_1400, code_1700):
    return (code_1400 + code_1700) / code_1300


def lever_all(data, result):
    lever_list = []
    for year in data.get("years"):
        lever_list.append(round(lever(year["1300"], year["1400"], year["1700"]), 4))
    result.update({"Плечо финансового рычага": lever_list})
    return result
