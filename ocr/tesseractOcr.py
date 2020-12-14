import pytesseract as ocr

img= ocr.image_to_string('/home/rahul/Desktop/work folder/malayalam text to speech/ocr/download.jpeg',lang='mal')
print(img)