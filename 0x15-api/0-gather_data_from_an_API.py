#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
    response = requests.get(url)
    todos = response.json()

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    user_response = requests.get(user_url)
    user_info = user_response.json()
    employee_name = user_info.get('name')

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t", task.get('title'))
