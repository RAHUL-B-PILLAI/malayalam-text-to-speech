import pytesseract as ocr

img= ocr.image_to_string('/ocr/download.jpeg',lang='mal')
print(img)
