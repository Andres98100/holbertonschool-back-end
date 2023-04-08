#!/usr/bin/python3
"""import"""
import json
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{URL}/users").json()
    dic_user = {}
    for user in users:
        tasks = requests.get(f"{URL}/users/{user['id']}/todos").json()
        dic_user[user["id"]] = []
        for task in tasks:
            dic_task = {"task": task["title"], "completed": task["completed"],
                        "username": user["username"]}
            dic_user[user["id"]].append(dic_task)
    with open("todo_all_employees.json", "w") as file:
        json.dump(dic_user, file)
