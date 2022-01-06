# python_scheduler_and_clean_forced_exit
A basic Python scheduler and a listener to help cleanly exit python scripts.

The idea is to be able to schedule large jobs, and have them finish before being killed if the script was killed. DB changes, close network sockets, finish file uploads/downloads first, then exit.

## Usage
### As-is
- Look at `/src/tasks/dummy_task.py` to determine the function layout. Make your own version.
- Expand `/src/tasks/__init__.py` to import your function. Not needed, but looks better.
- Look at `__main__.py` to see how the dummy function is used. Do note that the function parameters are named.
- Copy the dummy implementation for your one.

### As a package
- Copy this folder into your project.
- Import classes:
```python
from python_scheduler_and_clean_forced_exit import ScheduledTask, GracefulKiller
```

## Todo
Very rough implementaion.
- Handle responses from functions to determine if a job is done. Currently the options are always repeat (interval set), or run once (no interval set).
- Add option to force kill application if the trigger is not handled.
- Cleanup.
- Documentation.
