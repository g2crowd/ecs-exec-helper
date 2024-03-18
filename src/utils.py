import logging


LOGGER = logging.getLogger("root")
ENV_FILE = ".env_vars"


def create_container_body(cluster, task_id, container):
    return f""" To connect to __{container}__ container please copy the following command into your terminal:
    
    aws ecs execute-command \\
      --region us-east-1 \\
      --cluster {cluster} \\
      --task {task_id} \\
      --container {container} \\
      --command "/bin/bash" \\
      --profile $AWS_PROFILE \\
      --interactive \n\n"""


def create_body(cluster, task_id, containers):
    comment = ""
    for container in containers:
        comment += create_container_body(cluster, task_id, container)
    return comment


def export_env(key, value):
    env_file = open(ENV_FILE, "a")
    env = "{}={}".format(key, value)
    print(env, file=env_file)
    env_file.close()


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt="[%(levelname)s] %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
