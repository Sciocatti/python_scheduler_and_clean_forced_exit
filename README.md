# python_scheduler_and_clean_forced_exit
A basic Python scheduler and a listener to help cleanly exit python scripts.

The idea is to be able to schedule large jobs, and have them finish before being killed if the script was killed. DB changes, close network sockets, finish file uploads/downloads first, then exit.

## Todo
Very rough implementaion.
- Handle responses from functions to determine if a job is done. Currently the options are always repeat (interval set), or run once (no interval set).
- Add option to force kill application if the trigger is not handled.
- Cleanup.
