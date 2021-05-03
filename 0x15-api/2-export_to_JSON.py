#!/usr/bin/python3
"""Script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    # request for user data
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId)).json()

    username = user.get("username")
    task_list = []
    item_dict = {}
    for task in todo:
        item_dict["task"] = task.get('title')
        item_dict["completed"] = task.get('completed')
        item_dict["username"] = user.get('username')
        task_list.append(item_dict)
    jso = {}
    jso[userId] = task_list
    with open("{}.json".format(userId), 'w') as f:
        json.dump(jso, f)
