#!/usr/bin/python

import subprocess
import re
from bs4 import BeautifulSoup
import requests
import wget
import zipfile, requests
from io import BytesIO

def get_url(soup):
    for a in soup.select("a[href]"):
        if a.text.startswith('RxNorm_full_'):
            return a["href"]
    print("Error getting url")
    exit()

def download_and_extract(url):
    file_name = url.split('/')[-1]
    link = f"https://uts-ws.nlm.nih.gov/download?url={url}&apiKey=26f0779c-75cc-4611-a9f3-2e0c36f5a17d"
    content = BytesIO()
    print(f'Downloading {file_name}')
    with requests.get(link, stream=True) as r:
        for chunk in r.iter_content(chunk_size=1024):
            content.write(chunk)
    print("Download Completed")    
    content.seek(0)
    zip_file = zipfile.ZipFile(content)
    zip_file.extractall(file_name)
        
        subprocess.run(["mv", slashurl[1], "db.zip"])
        subprocess.run(["unzip", "db.zip"])
        print("uploading the latest dump to s3")
        subprocess.run(["bash", "/home/ubuntu/rxnorm/rxnorm_dump_to_s3.sh"])
        subprocess.run(["bash", "/home/ubuntu/rxnorm/rxnorm_clean.sh"])
        return

r = requests.get('https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html?_gl=1')
soup = BeautifulSoup(r.text, 'html.parser')
url = get_url(soup)
download_and_extract(url)
