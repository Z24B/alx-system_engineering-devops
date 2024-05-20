#!/usr/bin/python3
"""
Gathers data from an API for a given employee ID and displays their TODO list progress.
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def gather_data(employee_id):
    """Fetch employee TODO list progress"""
    # Fetch user info
    user_response = requests.get(users_url + f'/{employee_id}')
    if user_response.status_code != 200:
        print("User not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todo_response = requests.get(todos_url, params={'userId': employee_id})
    if todo_response.status_code != 200:
        print("TODO list not found")
        return

    todo_data = todo_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_data(employee_id)
