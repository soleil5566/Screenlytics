""" import psutil
import win32gui
import win32process

def get_active_process_name():
    win32gui.GetForegroundWindow()
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)
    print(pid)
    return process.name()

process_name = get_active_process_name()

last_process = None

while True:
    current_process = get_active_process_name()

    if current_process != last_process:
        print(current_process)
        last_process = current_process """

import time
import psutil
import win32gui
import win32process


def get_active_process_name():
    hwnd = win32gui.GetForegroundWindow()

    if hwnd == 0:
        return None

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    if pid == 0:
        return None

    try:
        process = psutil.Process(pid)
        return process.name()

    except psutil.NoSuchProcess:
        return None

    except psutil.AccessDenied:
        return None

    except psutil.ZombieProcess:
        return None


last_process = None

while True:
    current_process = get_active_process_name()

    if current_process is None:
        time.sleep(0.2)
        continue

    if current_process != last_process:
        print(current_process)
        last_process = current_process

    time.sleep(0.2)