#!/usr/bin/python3
"""import"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    username = data[0]["user"]["username"]
    USER_TASK = {EMPLOYEE_ID: []}
    for task in data:
        dic_task = {"task": task["title"], "completed": task["completed"],
                    "username": username}
        USER_TASK[EMPLOYEE_ID].append(dic_task)
    fileName = "USER_ID.json"
    with open(fileName, "w") as file:
        json.dump(USER_TASK, file)
