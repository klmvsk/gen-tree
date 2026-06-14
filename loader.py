import json


def load_people(filename):
    """
    Читает людей из JSON файла и возвращает словарь, где ключ это имя.
    """
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    people = {}
    # складываем каждого человека в словарь по его имени
    for person in data:
        people[person["name"]] = person
    return people
