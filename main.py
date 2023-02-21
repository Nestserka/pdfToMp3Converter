import pyttsx3
import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open("sample_file.pdf", 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'sample_audio_file.aiff')
speaker.runAndWait()
