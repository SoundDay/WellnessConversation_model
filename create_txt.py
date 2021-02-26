import os
import time

def check_time():
    now = time.localtime()
    local_time = str(now.tm_year)+'.'+str(now.tm_mon)+'.'+str(now.tm_mday)
    return local_time

def createFolder(date_folder):
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)

def createTxt_dialog(contents, path):
    now = time.localtime()
    txt_name = path + '/' + "user.txt"
    f = open(txt_name, "w" , encoding="utf-8")
    f.write(contents)
    f.close()

def createTxt_answer(contents, path):
    now = time.localtime()
    txt_name = path + '/' + "ai.txt"
    f = open(txt_name, "w", encoding="utf-8")
    # contents = contents.replace("\n", "").replace(" ", "")
    f.write(contents)
    f.close()

def createTxt_summarize(contents, path):
    now = time.localtime()
    txt_name = path + '/' + "%04d.%02d.%02d_%02d.%02d.%02d_summarize.txt" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    f = open(txt_name, "w")
    f.write(contents)
    f.close()




