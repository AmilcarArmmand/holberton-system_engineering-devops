#!/usr/bin/python3
"""Script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    # request for user data
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId)).json()

    with open("{}.csv".format(userId), 'w', newline='') as f:
        spamwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo:
            spamwriter.writerow([int(userId), user.get("username"),
                                 task.get("completed"), task.get("title")])
