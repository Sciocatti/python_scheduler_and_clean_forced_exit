import logging
import traceback

def dummy_function(dummy_arg1, dummy_arg2) -> None:
    try:
        # Execution here
        print(dummy_arg1, dummy_arg2)
    except Exception as e:
        # Handle exceptions here. Of course adjust to the appropriate level.
        # We don't want it to propagate to the top as the other tasks
        # might be affected
        logging.error(f"Exception. Catch and handle responsibly.")
        logging.error(f"e")
        traceback.print_exc()
    finally:
        # Do stuff like closing DB connections
        pass