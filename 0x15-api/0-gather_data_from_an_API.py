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
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userID={}".
                        format(user_id)).json()
    completed_tasks = []
    for item in todo:
        if item.get("completed") is True:
            completed_tasks.append(item.get("title"))
    # EMPLOYEE_NAME NUMBER_OF_DONE_TASKS / TOTAL_NUMBER_OF_TASKS
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed_tasks), len(todos)))
    for item in todos:
        print("\t {}".format(item.get("title")))
