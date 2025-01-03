# pip install requests
 
import requests
 
api_key = "up_xFUU943s1zVo94CMuo4HRNBLBUCLK"  # ex: up_xxxYYYzzzAAAbbbCCC
filename = "./1.jpg"        # ex: ./image.png
model = "receipt-extraction"                # ex: receipt-extraction
 
url = f"https://api.upstage.ai/v1/document-ai/extraction"
headers = {"Authorization": f"Bearer {api_key}"}
 
files = {"document": open(filename, "rb")}
data = {"model": model}
 
response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())


if response.status_code == 200:
    result = response.json()
    fields = result.get('fields', [])
    for field in fields:
        refined_value = field.get('refinedValue', '')
        if refined_value:
            print(f"Refined Value: {refined_value}")
else:
    print("Error:", response.status_code, response.text)