import json


def card_save(card, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(card, f, indent=2, ensure_ascii=False)


# encoding="utf-8"


def card_load(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
