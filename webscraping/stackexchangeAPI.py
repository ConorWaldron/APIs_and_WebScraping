import requests
import json

# returns a response object
response = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1698796800&todate=1700006400&order=desc&sort=activity&site=stackoverflow')
print(type(response))  # requests.models.Response
print(response)  # <Response [200]> which is a success message

# we convert it to a python dict with JSON
json_response = response.json()
print(json_response.keys())  # 'items', 'has_more', 'quota_max', 'quota_remaining'

# We access first item in list and see what keys it has
print(type(json_response['items']))  # list
print(type(json_response['items'][0]))  # dict
print(json_response['items'][0].keys())  # ['tags', 'owner', 'is_answered', 'view_count', 'bounty_amount', 'bounty_closes_date', 'answer_count', 'score', 'last_activity_date', 'creation_date', 'question_id', 'content_license', 'link', 'title'])

for item in json_response['items']:
    print(item['title']) # display the title of all the questions
    print(item['link']) # display the url link for each question
    print()