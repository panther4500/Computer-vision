#Prabhat Panwar
#TSF TASK:6  Optical Character Recognition (ORC) using openCV and pytesseract
#Computer Vision & Internet of Things

#importing libraries
import cv2
import pytesseract

#pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#reading the image
img=cv2.imread('sample.png')

#image to string converter
def ocr(img):                                     
    text=pytesseract.image_to_string(img)
    return text

#convert image to grayscale
def gray(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#clarifies the image
def clarify(image):
    return cv2.medianBlur(image,5)

def thresholder(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img=gray(img)
img=thresholder(img)
img=clarify(img)

print(ocr(img))          #print the optical characters read on cli


