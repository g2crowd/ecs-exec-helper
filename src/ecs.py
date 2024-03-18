import boto3
import jmespath


def get_ecs_task_description(cluster, task_id):
    client = boto3.client('ecs')
    return client.describe_tasks(cluster=cluster, tasks=[task_id])


def get_ecs_containers(task_desc):
    containers = jmespath.search('tasks[*].containers[*].name[]', task_desc)
    return filter(lambda x: x not in ["coralogix", "nginx"], containers)
