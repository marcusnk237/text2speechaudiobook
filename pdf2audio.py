import pdfplumber as pp
from gtts import gTTS

def extractText(file_path):
    pdf_text = ''
    with pp.open(file_path) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text()
    return pdf_text


def text2mp3 (file_path , save_path,  lang ='en'):

    pdf2text = extractText(file_path)
    tts = gTTS(text=pdf2text, lang=lang)
    tts.save(save_path)
    
