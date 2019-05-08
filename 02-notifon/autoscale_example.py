# coding: utf-8
import boto3
session = boto3.Session()
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up', MetricValue=5.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up', MetricValue=60.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up', MetricValue=60.0, BreachThreshold=70.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale up', MetricValue=510.0, BreachThreshold=70.0)
