# third-party modules
try:
    from google.cloud import vision
    from wand.image import Image
    from PIL import Image as Img
except ImportError as ie:
    print("Make sure that you have installed all the modules mentioned in the 'reuirements.txt' file: {{ie}}")

# built-in modules
import io


# initialize
client = vision.ImageAnnotatorClient.from_service_account_json("./apiKey/MedUSA-9ea899b19d9e.json")


def google_txt_converter(FILEPATH, file_name, *args, **kwargs):

    file_name = file_name.split('.')[0]
    imgBlobs = []

    try:
        with Image(filename= FILEPATH, resolution = 300) as pdf:
            pdfImage = pdf.convert('jpeg')
            print(pdfImage)

    except Exception as exc:
        return exc

    else:
        for index, img in enumerate(pdfImage.sequence):
            print(index)
            print(img)
            page = Image(image = img)
            imgBlobs.append(page.make_blob('jpg'))

        # extracted_txt = []

        for imgBlob in imgBlobs:
            # im = Img.open(io.BytesIO(imgBlob))

            image = vision.types.Image(content=imgBlob)
            response = client.document_text_detection(image=image)
            document = response.full_text_annotation.text
            # extracted_txt.append(document.split('\n'))
        
            # print(extracted_txt)
            with open(f'../txt_files/{file_name}_gva.txt', 'a+', encoding="utf-8") as txtfile:
                txtfile.write(document)

       

        print("Task Completed !!")
        
        return file_name

if __name__ == '__main__':
    print(google_txt_converter('../uploaded_data/img_6-converted.pdf', 'img_6-converted.pdf'))