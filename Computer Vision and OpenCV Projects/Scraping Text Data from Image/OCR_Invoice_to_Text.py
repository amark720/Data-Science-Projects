'''
step1. GoTo Command Prompt and install pytesseract package using command 'pip install pytesseract'
step2. Goto this link - https://github.com/ub-mannheim/tesseract/wiki and download
'tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.' setup and Install it on your machine.

After that run the below code
'''

import pytesseract  # Importing the package installed in step1.
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/gsc-30431/AppData/Local/Tesseract-OCR/tesseract.exe"
# Provide the path of tesseract.exe file which was installed in step2


def convert():
    img = Image.open('C:/Users/gsc-30431/PycharmProjects/test1.py/Python_Projects/OCR_Img_to_Text/invoice4.png')
    # Provite the path of Image which is to be converted into text
    text = pytesseract.image_to_string(img)
    print(text)
    return text


text = convert()
list = list(text.split('\n'))  # Splitting the list items line by line wise
list = [x for x in list if x]  # Removing blank spaces/items from the list
print(list)

item_start_index = list.index('Item')
item_end_index = list.index('Date')
date_end_index = list.index('‘Amount (E)')
amount_end_index = list.index('Reason')

dictionary = dict()
dictionary['Items'] = []
for i in range(item_start_index, item_end_index):
    dictionary['Items'].append(list[i])
print("Items are: ", dictionary['Items'])

dictionary['Date'] = []
for i in range(item_end_index + 1, date_end_index):
    dictionary['Date'].append(list[i])
print("Dates are: ", dictionary['Date'])

dictionary['Amount'] = []
for i in range(date_end_index + 1, date_end_index + 6):
    dictionary['Amount'].append(list[i])
print("Amount are: ", dictionary['Amount'])

dictionary['Reason'] = []
for i in range(amount_end_index + 1, amount_end_index + 6):
    dictionary['Reason'].append(list[i])
print("Reason are: ", dictionary['Reason'])

print(dictionary)