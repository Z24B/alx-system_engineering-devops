#!/usr/bin/python3
"""Export data to CSV."""

import sys
import requests
import csv

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
    username = user_info.get('username')

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID",
                        "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            writer.writerow([employee_id,
                            username,
                            task['completed'],
                            task['title']])

    print("CSV file generated: {}".format(csv_file))
