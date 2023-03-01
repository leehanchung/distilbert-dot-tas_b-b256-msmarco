import base64
import requests
from io import BytesIO

model_inputs = {
    "passage": "This is a good day to die."
}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())