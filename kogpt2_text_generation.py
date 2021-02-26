import os
import numpy as np
import torch
from model.kogpt2 import DialogKoGPT2
from kogpt2_transformers import get_kogpt2_tokenizer

data_path = "data/wellness_dialog_for_autoregressive_train.txt"
checkpoint_path = "checkpoint"
save_ckpt_path = f"{checkpoint_path}/kogpt2-catbot-wellness.pth"

# ctx = "cuda" if torch.cuda.is_available() else "cpu"
ctx = "cpu"
# ctx = 'cuda'
device = torch.device(ctx)


checkpoint = torch.load(save_ckpt_path, map_location=device)

model = DialogKoGPT2()
model.load_state_dict(checkpoint['model_state_dict'])

model.eval()

tokenizer = get_kogpt2_tokenizer()

count = 0
output_size = 200 

def chatbot_func(speech):
  sent = speech

  tokenized_indexs = tokenizer.encode(sent)
  input_ids = torch.tensor([tokenizer.bos_token_id,]  + tokenized_indexs +[tokenizer.eos_token_id]).unsqueeze(0)
  sample_output = model.generate(input_ids=input_ids)

  return (tokenizer.decode(sample_output[0].tolist()[len(tokenized_indexs)+1:],skip_special_tokens=True).split('.')[0])
