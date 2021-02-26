import kogpt2_text_generation
import kogpt2_transformers
import model.kogpt2
import naver_stt
import text_summarize
import re
import create_txt
import create_summarize

def active_func(stt_result):
    #STT
    # input_file = filename
    # stt_result = naver_stt.naver_stt_api(input_file)
    # stt_result = re.sub('[{}\'\"]', '', stt_result.split(":")[1])
    print("STT_finish")
    #Chat_bot model
    wellness_answer = kogpt2_text_generation.chatbot_func(stt_result)
    print("wellness_answer finish")

    #create_txt_file or folder
    local_time = create_txt.check_time()
    create_path = 'text_folder/'
    create_txt.createFolder(create_path)
    create_txt.createTxt_dialog(stt_result, create_path)
    create_txt.createTxt_answer(wellness_answer, create_path)
    print("create_txt finish")

    #create_summarize_txt_file
    # create_summarize.create_summarize_txt(create_path)

# if __name__ =='__main__':
#     active_func('voice_recorder/hac.m4a') 