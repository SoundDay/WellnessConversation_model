from gensim.summarization.summarizer import summarize

def summarize_text(text):

    return summarize(text, ratio=0.5)
