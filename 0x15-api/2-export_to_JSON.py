#!/usr/bin/python3
"""DATA-API"""
import json
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    r1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = r1.json().get('username')
    r2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = r2.json()
    with open('{}.json'.format(employee_id), 'w') as file:
        tasks_list = []
        data = {employee_id: tasks_list}
        for t in responses:
            tasks_list.append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": employee_username
            })
        json.dump(data, file)
