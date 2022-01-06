import time
import logging
from datetime import datetime, timedelta

class ScheduledTask:
    def __init__(self,
                 execution_function=None,
                 execution_function_args = None, 
                 next_execution_time:datetime or None = None,
                 interval_in_seconds: int or None = None,
                 tag: str = "TAG") -> None:
        self.next_execution_time = next_execution_time
        self.set_interval(interval_in_seconds)
        logging.info(f"Interval: {self.interval}")
        self.tag = tag
        self.execution_function = execution_function
        self.execution_function_args = execution_function_args
        logging.debug(f"{self.tag}: Initializing ScheduledPersonLinker")

    def set_interval(self, seconds: int or None = None):
        logging.info(f"interval: {seconds}")
        if not seconds or (seconds < 1):
            self.interval = None
            return
        self.interval = timedelta(seconds=seconds)

    def process(self) -> bool:
        # * No next_execution_time_set, so we are done
        if not self.next_execution_time: return False
        # * No function given to execute, so we are done?
        if not self.execution_function: return False
        now = datetime.now()
        # * It is not yet time to run this task
        if now < self.next_execution_time: return True
        logging.info(f"{self.tag}: Task started")
        logging.info(f"{self.tag}: Args: {self.execution_function_args}")
        if self.execution_function_args:
            self.execution_function(**self.execution_function_args)
        else:
            self.execution_function()
        if self.interval:
            self.next_execution_time += self.interval
            return True
        else:
            self.next_execution_time = None
            return False

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    def test_func(count):
        print(count)

    args = {
        "execution_function": test_func,
        "execution_function_args": {
            "count": 3
        },
        "next_execution_time": datetime.now(),
        "interval_in_seconds": 15,
        "tag": "RANDOM TEST"
    }
    st = ScheduledTask(**args)
    while st.process() == True:
        time.sleep(1)

