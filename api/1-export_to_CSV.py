#!/usr/bin/python3
"""import"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])
    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    fileName = "USER_ID.csv"
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open(fileName, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerow(
                {"USER_ID": EMPLOYEE_ID, "USERNAME": EMPLOYEE_NAME,
                 "TASK_COMPLETED_STATUS": str(task["completed"]),
                 "TASK_TITLE": task["title"]}
            )

    for title in TASK_TITLE:
        print("\t ", title)
