#!/usr/bin/python3
"""Export data to JSON."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch todos for the given employee ID
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Fetch user info for the given employee ID
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    user_response = requests.get(user_url)
    user_info = user_response.json()
    username = user_info.get('username')

    # Prepare data for JSON export
    tasks_list = [{
        "task": task['title'],
        "completed": task['completed'],
        "username": username
    } for task in todos]

    tasks_data = {str(employee_id): tasks_list}

    # JSON file name
    json_file = "{}.json".format(employee_id)

    # Write to JSON file
    with open(json_file, 'w') as file:
        json.dump(tasks_data, file)

    print("JSON file generated: {}".format(json_file))
