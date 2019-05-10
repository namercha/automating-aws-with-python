# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-05-10T00:01:43.970Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAJCAIPTDXJPVWA3YL4'}, 'requestParameters': {'sourceIPAddress': '173.79.14.179'}, 'responseElements': {'x-amz-request-id': '9B04BAF4E7F8D997', 'x-amz-id-2': 'Nd/BnFSaWeIi0CRHuHm7XDCmPJ0ibbJGjaSr8MHavUXR5OsMNnBcOEdd7mCDwmIFo7mOlQStCco='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '6d122522-6e38-4ecb-b7eb-1430a6e18f52', 'bucket': {'name': 'nabimdeletethisbucket12345', 'ownerIdentity': {'principalId': 'A2JVTU9DYY11Z'}, 'arn': 'arn:aws:s3:::nabimdeletethisbucket12345'}, 'object': {'key': 'Pexels+Videos+1675442.mp4', 'size': 3437849, 'eTag': '772a1e63b559c5cb3281bf5271a12644', 'sequencer': '005CD4BF675F0641F0'}}}]}
event
event['Record'][0]
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
