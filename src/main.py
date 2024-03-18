import argparse

from ecs import get_ecs_task_description, get_ecs_containers
from git import create_comment
from utils import create_body


def put_comment(org, repo, pr, cluster, task):
    task_desc = get_ecs_task_description(cluster, task)
    containers = get_ecs_containers(task_desc)

    body = create_body(cluster, task, containers)

    create_comment(org, repo, pr, body)


def main(command_line=None):
    parser = argparse.ArgumentParser(
        description=""
    )

    parser.add_argument("-o", "--org", required=True)
    parser.add_argument("-r", "--repo", required=True)
    parser.add_argument("-p", "--pr", required=True)
    parser.add_argument("-c", "--cluster", required=True)
    parser.add_argument("-t", "--task", required=True)

    args = parser.parse_args(command_line)

    put_comment(
        args.org,
        args.repo,
        args.pr,
        args.cluster,
        args.task
    )


if __name__ == "__main__":
    main()
