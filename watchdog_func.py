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
import watchdog_func
from active import active_func

class Target:
    watchDir = 'voice_recorder'
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, 
                                                       recursive=True)
        
        self.observer.start()
        try:
            while True:
                print("1s")
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        event_source = event.src_path
        event_source = event_source.replace("\\", "/")
        active_func(event_source)

    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)
        print("삭제됐당")


w = Target()
w.run()