import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class ActionHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_server()

    def start_server(self):
        if self.process:
            self.process.kill()
        print("Iniciando o servidor de ações...")
        self.process = subprocess.Popen(["rasa", "run", "actions"])

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print("Alteração detectada. Reiniciando o servidor de ações...")
            self.start_server()

if __name__ == "__main__":
    path = "./actions"
    event_handler = ActionHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
