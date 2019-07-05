# pdf_to_imgs.py

#########################
# AUTHOR : PRANEET NIGAM
#########################

# third-party modules
try: 
    from wand.image import Image
    from tqdm import tqdm
    from PIL import Image as Img
    import pytesseract
except ImportError as ie:
    print(f"Make sure that you have installed the required packages : {ie}")

# built-in modules
import os
import io

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# return the images
def txt_converter(FILEPATH, file_name, *args, **kwargs):

    file_name = file_name.split('.')[0]
    imgBlobs = []

    try:
        with Image(filename= FILEPATH, resolution = 300) as pdf:
            pdfImage = pdf.convert('jpeg')
            print(pdfImage)


    except Exception as exc:
        return exc

    else:
        for index, img in tqdm(enumerate(pdfImage.sequence)):
            print(index)
            print(img)
            page = Image(image = img)
            imgBlobs.append(page.make_blob('jpg'))


        extracted_txt = []

        for imgBlob in imgBlobs:
            im = Img.open(io.BytesIO(imgBlob))
            text = pytesseract.image_to_string(im, lang ='eng')
            extracted_txt.append(text)

        data = '\n'.join(extracted_txt)

        with open(f'../txt_files/{file_name}.txt', mode = "a+") as txtfile:
            txtfile.write(data)

        print("Task Completed!!!!!")

        return file_name

        

    



if __name__ == '__main__':
    FILEPATH = ''
    file_name = ''
    print(txt_converter(FILEPATH, file_name))

