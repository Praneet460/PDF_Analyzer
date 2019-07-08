# text_analyzer.py

# Analyze the text

import re 

def txt_file_analyzer(file_path):

    result_dict = {}

    date_lst = []

    no_of_records = []
    start_end_date = []
    date_filled = []
    date_dob = []
    address_lst = []


    with open(file_path, 'r', encoding="utf8") as file:
        data = file.read()
    
    matches_no_of_record = re.findall(r'[A-za-z]{7}:\s+\d+', data)
    matches_start_end_date = re.findall(r'[A-Za-z]{4}:\s+\d\d/\d\d?/\d\d\d\d', data)   
    matches_date = re.findall(r'\d\d\d\d-\d\d-\d\d', data)
    matches_address = re.findall(r'\d\d\d\d\d\s+[A-Za-z]+\s+[A-Za-z]+,?.?\s+[A-Za-z]+,\s+[A-Za-z]+\s+\d?[A-Z]?\d\d\d\d', data)

    for match in matches_date:
        date_lst.append(match)
    
    
    for match_record in matches_no_of_record:
        no_of_records.append(match_record.split(': ')[1])
    
    for match_start_end_date in matches_start_end_date:
        # print(match_start_end_date)
        start_end_date.append(match_start_end_date.split(': ')[1])


    for date in date_lst:
        if date.startswith('20'):
            date_filled.append(date)
        else:
            date_dob.append(date)
    

    for match_add in matches_address:
        address_lst.append(match_add)

    

    result_dict.update({'Number of Records' : no_of_records[0]})
    result_dict.update({'Start Date' : start_end_date[0]})
    result_dict.update({'End Date' : start_end_date[1]})
    result_dict.update({'Date Filled' : date_filled})
    result_dict.update({'DOB' : date_dob})
    result_dict.update({'Address' : address_lst})
   
    return result_dict

if __name__ == '__main__':
    print(txt_file_analyzer('../txt_files/sample_pdf_gva.txt'))