from workflows.models import DockerTask, PythonTask, Task, TaskExecution

tasks_data = {
    DockerTask:
        {
            "name": "Docker",
            "task_related_name": "dockertask",
            "execution_related_name": "dockertaskexecution",
            "display_fields": ["docker_image"],
        },

    PythonTask:
        {
            "name": "Python",
            "task_related_name": "pythontask",
            "execution_related_name": "pythontaskexecution",
            "display_fields": ["python_file"],
        }
}


def get_task_data(task):
    # convert task execution to task
    if isinstance(task, TaskExecution):
        task = task.task

    # convert inheritance object to task
    if task.__class__ != Task:
        task = task.task_ptr

    for model, data in tasks_data.items():
        if hasattr(task, data["task_related_name"]):
            return tasks_data[model]

    raise Exception("Service not found!")