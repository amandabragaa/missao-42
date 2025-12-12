#!/usr/bin/env python3 


def ord_by_date(item: tuple) -> str:
    return item[1]["date_of_birth"]

def famous_births(famous: dict[str, dict[str, str]]) -> None:
    for info in sorted(famous.items(), key=ord_by_date):
        print(info[1]["name"], "is a great scientist born in", info[1]["date_of_birth"]+".")
    return

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)


