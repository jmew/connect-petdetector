import shutil
from urllib.request import urlopen
from IPython.display import Image, HTML, display
import requests
import json
import numpy as np
from base64 import b64encode
from scripts.print_predictions import parse_results

image_uri = "https://images.dog.ceo/breeds/beagle/n02088364_12154.jpg"
service_uri = 'http://52.180.90.254/score'

with urlopen(image_uri) as response:
    with open('temp.jpg', 'bw+') as f:
        shutil.copyfileobj(response, f)

def image_to_json(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    base64_bytes = b64encode(content)
    base64_string = base64_bytes.decode('utf-8')
    raw_data = {'image': base64_string}
    return json.dumps(raw_data, indent=2)

# Turn image into json and send an HTTP request to the prediction web service
input_data = image_to_json('temp.jpg')
headers = {'Content-Type':'application/json'}
resp = requests.post(service_uri, input_data, headers=headers)

# Extract predication results from the HTTP response
result = resp.text.strip("}\"").split("[")
parse_results(result)