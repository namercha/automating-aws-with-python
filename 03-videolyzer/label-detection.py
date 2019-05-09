# coding: utf-8
import boto3
session = boto3.Session()
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='nabilvideolyzervideos')
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/nabim/Downloads/*.mp4')
pathname = '~/Downloads/Pexels Videos 1466210.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
response['JobId']
job_id = response['JobId']
job_id
result = rekognition_client.get_label_detection(JobID=job_id)
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['labels']
result['label']
result['Labels']
len(result['Labels'])
