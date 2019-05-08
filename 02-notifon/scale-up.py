# coding: utf-8
import boto3
session = boto3.Session()
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up', MetricValue=510.0, BreachThreshold=70.0)
