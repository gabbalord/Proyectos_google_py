#!/usr/bin/env python3
import requests
import os 

directory = "supplier-data/images"
url = "http://localhost/upload/"
for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
        with open(os.path.join(directory, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
