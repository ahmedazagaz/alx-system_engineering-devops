#!/usr/bin/python3
"""DATA-API"""
import csv
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    r1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = r1.json().get('username')
    r2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = r2.json()
    with open('{}.csv'.format(employee_id), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in responses:
            writer.writerow([
                employee_id,
                employee_username,
                task.get('completed'),
                task.get('title')
            ])
