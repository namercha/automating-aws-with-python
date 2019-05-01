# coding: utf-8
import boto3
session = boto3.Session()
s3 = session.resource('s3')
