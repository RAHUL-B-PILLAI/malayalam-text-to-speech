from playsound import playsound
from gtts import gTTS
import pytesseract as ocr
import PyPDF2
myfile=open('/home/rahul/Desktop/work folder/malayalam text to speech/ocr/story-11.pdf','rb',encoding='UTF-8')
pdf_reader=PyPDF2.PdfFileReader(myfile)
#print(pdf_reader.numPages)
page_one=pdf_reader.getPage(0)
print(page_one.extractText())
#img= ocr.image_to_string('/home/rahul/Desktop/work folder/malayalam text to speech/ocr/download.jpeg',lang='mal')
#print(img)
#malayalam_text=input("enter malayalam text ")
#obv =gTTS(img,lang='ml',slow=False)
#obv.save('speech.mp3')
#playsound('speech.mp3')