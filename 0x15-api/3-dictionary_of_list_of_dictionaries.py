#!/usr/bin/python3
"""Export all employees' tasks to JSON."""
import json
import requests
import sys

if __name__ == "__main__":
    # Fetch all users
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch all todos
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare data for JSON export
    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [{
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        } for task in todos if task['userId'] == user_id]
        all_tasks[str(user_id)] = user_tasks

    # JSON file name
    json_file = "todo_all_employees.json"

    # Write to JSON file
    with open(json_file, 'w') as file:
        json.dump(all_tasks, file)
