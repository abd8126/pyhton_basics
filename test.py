import requests
import json

url = "https://wyadp23eri.execute-api.eu-west-2.amazonaws.com/cw356_dev/s3.a.txt"

headers = {"Authorization": "token-e9d44f8569bcf0f9"}


response = requests.post(url, headers=headers)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
