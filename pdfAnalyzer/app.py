# third-party modules

try:
    from flask import Flask, render_template, url_for, redirect, request
    from werkzeug.utils import secure_filename
    from flask import send_from_directory

except ImportError as ie:
    print(f"Please install the required packages in the requirements.txt file: {ie}")

# built-in modules
import os

# our modules
from helper import allowed_files
from text_conversion import txt_converter
from file_downloader import downloader
from google_vision import google_txt_converter
from text_analyzer import txt_file_analyzer

# variable
UPLOAD_FOLDER = '../uploaded_data'

# initialize
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'secret key'

# redirect to local-host
@app.route('/', methods = ['POST', 'GET'])
def home():
    '''
    Main home page
    '''

    # In case of 'POST' request
    if request.method == 'POST':
        
        # check 'inputFile' in POST request
        # if 'inputFile' in request.files and request.form.get('tabular_data_pdf') == None:
        #     file = request.files['inputFile']

        #     if file.filename == '':
        #         return redirect(request.url)

        #     elif file and allowed_files(file.filename):
        #         filename = secure_filename(file.filename)
        #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         print(filename)

        #         # convert pdf file into the txt file
        #         fileName = txt_converter(
        #             FILEPATH = os.path.join(app.config['UPLOAD_FOLDER'], filename),
        #             file_name = filename)

        #         print(fileName)

        #         return render_template('./home/index.html', title = "Home Page", filename = str(fileName)+".txt" )
        #     else:
        #         return redirect(request.url)

        
        if 'inputFile' in request.files: # and request.form.get('tabular_data_pdf') != None
            file = request.files['inputFile']

            if file.filename == '':
                return redirect(request.url)

            elif file and allowed_files(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(filename)

                # convert pdf file into the txt file
                fileName_gva = google_txt_converter(
                    FILEPATH = os.path.join(app.config['UPLOAD_FOLDER'], filename),
                    file_name = filename)

                print(fileName_gva)

                return render_template('./home/index.html', title = "Home Page", filename = str(fileName_gva)+"_gva.txt", analyze_pdf = str(fileName_gva)+"_gva.txt")
        
        if 'pdfUrl' in request.form:
            pdf_url = request.form['pdfUrl']
            print(pdf_url)
            file_name = downloader(pdf_url)

            # convert pdf file into the images
            fileName = google_txt_converter(
                FILEPATH = os.path.join(app.config['UPLOAD_FOLDER'], file_name),
                    file_name = file_name)

            return render_template('./home/index.html', title = "Home Page", filename = str(fileName)+"_gva.txt", analyze_pdf = str(fileName)+"_gva.txt" )

        else:
            return "No work to do."
                

    else:
        return render_template('./home/index.html', title = "Home Page")



@app.route('/<filename>')
def view_file(filename):
    return send_from_directory("../txt_files", filename)

@app.route('/original/<filename>')
def view_original_file(filename):
    file_name = filename.split('_gva')[0] + '.pdf'
    return send_from_directory("../uploaded_data", file_name)

@app.route('/analyzer/<filename>')
def analyze_pdf_page(filename):
    output_data = txt_file_analyzer(f"../txt_files/{filename}")
    return render_template('./home/analyzer.html', title = "PDF Analysis", output_data = output_data)

if __name__ == '__main__':
    app.run(debug = True)