#!/usr/bin/python3
"""DATA-API"""
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    r1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_name = r1.json().get('name')
    r2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = r2.json()
    done_tasks = [t for t in responses if t.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, len(done_tasks), len(responses)))
    for t in done_tasks:
        print('\t {}'.format(t.get('title')))
