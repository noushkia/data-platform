import os
import docker

from workflows.models import DockerTaskExecution, TaskExecution
from workflows.services.docker import DockerTaskService


class PythonTaskService(DockerTaskService):
    def run_task(self, task):
        file_path = os.path.abspath(str(task.pythontask.python_file))
        client = docker.from_env()
        container = client.containers.run("python", detach=True, volumes={
            file_path: {"bind": "/run_file.py", "mode": "ro"}}, command="python3 /run_file.py")
        DockerTaskExecution.objects.create(task=task, container_id=container.id,
                                           status=TaskExecution.StatusChoices.RUNNING)