import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import kogpt2_text_generation
import kogpt2_transformers
import model.kogpt2
import naver_stt
import text_summarize
import re
import create_txt
import create_summarize
from active import active_func

class Watcher:
    DIRECTORY_TO_WATCH = "voice_recorder"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                # if not os.path.isdir("voice_recoder"):
                #     os.mkdir("voice_recoder")
                # if not os.path.isdir("text_folder"):
                #     os.mkdir("text_folder")
                time.sleep(5)
                
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):
    
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            voice_path = "voice_recorder"
            new_text_file = os.listdir("voice_recorder")
            with open(voice_path + "/" + new_text_file[-1]) as f:
                stt_result = f.read()
                stt_result = stt_result.replace("\n", "").replace(" ", "")
            active_func(stt_result)
            for i in new_text_file:
                os.remove(voice_path + "/" + i)



if __name__ == '__main__':
    print ('Sites folder watchdog is running...')
    w = Watcher()
    w.run()
