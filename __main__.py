import logging, sys
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

import src.tasks
from src.scheduled_task import ScheduledTask
from src.graceful_killer import GracefulKiller

base_args = {
    "execution_function": None,
    "execution_function_args": None,
    "next_execution_time": datetime.now(),
    "interval_in_seconds": 5,
    "tag": "PERSON_LINKER"
}

dummy_function_task_args = base_args.copy()
dummy_function_task_args["execution_function"] = src.tasks.dummy_function
dummy_function_task_args["tag"] = "DUMMY_FUNCTION"
dummy_function_task_args["execution_function_args"] = {
    "dummy_arg1": "Arg1",
    "dummy_arg2": "Arg2"
}

scheduled_tasks = [
    ScheduledTask(**dummy_function_task_args),
]

# * Using a gracefull killer so that we can complete the current loop before we shut down
gs = GracefulKiller()

# * The way the tasks work:
# *     If the scheduled task reaches the execution time,
# *     it will execute the function with the arguments provided.
# *     If an interval was set, then it will set a new execution time as
# *     the current execution time + the interval between executions.
# *     If no interval is set, then the task is finished and it will
# *     return False. If the task is still active it will return True.
# *     Once a task finishes, we remove it from the list, and if all tasks
# *     are finished we shut down.
while not gs.kill_now:
    for task in scheduled_tasks:
        if task.process() == False:
            scheduled_tasks.remove(task)
    if len(scheduled_tasks) == 0:
        logging.warning("All tasks completed and no next_execution_times are set")
        # * Force the application to exit with status code 2, equivalent to Ctrl+C
        sys.exit(2)

logging.warning("Kill signal received. Shutting down")