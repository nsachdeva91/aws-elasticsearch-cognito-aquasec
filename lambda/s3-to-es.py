import boto3
import re
import requests
import json
from requests_aws4auth import AWS4Auth

region = 'us-east-1'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = '' # the Amazon ES domain, including https://
index = 'aquasec' # You can pesonalize it as you whish
type = '_doc'
url = host + '/' + index + '/' + type + '/'

headers = { "Content-Type": "application/json" }

s3 = boto3.client('s3')

# Regular expressions used to parse some simple log lines
# ip_pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
# time_pattern = re.compile('\[(\d+\/\w\w\w\/\d\d\d\d:\d\d:\d\d:\d\d\s-\d\d\d\d)\]')
# message_pattern = re.compile('\"(.+)\"')

# Lambda execution starts here
def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    for record in event['Records']:
        # Get the bucket name and key for the new file
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Get, read, and split the file into lines
        obj = s3.get_object(Bucket=bucket, Key=key)
        file_content = obj['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        # json_content = json.load(json_file)
        for line in json_content['tests']:
            document = line
            r = requests.post(url, auth=awsauth, json=document, headers=headers)
            # print(document) 