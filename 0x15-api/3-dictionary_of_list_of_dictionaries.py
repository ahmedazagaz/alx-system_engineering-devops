#!/usr/bin/python3
"""DATA-API"""
import json
import requests


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    r1 = requests.get('{}/users'.format(api_url))
    employees = r1.json()
    data = {}
    for employee in employees:
        tasks_list = []
        data[employee.get('id')] = tasks_list
        r2 = requests.get('{}/todos?userId={}'.format(
            api_url,
            employee.get('id')
        ))
        tasks = r2.json()
        for t in tasks:
            tasks_list.append({
                "username": employee.get('username'),
                "task": t.get('title'),
                "completed": t.get('completed')
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
