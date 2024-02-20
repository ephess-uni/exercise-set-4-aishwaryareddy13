""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Calculate the time between shutdown events in gievn logfile.
    """
    shutdown_events = get_shutdown_events(logfile)
    if not shutdown_events:
        return None
    shutdown_times = [logstamp_to_datetime(event.split()[1]) for event in shutdown_events]
    time_difference = max(shutdown_times) - min(shutdown_times)
    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
