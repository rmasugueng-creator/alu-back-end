#!/usr/bin/python3
"""Exports employee TODO list data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, emp_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": emp_id}).json()

    username = user.get("username")
    tasks_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    data = {emp_id: tasks_list}
    filename = "{}.json".format(emp_id)

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)
