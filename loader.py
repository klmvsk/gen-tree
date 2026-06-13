import json


def load_people(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    people = {}
    for person in data:
        people[person["name"]] = person
    return people
