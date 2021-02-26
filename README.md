# WellnessConversation_model

## 0. Data
- [AIHUB  윌니스 대화 데이터](https://aihub.or.kr/keti_data_board/language_intelligence) : 데이터를 신청 후 다운로드 가능
- [데이터 전처리](https://github.com/nawnoes/WellnessConversation-LanguageModel) : KoGPT2 model train 사용

## 1. Process
 1. Android 단말기에서 입력된 음성 입력받기
 2. 구글 STT를 통해 텍스트 파일로 변환
 3. Watchdog을 통해 STT 텍스트 파일이 생성되는 것을 확인
 4. 생성된 STT 텍스트 파일을 wellnessconversation 모델의 입력값으로 투입
 5. model process
 6. 모델의 결과값으로 심리 상담 데이터셋 기반 챗봇 답변 텍스트 파일 생성
 7. Android 단말기에서 텍스트 파일 가져가서 화면에 출력
 
## 2. Package
kobert-transformers==0.4.1  
kogpt2-transformers==0.3.0  
torch  
transformers==3.0.2  

## 3. How to run
 1. 'data' 폴더에 데이터 준비
 2. (0.Data)의 데이터 전처리를 통해 autoregressive 데이터 준비
 3. KoGPT2 학습 후 모델 'checkpoint'에 준비 
 4. run.py 실행
 5. Android 부분은 옆 repository에서 확인
 
## 4. Result
 Input : 앞으로 내가 뭘 해야 될지 모르겠고 너무 우울해  
 Output : 우울할 떄는 칭찬타임! 오늘의 잘한 일을 말해봐요  
   
 Input : 남자 친구랑 헤어졌어 근데 이게 너무 아프다  
 Output : 언젠가는 이별이 찾아오기 마련이죠  
 
## Reference
[WellnessConversation](https://github.com/nawnoes/WellnessConversation-LanguageModel)  
[train 방법 알려주는 블로그](https://rogerheederer.github.io/ChatBot_Wellness/)  
[chatbot data](https://github.com/songys/Chatbot_data)  
