#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys


def check_tasks(id):
    """ Fetch user name, number of tasks """

    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        done_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)
        num_done_tasks = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'], num_done_tasks, total_tasks))

        for task in done_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)


if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
