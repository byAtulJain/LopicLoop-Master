from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

import requests
import random
from challenges.models import Problem, TestCase

difficulty_map = {
  '8kyu': 'Easy',
  '7kyu': 'Medium',
  '6kyu': 'Hard'
}

difficulties = ['8kyu', '7kyu', '6kyu']
kyu_points = {
  '8kyu': 10,
  '7kyu': 20,
  '6kyu': 30
} 

for difficulty in difficulties:

  for i in range(20):

    url = f'https://www.codewars.com/api/v1/code-challenges/python/{difficulty}/random'
    response = requests.get(url)
    #data = response.json()
    print(response)
    # problem = Problem()
    # problem.title = data['name'] 
    # problem.statement = data['description']
    # problem.difficulty = difficulty_map[data['rank']]
    # problem.points = kyu_points[data['rank']]
    # problem.save()

    # for testcase in data['testCases']:
    #   case = TestCase(problem=problem)
    #   case.input_data = testcase['input']
    #   case.expected_output = testcase['expected']  
    #   case.save()

print("Inserted 20 random challenges for each difficulty level!")