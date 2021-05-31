import os
import sys
import time
from pathlib import Path
from os import sep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MonitorFolder(FileSystemEventHandler):
    file_name = "Sent"

    def on_created(self, event):
        print(event.src_path, event.event_type)

    def on_modified(self, event):
        print(event.src_path, event.event_type)

    def on_deleted(self, event):
        print(event.src_path, event.event_type)


if __name__ == "__main__":
    home_path = str(Path.home())
    path_file = f"{home_path}{sep}Documents"

    src_path = f"{home_path}{sep}Documents{sep}6xChb"

    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")
    observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
