import os
import time
import text_summarize
import create_txt

def create_summarize_txt(path):
    now = time.localtime()
    local_time = str(now.tm_year)+'.'+str(now.tm_mon)+'.'+str(now.tm_mday)
    path_dir = 'text_folder/' + local_time
    file_list = os.listdir(path_dir)

    before_summarize = []

    for file in file_list:
        if len(file.split('_')) != 3:
            f = open(path_dir + '/' + file, 'r')
            contents = f.read()
            before_summarize.append(contents)
            f.close()
        if (file.split('_')[-1].split('.')[0] == 'summarize'):
            before_summarize.pop()
            before_summarize_string = '\n'.join(before_summarize)
            after_summarize_string = text_summarize.summarize_text(before_summarize_string)
            create_txt.createTxt_summarize(after_summarize_string, path)
        if (file == file_list[-1]):
            before_summarize_string = '\n'.join(before_summarize)
            after_summarize_string = text_summarize.summarize_text(before_summarize_string)
            create_txt.createTxt_summarize(after_summarize_string, path)

