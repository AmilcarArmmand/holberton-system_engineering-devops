#!/usr/bin/python3
"""Script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    u_id = argv[1]
    # request for user data
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(u_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(u_id)).json()

    username = user.get("username")

    new_list = []
    task_dict = {}
    for task in todo:
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = username
        new_list.append(task_dict)
        task_dict = {}
    jso = {}
    jso[u_id] = new_list
    with open("{}.json".format(u_id), 'w') as f:
        json.dump(jso, f)
