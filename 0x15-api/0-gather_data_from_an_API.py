#!/usr/bin/python3
"""Script that uses REST API to get user information on TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    # request for user data
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    # request for todos data
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                         format(user_id)).json()
    completed_tasks = []
    for task in todo:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

#    task = [task for task in todo if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed_tasks), len(todo)))

    for task in todo:
        print("\t {}".format(task.get("title")))

    # print("\n".join("\t {}".format(item) for item in completed_tasks))
