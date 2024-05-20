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
    username = user_info.get('username')

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        fieldnames = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({'USER_ID': employee_id,
                             'USERNAME': username,
                             'TASK_COMPLETED_STATUS': task['completed'],
                             'TASK_TITLE': task['title']})
