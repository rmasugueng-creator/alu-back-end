#!/usr/bin/python3
"""Gathers employee TODO list progress from a REST API."""
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

    emp_name = user.get("name")
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(done_tasks), len(todos)))

    for title in done_tasks:
        print("\t {}".format(title))
