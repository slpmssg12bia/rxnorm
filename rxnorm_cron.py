#!/usr/bin/python

import zipfile, requests, time, subprocess
from bs4 import BeautifulSoup
from io import BytesIO


dump_folder = "rxnormdump"

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
    downloaded = 0
    start = time.time()
    with requests.get(link, stream=True) as r:
        for chunk in r.iter_content(chunk_size=1024):
            downloaded += len(chunk)
            print(f"Downloaded {downloaded / 1024 / 1024:.2f} MB", end="\r", flush=True)
            content.write(chunk)
    print()
    end = time.time()
    print("Download Completed in {:.2f} seconds".format(end - start))    

    content.seek(0)
    zip_file = zipfile.ZipFile(content)
    zip_file.extractall(dump_folder)
    subprocess.run(["bash", "/home/ubuntu/rxnorm/rxnorm_dump_to_s3.sh"])
    subprocess.run(["bash", "/home/ubuntu/rxnorm/rxnorm_clean.sh"])


r = requests.get('https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html?_gl=1')
soup = BeautifulSoup(r.text, 'html.parser')
url = get_url(soup)
download_and_extract(url)
