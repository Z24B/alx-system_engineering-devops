#!/usr/bin/python3
"""Export data to CSV."""
import csv
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

    # CSV file name
    csv_file = "{}.csv".format(employee_id)

    # Write to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                            username, task['completed'], task['title']])

    print("CSV file generated: {}".format(csv_file))
