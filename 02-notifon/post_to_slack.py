# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = {"text": "Hello, world."}
requests.post(url, json=data)
get_ipython().run_line_magic('save', 'post_to_slack.py')
