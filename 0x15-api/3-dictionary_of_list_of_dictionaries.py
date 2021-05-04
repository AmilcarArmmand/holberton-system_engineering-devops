#!/usr/bin/python3
"""Script to export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    u_dict = {}
    n_dict = {}

    for user in users:
        u_id = user.get("id")
        u_dict[u_id] = []
        n_dict[u_id] = user.get("username")

    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in todo:
        task_dict = {}
        u_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = n_dict.get(u_id)
        u_dict.get(u_id).append(task_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(u_dict, f)
