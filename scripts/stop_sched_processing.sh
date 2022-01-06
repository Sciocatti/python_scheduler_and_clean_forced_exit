#!/bin/bash

# * This is the term to grep for. In our case, the executing PYTHONPATH for the script we want to kill
SEARCH_TERM='python3 python_scheduler_and_clean_forced_exit'
PYTHON_PID=$(ps -fA | grep -v grep | grep "$SEARCH_TERM" | xargs -l bash -c 'echo $1')

if [ ! -z "$PYTHON_PID" ];
    then 
        echo "PID found: ${PYTHON_PID}. Killing process."
        sudo kill -2 $PYTHON_PID
else
    echo 'No PID found'
fi