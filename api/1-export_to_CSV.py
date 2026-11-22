#!/usr/bin/python3
"""Exports employee TODO list data to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1][1]
    base_url = "https://typicode.com"

    user = requests.get("{}/users/{}".format(base_url, emp_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": emp_id}).json()

    username = user.get("username")
    filename = "{}.csv".format(emp_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
