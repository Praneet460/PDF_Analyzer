# helper.py

##########################
# AUTHOR : PRANEET NIGAM
##########################

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_files(filename:str):
    
    return '.' in filename and \
           filename.rsplit(sep = '.', maxsplit = 1)[1].lower() in ALLOWED_EXTENSIONS
    


if __name__ == '__main__':

    print(allowed_files('C:\\User\oo.pdf'))