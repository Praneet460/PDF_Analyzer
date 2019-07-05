import requests


def downloader(file_url):
    url = file_url 
    r = requests.get(url, stream = True)
    filename = url.rsplit('/', 1)[-1]
    print(filename)
    with open(f"../uploaded_data/{filename}","wb") as pdf: 
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                pdf.write(chunk) 
    
    return filename
    

if __name__ == '__main__':
    downloader("https://www.db-book.com/db4/slide-dir/ch1-2.pdf")