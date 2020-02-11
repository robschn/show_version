# example from https://github.com/ktbyers/netmiko/blob/develop/examples/use_cases/case16_concurrency/threads_netmiko.py

import threading
from datetime import datetime
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from my_devices import device_list as devices

def show_version(a_device):
    """Execute show version command using Netmiko"""
    remote_conn = ConnectHandler(**a_device)
    print(remote_conn.send_command_expect("show version"))


def main():
    """
    Use threads and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this.
    """
    start_time = datetime.now()

    for a_device in devices:
        my_thread = threading.Thread(target=show_version, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()