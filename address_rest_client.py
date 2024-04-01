import requests
import sys

def fetch_data_from_url(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

model_name = sys.argv[1]

data = {
    "address": "12 / 89 spadina road",
    "model_name": model_name,
}

api_url = "https://41b0-103-28-246-251.ngrok-free.app/predict/json"
json_data = fetch_data_from_url(api_url, data)

if json_data:
    print("json data:")
    print(json_data)


'''
How to run?

python address_rest_client.py address_20240227_2
'''